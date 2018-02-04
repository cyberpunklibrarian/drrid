import feedparser
import pprint
import shutil
import requests
import os

directory = "./images/"

# Based upon code from Timothy Bramlett
# http://timothybramlett.com/recieving_notifications_of_rss_feeds_matching_keywords_with_Python.html

# Get the urls we've already seen
f = open('viewed_urls.txt', 'r')
urls = f.readlines()
urls = [url.rstrip() for url in urls] # remove the '\n' char
f.close()

def url_is_new(urlstr):
    # Returns true if the url string does *not* exist in the list of strings extracted from the text file
    if urlstr in urls:
        return False
    else:
        return True

# feeds.txt can contain one or more RSS feeds
filepath = 'feeds.txt'
with open(filepath) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        rss = line.strip()
        feed = feedparser.parse(rss)

        for key in feed["entries"]:
            url = key['links'][0]['href']
            title = key['title']
            content = key['content']
            # get the summary from the entry
            summary = key['summary']
            # search the summary for the image link
            img = summary[summary.find("<span>")-1:summary.find("\">[link]")]
            # pare down the result of img to only a url
            imgURL = (img[16:])
            # split the url to acquire the image file name
            imgFile = imgURL.split("/")[-1]
            saveFile = directory + imgFile

            # Here are a bunch of if statements to deal with various links.

            if "imgur.com" in imgURL and imgURL.endswith(".gifv"):
                imgURL = "https://i.imgur.com/" + imgFile[:-5] + ".gif"
            elif "imgur.com" in imgURL:
                imgURL = "https://i.imgur.com/" + imgFile + ".jpg"

            if "i.redd.it" in imgURL:
                imgURL = "https://i.redd.it/" + imgFile

            if "cdnb.artstation.com" in imgURL:
                imgURL = imgURL[:-4]

            if "gfycat.com" in imgURL:
                imgURL = "https://giant.gfycat.com/" + imgFile + ".webm"

            # Debugging statement - can be commented out.
            # print(imgURL)

            if url_is_new(url):
                # Uncomment the line below to print info to screen.
                print('{} - {}'.format(title, imgFile))
                # request the image for download and save it
                r = requests.get(imgURL, timeout=5)
                if r.status_code == 200:
                    with open(saveFile, 'wb') as i:
                        # Deal with gfycat .webm files.
                        if "gfycat" in imgURL:
                            i.write(r.content)
                            os.rename(saveFile, saveFile + ".webm")
                        # And if it's not gfycat then...
                        i.write(r.content)
                msgtitle = title
                msg = '{}\n{}'.format(title, url)

                with open('viewed_urls.txt', 'a') as v:
                    v.write('{}\n'.format(url))

        line = fp.readline()
        cnt += 1


# Files downloaded - rename those that came down without an extension.
dirname = './images/'
for f in os.listdir(dirname):
    # Add extensions that should _not_ be renamed.
    ext = [".jpg", ".png", ".gif", ".gifv", ".py", ".txt", ".xml", ".webm", ".DS_Store"]
    path = os.path.join(dirname, f)
    if not os.path.isfile(path):
        continue  # Don't rename directories
    if not f.endswith(tuple(ext)):
        os.rename(path, path + '.jpg')
    if f.endswith(".gifv"):
        os.rename(path, path[:-5] + '.gif')
