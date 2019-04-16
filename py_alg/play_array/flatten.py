"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""

def flatten(lst):
  ret = []
  for ele in lst:
    if type(ele) == type([]):
      ret.extend(flatten(ele))
    else:
      ret.append(ele)
  return ret

if __name__ == '__main__':
  alist = [1,2,[3,4],[7,[9,10]]]
  print(flatten(alist))