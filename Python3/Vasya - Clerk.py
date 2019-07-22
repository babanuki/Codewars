def tickets(people):
    d={
        25:0,
        50:0,
    }
    for i in people:
        if i==25:
            d[25]+=1
        elif i==50:
            if d[25]>0:
                d[50]+=1
                d[25]-=1
            else:
                return 'NO'
        else:
            if d[25]>0 and d[50]>0:
                d[25]-=1
                d[50]-=1
            elif d[25]>2:
                d[25]-=3
            else:
                return 'NO'
    return 'YES'
