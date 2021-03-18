#! python3
# USAGE: python3 search.py <keyword>
# Opens first five search results on imgur.com
# NOTE: Doesn't work on ubuntu vm, need to fix sys.argv[]

import requests, sys, webbrowser, bs4
print("Searching...")
request = requests.get("https://imgur.com/search?q=" + ' '.join(sys.argv[1:]))
request.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(request.text,'html.parser')

# Open a new browser tab for each result
linkElems = soup.select('.image-list-link')
print("Links found:", len(linkElems))
numOpen = min(5,len(linkElems))
for i in range(numOpen):
    url = 'https://imgur.com' + linkElems[i].get('href')
    print("Opening:", url)
    webbrowser.open(url)