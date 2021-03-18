# python3
# USAGE: python3 imgur.py <keyword>
# Searches imgur.com for keyword and downloads the photos

import os, requests, sys, bs4, webbrowser

# Makes sure the usage is correct
if len(sys.argv) < 2:
    print("USAGE: python3 imgur.py <keyword>")
else:

    # Make ./imgur to store photos
    os.makedirs('imgur',exist_ok=True)

    # Gets the imgur URL with keyword search
    url = "https://imgur.com/search?q=" + ' '.join(sys.argv[1:])

    # Downloads the URL
    res = requests.get(url)
    res.raise_for_status()

    # Get the first image page
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    links = soup.select('.image-list-link')
    url = 'https://imgur.com' + links[0].get('href')

    # Downloads 10 pages
    for i in range(10):

        # Download the page
        res = requests.get(url)
        res.raise_for_status()

        # Get the image URL
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        imageElem = soup.select('.image-placeholder')

        if imageElem == []:
            print("Could not find image.")
            continue
        imageURL = imageElem[0].get('src')

        # Download the image to ./imgur folder
        res = requests.get(imageURL)
        res.raise_for_status()
        with open(os.path.join('./imgur',os.path.basename(imageURL)),'wb') as f:
            for chunk in res.iter_content(100000):
                f.write(chunk)

        # Gets the next image page
        nextImageElem = soup.select('.Navigation Navigation-next')
        url = 'https://imgur.com' + nextImageElem[0].get('href')


