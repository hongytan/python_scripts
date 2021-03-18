# python3
# Downloads every single comic from xkcd

import requests, os, bs4

url = 'https://xkcd.com' # Starting url
os.makedirs('xkcd',exist_ok=True) # Store comics in ./xkcd
while not url.endswith('#'):
    
    # Download the page
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'html.parser')

    # Find the URL of the comic page
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print(f"Could not find comic image on {url}.")
    else:
        comicURL = 'https:' + comicElem[0].get('src')

        # Download the image
        res = requests.get(comicURL)
        res.raise_for_status()

        # Save the image to ./xkcd
        with open(os.path.join('xkcd',os.path.basename(comicURL)),'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)
        
        # Get the Prev button's url
        prevElem = soup.select("a[rel='prev']")
        url = "https://xkcd.com/" + prevElem[0].get('href')

print("Done.")
