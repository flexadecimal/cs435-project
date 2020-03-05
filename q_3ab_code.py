from random import random

def getRandomArray(n):
  out = set()
  while len(out) < n:
    out.add(random())
  return out
  
def getSortedArray(n):
  return list(reversed(range(1, n + 1)))
  
# for testing
if __name__ == "__main__":
  n = 10
  print("getRandomArray({}): {}".format(n, getRandomArray(n)))
  print("getSortedArray({}): {}".format(n, getSortedArray(n)))