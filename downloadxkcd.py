# download every single xkcd comic

import requests, bs4, os

# starting URL
url = 'https://xkcd.com'

# storing comics in ./xkcd
os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):

    # Download the page
    print("Downloading page %s..." %url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "lxml")

    # find the URL of the comic image
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = 'https:' +  comic_elem[0].get('src')
        # Download the image
        print("Downloading image %s..." % (comic_url))
        res = requests.get(comic_url)
        res.raise_for_status()

    # Save the image to ./xkcd
    image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    # Get the prev button's URL
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prev_link.get('href')

print("Done.")
