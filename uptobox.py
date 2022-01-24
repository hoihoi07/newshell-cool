#Uptobox Downloader By SilentKiller Writen in python


import json
import re
import urllib.parse
from os import popen
from random import choice

import requests
import logging


#Enter Uptobox Token:
utk = "a308f973f081097d7f6ca38b9d807d6b2o45m"
url = input("Enter Url:")
link = re.findall(r'\bhttps?://.*uptobox\.com\S+', url)[0]
check = 'https://uptobox.com/api/user/me?token=%s' % (utk)
request = requests.get(check)
info = request.json()
premium = info["data"]["premium"]
try:
   link = re.findall(r'\bhttp?://.*uptobox\.com/dl\S+', url)[0]
   logging.info('Uptobox direct link')
   dl_url = url
except:
    if premium == 1:
        file_id = re.findall(r'\bhttps?://.*uptobox\.com/(\w+)', url)[0]
        file_link = 'https://uptobox.com/api/link?token=%s&file_code=%s' % (utk, file_id)
        req = requests.get(file_link)
        result = req.json()
        dl_url = result['data']['dlLink']
    else:
        file_id = re.findall(r'\bhttps?://.*uptobox\.com/(\w+)', url)[0]
        file_link = 'https://uptobox.com/api/link?token=%s&file_code=%s' % (utk, file_id)
        req = requests.get(file_link)
        result = req.json()
        waiting_time = result["data"]["waiting"] + 1
        waiting_token = result["data"]["waitingToken"]
        _countdown(waiting_time)
        file_link = 'https://uptobox.com/api/link?token=%s&file_code=%s&waitingToken=%s' % (utk, file_id, waiting_token)
        req = requests.get(file_link)
        result = req.json()
        dl_url = result['data']['dlLink']    
    print(dl_url)            