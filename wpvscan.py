#!/usr/bin/env python
# Name: WPvSCAN
# https://github.com/cyb3rd3s/WPvSCAN
# Author: Roman Kulich @ 2020
# Version: v1.0.3
import bs4 as bs
import urllib.request
import time
import os
import argparse
import requests

TGREEN =  '\033[32m' # Green Text
TWHITE = '\033[37m' # White text
TRED = '\033[31m' # White text

print('''
 __          _______         _____  _____          _   _ 
 \ \        / /  __ \       / ____|/ ____|   /\   | \ | |
  \ \  /\  / /| |__) |_   _| (___ | |       /  \  |  \| |
   \ \/  \/ / |  ___/\ \ / /\___ \| |      / /\ \ | . ` |
    \  /\  /  | |     \ V / ____) | |____ / ____ \| |\  |
     \/  \/   |_|      \_/ |_____/ \_____/_/    \_\_| \_|                                                                                                                
v1.0.0
''')
print(TGREEN + "USAGE: wpvscan.py target.com", TWHITE)
print("")

response = requests.get('https://api.wordpress.org/core/version-check/1.7/')
json = response.json()

parser = argparse.ArgumentParser(description="Human Para")
parser.add_argument(dest='domain', help="wpvscan.py target.com")
args = parser.parse_args()

website = (args.domain)
source = urllib.request.urlopen('https://'+ website).read()
soup = bs.BeautifulSoup(source,'lxml')
WP_check = soup.find(attrs={'name' : 'generator'})
WP_pars = WP_check['content']
WP_name = WP_pars[0:9]
WP_version = WP_pars[10:15] + "." 
WP_now = str(json['offers'][0]['version'])
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

print(" ")
if WP_version == WP_now:
    print("Target website " + website + " is running on CMS " + WP_name + " of version " + TGREEN + WP_version,TWHITE)
else:
    print("Target website " + website + " is running on CMS " + WP_name + " of version " + TRED + WP_version,TWHITE)
print("Latest version is " + TGREEN + WP_now,TWHITE)
print("Scan finished " + current_time)

searchsploit = input("Do you want to use searchsploit to check exploits for this version? (y/n) ")
if searchsploit == "y":
    print(" ")
    print(os.system("searchsploit " + WP_pars))
else:
    print("DONE")
