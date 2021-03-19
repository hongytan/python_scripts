# python3
# USAGE: python3 link.py <link>
# Opens links on given webpage in new tabs

import sys, requests, bs4, webbrowser

# Download the link
res = requests.get(sys.argv[1])
res.raise_for_status()

# Search for all the links within page
soup = bs4.BeautifulSoup(res.text,'html.parser')
links = soup.select('a')

# Opens a max of 5 links from the webpages
for i in range(min(len(links),5)):
    # Get the URL
    url = links[i].get('href')

    # Opens the URL in a new tab
    try: 
        webbrowser.open(url)
    except:  
        print('There was a 404 error.')
    



