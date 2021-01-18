#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

# Part A. Manipulating file paths
# returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dirname):
  result = []
  filenames = os.listdir(dirname)
  # print filenames ## ['zz__something__.jpg', 'copyspecial.py', ...]
  for filename in filenames:
    # path = os.path.join(dirname, filename)  ## joins dir + fname in platform-valid way)  
    # print path    ## ./zz__something__.jpg 
    # print os.path.abspath(path) ## complete path

    # extract filenames with the pattern __w__
    match = re.search(r'__(\w+)__', filename)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, filename)))
  return result

# Part B. File copying
# given a list of paths, copies those files into the given directory
# copies special files into given dir, create that dir if doesn't exist
def copy_to(paths, todir):
  if not os.path.exists(todir):
    os.mkdir(todir)
  for path in paths:
    filename = os.path.basename(path)
    shutil.copy(path, os.path.join(todir, filename))


# Part C. Calling an external program
# given a list of paths, zip those files up into the given zipfile
# def zip_to(paths, zippath):

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  paths = []
  for dirname in args:
    paths.extend(get_special_paths(dirname))
  
  if todir: 
    copy_to(paths, todir)
  else: 
    print '\n'.join(paths)
  

if __name__ == "__main__":
  main()
