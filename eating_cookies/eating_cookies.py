#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution
def eating_cookies(n, cache=None):
    # Cookie Monster can eat either 0, 1, 2, or 3 cookies at a time. If he were given a jar
    # of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies
    # in the cookie jar? Implement a function `eating_cookies` that counts the number of
    # possible ways Cookie Monster can eat all of the cookies in the jar.

    # establish base cases: 0, 1, 2, 3
    # adding "or type(cache) == list" bc it will overwrite the array
    # cache and replace it with a dictionary cache
    # all caching is in key, value pairs
    if cache is None or type(cache) == list:
          cache = {0: 1, 1: 1, 2: 2}
    # make a cache available to the recursive function through multiple recursive calls
    if n < 0:
          return 0
    elif n not in cache:
          cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')