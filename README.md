# pwned-passwords

A simple little script to check if a password is known to have been breached.

Uses the excellent Pwned Passwords V2 that Troy Hunt has so generously made publicly available.

Generally it is considered a bad idea to give a random site any password that is in use or that you are thinking of using, but don't worry, the method behind this service obfuscates the password. Read more at [this blog post] by the creator of the service, down under the heading "Cloudflare, Privacy and k-Anonymity". And as of June 2018, that is the [ONLY] search method the service allows, so you can rest easy knowing that your passwords are not being leaked.

[this blog post]: <https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/>
[ONLY]: <https://www.troyhunt.com/enhancing-pwned-passwords-privacy-by-exclusively-supporting-anonymity/>

### Prerequisites
Requires Python 3.6 or greater. Tested on Python 3.7.

### Setup
#### Mac/Linux
First, check to see if `python` points to Python2.x or >=Python3.6. In the terminal, run the command `python -V` If the response is `Python 2.x`, check to make sure `python3 -V` returns `Python 3.6` or greater. If both of these conditions are true, run the command `pip3 install --upgrade -r requirements.txt`. Otherwise, if `python -V` returns `Python 3.6` or greater, run the command `pip install --upgrade -r requirements.txt`.
#### Windows
Check to make sure `py -V` returns `Python 3.6` or greater. Then run `py -m pip install --upgrade -r requirements.txt`.

### Usage
```
$ python pwned_passwords.py --help
usage: pwned_passwords.py [-h] [-f FILE | -p PASSWORD]

Check password(s) against Pwned Passwords API.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File of you would like to check for pwnage, each line
                        containing semicolon-separated password and service
  -p PASSWORD, --password PASSWORD
                        Password you would like to check for pwnage
```

You may search either a single password or do a bulk search. Please note that only one option may be chosen. If you are searching a single password, the command will look something like `python pwned_passwords.py -p [password]`. If you are doing a bulk lookup, your command will look like `python pwned_passwords.py -f [filename]`.

If the second option is chosen, the input should be a text file of the following format:

```
password1;Source1
password2;Source2
```

The sources are only for ease of display and never leave your computeer. If you are doing a bulk-lookup without sources, feel free to use a random string or 'Source' or whatever.

Results will be displayed in your terminal.
