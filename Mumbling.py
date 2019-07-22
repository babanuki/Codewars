def accum(s):
    i=0
    ans=[]
    while i<len(s):
        tmpS=""
        tmpS+=s[i].upper()
        for j in range(0, i):
            tmpS+=s[i].lower()
        ans.append(tmpS)
        i+=1
    return "-".join(ans)
    
    
'''
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''
