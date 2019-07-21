def is_triangle(a, b, c):
    l=[a,b,c,]
    l.sort()
    if l[0]<=0:
        return False
    if l[2]>=l[0]+l[1]:
        return False
    else:
        return True
