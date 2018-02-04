# DR. RID
## The Dirty Rotten Reddit Image Downloader

### Description

This is a simple Python 3 script written to scratch my own itch. As an image junky, I save a bunch of images to my saved posts on Reddit. Downloading them later takes way too much time so I decided to write a Python script to help move things along and that's where this thing came from.

This has been written on and for macOS, but it's Python. It should work other places too.

If we're honest with each other, this is a pile of if statements because, while RSS is an awesome bit of technology, it's also a freaking mess because it has to pull data from everywhere. Currently this seems to work pretty well with images downloaded from Imgur (both static and animated), i.redd.it, ArtStation, and Gfycat (webm files). There's probably a more elegant "Pythonesque" way to do this, but frankly, I don't care. This is working for me, so far, and I'll make changes to make it work better and share it up here.

### Usage

There are three main files and one directory. The files:

* **drrid.py** - The Python script what makes the magic happen.
* **feeds.txt** - Put your list of RSS feed links in here; one per line. (I've included examples.) Me, I just put my saved posts RSS feed in there, but you do you.
* **viewed_urls.txt** - This file contains lists of URLs you've already sent through DR. RID. It works as a log and as a way to keep the good Doctor from downloading the same stuff over and over again.

The directory, images, is where the images end up. Seemed like a good place for them.

Watch for updates as I find things that don't work, get pissed off, and write even more bad code to deal with it.

---

"Python is where it's at!" ~A stupid ad on YouTube
