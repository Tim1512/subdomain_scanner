# Subdomain Scanner ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg) - [![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT) - [![HitCount](http://hits.dwyl.io/cr4shcod3/subdomain_scanner.svg)](http://hits.dwyl.io/cr4shcod3/subdomain_scanner)

> Subdomain Scanner is a python tool designed to enumerate subdomains on a target domain through a wordlist.

## Getting Started
> Please ensure to have Python 2 or Python 3 in your system. Install the required dependencies to run the script.

## Installation

### Requirements

* Python 2
* or
* Python 3

### Installing

`$ pip install -r requirements.txt`

OR

```
$ pip install requests
$ pip install future
$ pip install python-whois
```

### Usage
```
usage: subdomain.py [-h] [-u URL] [-l NUM] [-cl FILE] [-o FILE]

Python Subdomain Scanner Created By: Cr4sHCoD3

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     "Set the target URL." [http://example.com]
  -l NUM, --list NUM    "Set the wordlist to be used." [100] / [500] / [1000]
                        / [10000] / [uk-500] / [uk-1000] / [default]
  -cl FILE, --custom-list FILE
                        "Set the wordlist in your own custom wordlist."
                        [Filename.txt]
  -o FILE, --output FILE
                        "Set the output file." [output.txt]
```

Example:
```
$ python subdomain.py
$ python subdomain.py -u http://example.com
$ python subdomain.py -u http://example.com -l 100
$ python subdomain.py -l 100
$ python subdomain.py -u http://example.com -cl filename.txt
$ python subdomain.py -cl filename.txt
$ python subdomain.py -u http://example.com -l 100 -o filename.txt
"It doesn't matter if you miss one argument."
```
Output:
```
[ Configuration ]
URL = http://google.com
Wordlist = wordlist/s-100.txt
Subdomains = 100
Output = subdomains_output.txt

[ Subdomain Scanner ]
[+] 200 - http://www.google.com ( US - 108.177.97.106)
[+] 200 - http://images.google.com ( US - 172.217.31.174)
[+] 200 - http://ipv4.google.com ( US - 108.177.97.102)
[+] 200 - http://wap.google.com ( US - 172.217.26.14)
[+] 200 - http://video.google.com ( US - 172.217.31.174)
[+] 200 - http://search.google.com ( US - 172.217.26.14)
[+] 200 - http://dns.google.com ( US - 172.217.31.174)
[+] 200 - http://m.google.com ( US - 172.217.25.203)
[+] 200 - http://apps.google.com ( US - 172.217.26.14)
[+] 200 - http://blog.google.com ( US - 172.217.26.9)
[+] 200 - http://store.google.com ( US - 172.217.31.174)
[+] 200 - http://support.google.com ( US - 172.217.26.14)
[+] 200 - http://news.google.com ( US - 172.217.24.142)
[+] 200 - http://mobile.google.com ( US - 172.217.25.203)
[+] 200 - http://docs.google.com ( US - 172.217.26.14)
[+] 200 - http://chat.google.com ( US - 172.217.26.14)
[+] 200 - http://mail.google.com ( US - 172.217.31.165)
[+] 200 - http://calendar.google.com ( US - 172.217.26.14)
[+] 200 - http://sites.google.com ( US - 172.217.26.14)
[+] 200 - http://admin.google.com ( US - 172.217.24.142)
[#] 404 - http://web.google.com ( US - 172.217.26.14)
[#] 404 - http://email.google.com ( US - 172.217.26.14)
[#] 404 - http://api.google.com ( US - 172.217.31.164)
[#] 404 - http://download.google.com ( ? - 172.217.31.164)
[#] 404 - http://relay.google.com ( ? - 172.217.31.174)
[#] 404 - http://sms.google.com ( ? - 172.217.26.14)
[#] 404 - http://ads.google.com ( ? - 172.217.31.174)

[ Result ]
Valid = 20
Invalid = 72
Response Codes:
    400 = 0
    401 = 0
    403 = 0
    404 = 7
    500 = 0
    502 = 0
    503 = 0
    504 = 0
```

## Build With
* [Requests](https://github.com/requests/requests)
* [Python-whois](https://pypi.org/project/python-whois)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Authors
* [Cr4sHCoD3](https://www.facebook.com/cr4shcod3.py) - Subdomain Scanner

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit) - see the LICENSE file for details. You can do whatever you want. This is just a practice.
