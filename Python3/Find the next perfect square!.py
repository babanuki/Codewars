import math

def find_next_square(sq):
    tmp=math.sqrt(sq)
    if tmp%1==0:
        return (tmp+1)**2
    else:
        return -1
