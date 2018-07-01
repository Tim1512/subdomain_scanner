#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Script Created By:
	Cr4sHCoD3
Copyrights:
	Cr4sHCoD3 2018
Special Mentions:
	PureHackers PH
	Blood Security Hackers
"""



import os
import sys
import platform
import time
import datetime
import argparse
import socket
from threading import Thread



try:
    import requests
    from requests.exceptions import ConnectionError
except:
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('clear')
    print  ("""
 o-o       o       o                           o-o
|          |       |               o          |
 o-o  o  o O-o   o-O o-o o-O-o  oo   o-o       o-o   o-o  oo o-o  o-o  o-o o-o
    | |  | |  | |  | | | | | | | | | |  |         | |    | | |  | |  | |-' |
o--o  o--o o-o   o-o o-o o o o o-o-| o  o     o--o   o-o o-o-o  o o  o o-o o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
    """)
    print ('[!] - Module (requests) not installed!')
    sys.exit()
try:
    import whois
except:
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    elif platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('clear')
    print  ("""
 o-o       o       o                           o-o
|          |       |               o          |
 o-o  o  o O-o   o-O o-o o-O-o  oo   o-o       o-o   o-o  oo o-o  o-o  o-o o-o
    | |  | |  | |  | | | | | | | | | |  |         | |    | | |  | |  | |-' |
o--o  o--o o-o   o-o o-o o o o o-o-| o  o     o--o   o-o o-o-o  o o  o o-o o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
    """)
    print ('[!] - Module (python-whois) not installed!\n[!] - Module (futures) not installed!')
    sys.exit()


# GLOBAL
urls = []
valid = []
rc_400 = []
rc_401 = []
rc_403 = []
rc_404 = []
rc_500 = []
rc_502 = []
rc_503 = []
rc_504 = []
invalid = []
month = datetime.date.today().strftime("%B")
if datetime.date.today().strftime("%w") == 1 or datetime.date.today().strftime("%w") == '1':
    day = 'Monday'
elif datetime.date.today().strftime("%w") == 2 or datetime.date.today().strftime("%w") == '2':
    day = 'Tuesay'
elif datetime.date.today().strftime("%w") == 3 or datetime.date.today().strftime("%w") == '3':
    day = 'Wednesday'
elif datetime.date.today().strftime("%w") == 4 or datetime.date.today().strftime("%w") == '4':
    day = 'Thursday'
elif datetime.date.today().strftime("%w") == 5 or datetime.date.today().strftime("%w") == '5':
    day = 'Friday'
elif datetime.date.today().strftime("%w") == 6 or datetime.date.today().strftime("%w") == '6':
    day = 'Saturday'
elif datetime.date.today().strftime("%w") == 7 or datetime.date.today().strftime("%w") == '0':
    day = 'Sunday'
mday = datetime.date.today().strftime("%d")
year = datetime.date.today().strftime("%Y")
current_datetime = datetime.datetime.now()
current_time = current_datetime.strftime('%I:%M:%S')



def clear():
	if platform.system() == 'Linux':
		os.system('clear')
	elif platform.system() == 'Windows':
		os.system('cls')
	elif platform.system() == 'Darwin':
		os.system('clear')
	else:
		os.system('clear')



def banner():
	print  ("""
 o-o       o       o                           o-o
|          |       |               o          |
 o-o  o  o O-o   o-O o-o o-O-o  oo   o-o       o-o   o-o  oo o-o  o-o  o-o o-o
    | |  | |  | |  | | | | | | | | | |  |         | |    | | |  | |  | |-' |
o--o  o--o o-o   o-o o-o o o o o-o-| o  o     o--o   o-o o-o-o  o o  o o-o o

Created By: Cr4sHCoD3 [ PureHackers | Blood Security Hackers ]
Github: https://github.com/cr4shcod3
	""")



def generate_urls():
    for i in list:
        n_hostname = i + '.' + hostname
        n_url = 'http://' + n_hostname
        urls.append(n_url)



def subdomain_scan(s_url):
    try:
        r = requests.get(s_url)
        if r.status_code == 200:
            valid.append(s_url)
        elif r.status_code == 400:
            rc_400.append(s_url)
        elif r.status_code == 401:
            rc_401.append(s_url)
        elif r.status_code == 403:
            rc_403.append(s_url)
        elif r.status_code == 404:
            rc_404.append(s_url)
        elif r.status_code == 500:
            rc_500.append(s_url)
        elif r.status_code == 502:
            rc_502.append(s_url)
        elif r.status_code == 503:
            rc_503.append(s_url)
        elif r.status_code == 504:
            rc_504.append(s_url)
        else:
            invalid.append(s_url)
    except ConnectionError:
        invalid.append(s_url)
        pass



def create_output():
    output_file.write('{0}: {1} {2}, {3} = {4}\n'.format(day, month, mday, year, current_time))
    output_file.write('URL: {0}\n'.format(url))
    output_file.write('Subdomains:\n')
    ii = 1
    for i in valid:
        output_file.write('  ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    output_file.write('Response Code:\n')
    ii = 1
    output_file.write('  400:\n')
    for i in rc_400:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  401:\n')
    for i in rc_401:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  403:\n')
    for i in rc_403:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  404:\n')
    for i in rc_404:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  500:\n')
    for i in rc_500:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  502:\n')
    for i in rc_502:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  503:\n')
    for i in rc_503:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    ii = 1
    output_file.write('  504:\n')
    for i in rc_504:
        output_file.write('    ' + str(ii) + '. {0}\n'.format(i))
        ii = ii + 1
    output_file.write('\n\n')



def main():
    generate_urls()
    print ("""
