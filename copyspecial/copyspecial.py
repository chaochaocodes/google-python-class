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
def get_special_paths(dir):
  result = []
  filenames = os.listdir(dir)
  # print filenames ## ['zz__something__.jpg', 'copyspecial.py', ...]
  for filename in filenames:
    # print os.path.join(dir, filename)  ## ./zz__something__.jpg (joins dir+filename in pathform valid path form)
    # print os.path.abspath(path) ## complete path

    # extra filenames with the pattern __w__
    special_file = re.search(r'__(\w+)__', filename)
    if special_file:
      result.append(os.path.abspath(filename))

  for path in result:
    print path

# Part B. File copying
# given a list of paths, copies those files into the given directory
def copy_to(paths, dir):
  
  return

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
  for dir in args:
    paths = get_special_paths(dir)


  
if __name__ == "__main__":
  main()
