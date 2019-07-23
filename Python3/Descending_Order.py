def Descending_Order(num):
    l=list(str(num))
    l.sort(reverse=True)
    return int(''.join(l))



'''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
'''
