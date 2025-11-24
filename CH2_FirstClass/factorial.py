import functools
from multiprocessing.spawn import _main

def factorial(n):
  return functools.reduce(lambda p, n: p * n, range(1, n+1))

def main():
  print(factorial(5))

main()