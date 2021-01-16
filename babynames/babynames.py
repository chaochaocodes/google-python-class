#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract all the text from the file and print it
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list


 Part B. from video lecture:
 When babynames.py --summaryfile baby*.html is run, takes all baby files as argv
 -If '--summaryfile' is given, read each file and create a copy ending in .summary
 -Take output and write to new .summary file
 Gives you the option to take returned list/dict/etc. and choose to print to std ouput or print to file

 With these files, in terminal, run: grep 'Trinity ' *.summary will return every year Trinity was on the list!
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  # save result list [year, 'name rank', 'name rank', ...]
  names = []

  # 1. Extract entire file 
  f = open(filename, 'rU')
  text = f.read()

  # 2. Extract the year ('Popularity in 1990'), add to result list
  extract_year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
  year = extract_year.group()
  names.append(year)

  # 3. Extract the names and rank numbers as tuple (rank, boy, girl)
  name_tuple = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

  # 4. Turn tuple data into a dict, names == key, rank == value
  name_dict = {}
  for rank, boy_name, girl_name in name_tuple:
    if boy_name not in name_dict:
      name_dict[boy_name] = rank
    if girl_name not in name_dict:
      name_dict[girl_name] = rank

  # ** dict prints k,v in random order! sort by abc
  sorted_names = sorted(name_dict.keys())
  print sorted_names

  # 5. Build the [year, 'name rank', ... ] list
  for name in sorted_names:
    names.append(name + " " + name_dict[name])

  return names 


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # 6. Fix main() to use the extract_names list
  for filename in args:
    names = extract_names(filename)

    # f = open(filename, 'w') => write to file f.write(text)
    # run solution usage: babynames.py baby1990.html | more
    # print name + ranking on a new line
    text = '\n'.join(names)

    if summary:
      sumf = open(filename + '.summary', 'w')
      sumf.write(text + '\n')
      sumf.close()
    else:
      print text

  
if __name__ == '__main__':
  main()
