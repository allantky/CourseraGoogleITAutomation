#!/usr/bin/env python3
import requests
import glob

url = "http://localhost/upload/"
for file in list(glob.glob('/home/student-03-80cf580f56e8/supplier-data/images/*.jpeg')):
  with open(file, 'rb') as opened:
    r = requests.post(url, files={'file': opened})
