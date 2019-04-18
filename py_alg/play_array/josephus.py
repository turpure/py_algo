"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.

For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""

def play(a_list, skip):
  a_list = a_list[::]
  skip -= 1
  length = len(a_list)
  index = 0
  while length > 0:
    index = (skip + index) % length
    yield a_list.pop(index)
    length -= 1
  

if  __name__ == "__main__":
    for ele in play(list(range(10)), 4):
      print(ele)
  
