#!/usr/bin/env python

import string
import sys

"""Brute Force Password Cracker"""

def main():
  """Main"""
  password = raw_input("Enter a test password: ")
  brute_force(password)

def brute_force(password):
  """Brute forces password"""
  min_pass_length = 0
  max_pass_length = 2
  nothing = ''

  ascii_list = list(string.printable)
  print ascii_list
  #ascii_list = ['a', 'b', 'c', '1', '2', '3']
  for item in ascii_list:
    print item

  options = deep_iterate_options(ascii_list, max_pass_length)
  print options
  return


def deep_iterate_options(char_list, length):
  """Iterates through all character options"""
  options = ['']
  if length < 1:
    return options
  old_options = deep_iterate_options(char_list, length-1)
  for char in char_list:
    for option in old_options:
      print char + option
      options.append(char + option)
  return options

def password_equality(password_attempt, password):
  """Password equality comparator"""
  return password_attempt == password

if __name__ == "__main__":
  main()