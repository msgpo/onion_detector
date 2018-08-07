'''
Onion Scanner v1.0
Python 3

Scanner generates random onion site, tries to connect, and stores successfull connections in a log file.

The log file is located in the same folder as the script file.

A timed out message for the onion means it was not detected as up. Do not go below 1 for this setting.

When a onion site is detected, the sites code from hte get request will be printed and the onion site will be logged in the log file.

Happy onion scanning!

Make sure to save the file to push settings changes.

If you get a socks error, try checking you proxy settings.  
             - 9050 or 9150 is the most common proxy ports to try 1st.

'''

import requests
import json
from itertools import product
from random import choice
import sys

#Settings:
#Log File Name:
logfile = 'onionsdetected.txt'

#values used in site address space:
domain_values = "abcdefghijklmnopqrstuvwxyz234567"

#Proxy port:
proxy = '9150'

#Connection timeout(Higher for slower connections; stay above 1):
time = 1.5

proxies = {
    'http': 'socks5h://127.0.0.1:' + proxy,
    }
print("\nOnion Detector, 2018\n")
print("This script creates a random onion site and uses a http GET request to if it is live.\nIf a site is detected, site code will be diplayed and it will be logged into a file for you to further investigate.\n")
print("\nA brute-force onion scanner created because why not?\n")
print("\n\n\n'Ambitous, yet rubbish.'")
print("\n                  -Clarkson\n")
print("\nPress 'CTRL + C' to exit")

#main loop:
with open(logfile, 'a') as f:
        x = 1
        while True:
            try:        
                onion = "".join([choice(domain_values) for _ in range(16)])#Creates random onion
                fullURL = "http://" + onion + ".onion"#Packages onion into url for request
                data = requests.get(fullURL, proxies=proxies, timeout=time).text#Data request
                print(data)#Print of data
                dataEntry = fullURL
                print(fullURL + " is active \n")
                f.write(dataEntry + "\n")
            #Exception City
            except requests.exceptions.ConnectTimeout:
                print ('Address: ' + fullURL + ' timed out. Nothing to see. Generating next onion site.')
            except requests.exceptions.RequestException as e:
                print(e)
                dataEntry = e
            except KeyboardInterrupt:#exit
                print ('\nFor results, Check:\n' + logfile + '\nThis is like finding a needle in a haystack.\nGood luck!' )
                sys.exit()

sys.exit()