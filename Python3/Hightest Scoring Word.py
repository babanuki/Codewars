from string import printable

def high(x):
    l=x.split()
    dicl=[i for i in printable[10:36]]
    maxpt=0
    ans=""
    for i in l:
        point=0
        for j in i:
            point+=dicl.index(j)+1
        if maxpt<point:
            maxpt=point
            ans=i
    return ans
    
    
    
    '''
    def high(x):
      return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
    
    
    def high(x):
      words=x.split(' ')
      list = []
      for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        list.append(scores)
      return words[list.index(max(list))]
    '''
