'''
Here’s what your program does:

Loads the XKCD home page
Saves the comic image on that page
Follows the Previous Comic link
Repeats until it reaches the first comic
This means your code will need to do the following:

Download pages with the requests module.
Find the URL of the comic image for a page using Beautiful Soup.
Download and save the comic image to the hard drive with iter_content().
Find the URL of the Previous Comic link, and repeat.
'''

# ! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
while not url.endswith('#'):
    # TODO: Download the page.
    print("Downloading page %s..." % url)
    # TODO: Find the URL of the comic image.
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: Download the image.
    comicElem = soup.select("#comic img")
    print(comicElem)
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicURL = "https:" + comicElem[0].get("src")
        print("Downloading image %s..." % comicURL)
        res = requests.get(comicURL)
        res.raise_for_status()

    # TODO: Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)),
                     'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    # TODO: Get the Prev button's url.

    # break

print('Done.')
