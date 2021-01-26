#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself. (hostname: code.google.com)
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here++
  # Extract hostname from filename
  hostname = re.search(r'_(\w[^_]+)', filename)
  host = hostname.group(1)
  # 1. Process entire log file
  f_urls = []
  f = open(filename)
  # print f.read()
  # 2. Find all puzzle image url slices, add hostname
  for line in f:
    url_match = re.search(r'"GET ([^ ]+)', line)
    path = url_match.group(1)
    if 'puzzle' in path:
      f_urls.append('http://' + host + path)

  # 3. Remove duplicates
  urls = []
  for i in f_urls:
    if i not in urls:
      urls.append(i)
  
  # 4. Return urls, sorted
  return sorted(urls)
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

  # Create index.html:   
  # <html><body> <img src="img0"><img src="img1">... </body></html>
  index = file(os.path.join(dest_dir, 'index.html'), 'w')
  index.write('<html><body>\n')

  # Download each image into directory, as img0, img1 ...
  i = 0
  for img_url in img_urls:
    filename = 'img%d' % i
    print "Retrieving...", img_url
    urllib.urlretrieve(img_url, os.path.join(dest_dir, filename))

    index.write('<img src="%s">' % (filename,))
    i += 1

  index.write('\n</body></html>\n')
  index.close()


def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
