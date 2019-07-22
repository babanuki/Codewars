def unique_in_order(iterable):
    l=list(iterable)
    i=0
    while i<len(l)-1:
        if l[i]==l[i+1]:
            del l[i+1]
        else:
            i+=1
    return l



'''
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]




unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]





def unique_in_order(iterable):
  r = []
  for x in iterable:
    x in r[-1:] or r.append(x)
  return r
  '''