[ Configuration ]
URL = {0}
Wordlist = {1}
Subdomains = {2}
Output = {3}
""".format(url, l_file, len(list), output))
    try:
        for i in urls:
            t = Thread(target=subdomain_scan, args=(i,))
            t.start()
    except EOFError:
        print ('\n[+] - Exiting.')
        sys.exit()
    except KeyboardInterrupt:
        print ('\n[+] - Exiting.')
        sys.exit()
    try:
        t.join()
    except EOFError:
        print ('\n[+] - Exiting.')
        sys.exit()
    except KeyboardInterrupt:
        print ('\n[+] - Exiting.')
        sys.exit()
    print ("[ Subdomain Scanner ]")
    for i in valid:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[+] 200 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_400:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 400 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_401:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 401 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_403:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 403 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_404:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 404 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_500:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 500 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_502:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 502 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_503:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 503 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    for i in rc_504:
        hname = i.replace('http://', '')
        try:
            w = whois.whois(hname)
            country = w.country
        except Exception:
            country = '?'
            pass
        ip = socket.gethostbyname(hname)
        print ('[#] 504 - ' + i + ' ( ' + str(country) + ' - ' + ip + ') ')
    print ("""
[ Result ]
Valid = {0}
Invalid = {1}
Response Codes:
    400 = {2}
    401 = {3}
    403 = {4}
    404 = {5}
    500 = {6}
    502 = {7}
    503 = {8}
    504 = {9}
    """.format(len(valid), len(invalid), len(rc_400), len(rc_401), len(rc_403), len(rc_404), len(rc_500), len(rc_502), len(rc_503), len(rc_504)))
    create_output()



if __name__ == '__main__':
    clear()
    banner()
    parser = argparse.ArgumentParser(description='Python Subdomain Scanner Created By: Cr4sHCoD3')
    parser.add_argument('-u',
        '--url',
        metavar='URL',
        action='store',
        help='"Set the target URL." [http://example.com]',
        type=str)

    parser.add_argument('-l',
        '--list',
        choices=['default', '100', '500', '1000', '10000', 'uk-500', 'uk-1000'],
        default='default',
        metavar='NUM',
        action='store',
        help='"Set the wordlist to be used." [100] / [500] / [1000] / [10000] / [uk-500] / [uk-1000] / [default]')

    parser.add_argument('-cl',
        '--custom-list',
        metavar='FILE',
        default='wordlist/s.txt',
        action='store',
        help='"Set the wordlist in your own custom wordlist." [Filename.txt]')

    output = 'subdomains_output.txt'
    parser.add_argument('-o',
        '--output',
        default=output,
        metavar='FILE',
        action='store',
        help='"Set the output file." [output.txt]')

    args = parser.parse_args()
    if args.url is None:
        url = input('URL: ')
        if 'www.' in url:
            url = url.replace('www.', '')
        hostname = url.replace('http://', '')
    elif args.url is not None:
        url = args.url
        if 'www.' in url:
            url = url.replace('www.', '')
        hostname = url.replace('http://', '')
    if args.list == 'default':
        l_file = 'wordlist/s.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == '100':
        l_file = 'wordlist/s-100.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == '500':
        l_file = 'wordlist/s-500.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == '1000':
        l_file = 'wordlist/s-1000.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == '10000':
        l_file = 'wordlist/s-10000.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == 'uk-500':
        l_file = 'wordlist/suk-500.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    elif args.list == 'uk-1000':
        l_file = 'wordlist/suk-1000.txt'
        list_file = open(l_file, 'r')
        list = list_file.read().splitlines()
    else:
        l_file = 'wordlist/s.txt'
        list_file = open('wordlist/s.txt', 'r')
        list = list_file.read().splitlines()
    if args.list == 'default' and args.custom_list is not None:
        l_file = args.custom_list
        list_file = open(args.custom_list, 'r')
        list = list_file.read().splitlines()
    if args.custom_list is None:
        l_file = 'wordlist/s.txt'
        list_file = open('wordlist/s.txt', 'r')
        list = list_file.read().splitlines()
    if args.output == output:
        output_file = open(output, 'a+')
    elif args.output != output:
        if '.txt' in args.output:
            args.output = args.output + '.txt'
        output_file = open(args.output, 'a+')
    main()
