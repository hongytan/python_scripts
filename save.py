# Saves downloaded files from internet to hard drive

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

res.raise_for_status()

with open('raj.txt','wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)
