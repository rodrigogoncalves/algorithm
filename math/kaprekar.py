#!/usr/bin/env python3

def kap(n):
  """
  Execute and return result of a Kaprekar's routine step for number n.

  >>> kap(6174)
  6174
  >>> kap(2341)
  3087
  >>> kap(3087)
  8352
  >>> kap(8352)
  6174
  """
  n = format(n, '04d')
  small = int(''.join(sorted(n)))
  big = int(''.join(sorted(n, reverse=True)))
  return big - small

def kap_routine(n):
  """
  Execute Kaprekar's routine starting from number n and print all recursion steps to the output.

  >>> kap_routine(6174)
  6174 🥳
  >>> kap_routine(2341)
  2341 --> 3087 --> 8352 --> 6174 🥳
  >>> kap_routine(9876)
  9876 --> 3087 --> 8352 --> 6174 🥳
  """
  if n == 6174:
    print(f'{n} ' + u'\U0001f973')
  else:
    print(f'{n} --> ', end='')
    kap_routine(kap(n))

if __name__ == "__main__":
  import doctest, sys

  doctest.testmod()

  if len(sys.argv) > 1:
    n = int(sys.argv[1])
    kap_routine(n)
