def longest(s1, s2):
    l=[]
    for i in s1+s2:
        if i not in l:
            l.append(i)
    return ''.join(sorted(l))



'''
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))
'''
