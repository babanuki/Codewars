def unique_in_order(iterable):
    l=list(iterable)
    i=0
    while i<len(l)-1:
        if l[i]==l[i+1]:
            del l[i+1]
        else:
            i+=1
    return l