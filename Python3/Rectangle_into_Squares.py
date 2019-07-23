def sqInRect(lng, wdth):
    l=[]
    if lng==wdth:
        return None
    def InnerFunc(x, y):
        if not (x and y):
            return 1
        if x>y:
            x, y=y, x
        y-=x
        l.append(x)
        InnerFunc(x, y)
    InnerFunc(lng, wdth)
    return l



'''
# Recursive solution
def sqInRect(lng, wdth, recur = 0):
    if lng == wdth:
        return (None, [lng])[recur]            # If this is original function call, return None for equal sides (per kata requirement);
                                               # if this is recursion call, we reached the smallest square, so get out of recursion.
    lesser = min(lng, wdth)
    return [lesser] + sqInRect(lesser, abs(lng - wdth), recur = 1)

'''
