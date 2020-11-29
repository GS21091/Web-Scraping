# download comics

import requests, os, bs4, re

# starting URL
url = "https://365manga.com/manga/slave-b/chapter-49/"

os.makedirs("slave-b", exist_ok=True)

print("Downlaoding page %s..." %url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "lxml")

for img in soup.select("div.page-break img[src]"):
    comic_url = img['src']

    res = requests.get(comic_url)
    res.raise_for_status()

    # saving the image
    image_file = open(os.path.join('slave-b', os.path.basename(comic_url)), 'wb')

    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

print("Done.")

