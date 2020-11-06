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

TGREEN =  '\033[32m' # Green Text
TWHITE = '\033[37m'

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
WP_now = "5.5.1." # Manually added from https://api.wordpress.org/core/version-check/1.7/
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

print(" ")
print("Target website " + website + " is running on CMS " + WP_name + " of version " +WP_version)
print("Latest version is " + TGREEN + WP_now,TWHITE)
print("Scan finished " + current_time)

searchsploit = input("Do you want to use searchsploit to check exploits for this version? (y/n) ")
if searchsploit == "y":
    print(" ")
    print(os.system("searchsploit " + WP_pars))
else:
    print("DONE")
