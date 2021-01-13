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

** helper fn: one copy of code that builds the dictionary
then 2 uses of dictionary, 
--count: to loop and print all words in abc order
--topcount: pick out words with biggest count, and sort by count
tip: use .items() on dictionary to pull out tuples, custom sort, ... 
"""

import sys

# +++your code here+++
def print_words(filename):
  word_count = {}
  txt_file = open(filename, 'r')
  # entire file saved as a giant txt_string
  txt_string = txt_file.read()
  # split into words
  words = txt_string.split()
  # lowercase words, cannot use on list
  for word in words:
    word = word.lower()
    if not word in word_count: 
      word_count[word] = 1
    else: 
      word_count[word] = word_count[word] + 1
  txt_file.close()
  return word_count

  #   words = line.split()
  #   for word in words: 
  #     word = word.lower()
  # for word in filename:
  #   dict['word'] += 1
  
  # print dict # add space between key/value, then newline
# word1 count1
# word2 count2
# store in lowercase (for sorting), sort by word


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
