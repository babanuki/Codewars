def find_short(s):
    l=2147483647
    tmpl=s.split()
    for i in tmpl:
        if l>len(i):
            l=len(i)
    return l # l: shortest word length
    
    
'''
def find_short(s):
    return min(len(x) for x in s.split())
    
    
    
def find_short(s):
    return len(min(s.split(' '), key=len))
'''
