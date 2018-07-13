import argparse
import hashlib

import requests

URL = 'https://api.pwnedpasswords.com/range/'

HEADERS = {'User-Agent': 'Quick-password-checker'}


# Hashes the password with SHA1
def sha1_hasher(password):
    pw_byte = password.encode()
    hasher = hashlib.sha1()
    hasher.update(pw_byte)
    return hasher.hexdigest()


# Splits the hash into a 5-character prefix (what leaves your computer) and a suffix (what is checked against the return)
def get_prefix_suffix(sha1):
    prefix = sha1[:5].upper()
    suffix = sha1[5:].upper()
    return prefix, suffix


# Api call
def get_pwned_passwords(prefix):
    url = f'{URL}{prefix}'
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return r.text


# Converts the weird-ass format to a Python object for lookup by key
def parse_response(response):
    l = response.split('\r\n')
    out = {}
    for entry in l:
        key, val = entry.split(':')
        out[key] = val
    return out


# Looks up pwnage count that matches the password suffix
def get_pwnage_count(parsed, suffix):
    try:
        return parsed[suffix]
    except KeyError:
        return '0'


# Full count-getting procedure; returns count
def pwnage_check(password):
    sha1 = sha1_hasher(password)
    prefix, suffix = get_prefix_suffix(sha1)
    resp = get_pwned_passwords(prefix)
    parsed = parse_response(resp)
    return get_pwnage_count(parsed, suffix)


def main():
    parser = argparse.ArgumentParser(description='Check password(s) against Pwned Passwords API.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='File of you would like to check for pwnage, each line containing semicolon-separated password and service')
    group.add_argument('-p', '--password', help='Password you would like to check for pwnage')
    args = parser.parse_args()

    # Bulk option
    if args.file is not None:
        # Open the text file and convert the format into a Python object
        with open(args.file, 'r') as fn:
            passwords = {}
            for line in fn:
                password, service = line.split(';')
                passwords[password.strip()] = service.strip()

        # Run a lookup on each password
        for password, service in passwords.items():
            count = pwnage_check(password)
            print(f'The password "{password}" (used for {service}) has been pwned {count} times.')

    # Single password option
    elif args.password is not None:
        count = pwnage_check(args.password)
        print(f'The password "{args.password}" has been pwned {count} times.')

    # Neither option chosen; tell the user to pick one and do nothing
    else:
        print('You must search either a password or bulk passwords. Please input one or the other and try again.')


if __name__ == '__main__':
    main()
