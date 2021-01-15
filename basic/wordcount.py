#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top(). 
"""

import sys

# +++your code here+++
# define helper fn to build word/count dict for DRY code
def wordcount_dict(filename):
  word_count = {}
  txt_file = open(filename, 'r')
  # entire file saved as a giant txt_string
  txt_string = txt_file.read()
  # split string into a list of words
  words = txt_string.split()
  # store in lowercase for sorting
  for word in words:
    word = word.lower()
    if not word in word_count: 
      word_count[word] = 1
    else: 
      word_count[word] = word_count[word] + 1
  txt_file.close()
  return word_count

# sort dictionary by word
def print_words(filename):
  word_count = wordcount_dict(filename)
  sorted_words = sorted(word_count.keys())
  for word in sorted_words:
    print word, word_count[word]

# define custom function to sort tuple by value
def get_count(tuple):
  return tuple[1]

# sort dictionary by count and print top 20 (reverse sort)
def print_top(filename):
  word_count = wordcount_dict(filename)
  # .items() turns dictionary into a list of (key, value) tuples
  sort_tuples = sorted(word_count.items(), key=get_count, reverse=True)
  # Print first 20 via list slicing
  sort_tuples = sort_tuples[:20]
  for k,v, in sort_tuples: print k, v 


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.

def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
