#!/usr/bin/env python
# Author: Roman Kulich @ 2020
# Version: v1.0.0
import bs4 as bs
import urllib.request

print('''
▄▄▌ ▐ ▄▌ ▄▄▄· ▌ ▐·▄▄▄ .▄▄▄  .▄▄ · ▪         ▐ ▄ 
██· █▌▐█▐█ ▄█▪█·█▌▀▄.▀·▀▄ █·▐█ ▀. ██ ▪     •█▌▐█
██▪▐█▐▐▌ ██▀·▐█▐█•▐▀▀▪▄▐▀▀▄ ▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌
▐█▌██▐█▌▐█▪·• ███ ▐█▄▄▌▐█•█▌▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌
 ▀▀▀▀ ▀▪.▀   . ▀   ▀▀▀ .▀  ▀ ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪
v1.0.0
''')
website = input("Enter website: ")
source = urllib.request.urlopen('https://'+ website).read()
soup = bs.BeautifulSoup(source,'lxml')
WP_check = soup.find(attrs={'name' : 'generator'})
WP_pars = WP_check['content']
WP_name = WP_pars[0:9]
WP_version = WP_pars[10:15] + "." 
WP_now = "5.5.1." # Manually added from https://api.wordpress.org/core/version-check/1.7/

print(" ")
print("Website " + website + " is running on CMS " + WP_name + " of version " +WP_version)
print("Latest version is " + WP_now)
