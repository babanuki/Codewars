def digital_root(n):
    def digitCalc(num):
        ret=0
        while num>0:
            ret+=num%10
            num//=10
        return ret
    while n>9:
        n=digitCalc(n)
    return n



'''
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


def digital_root(n):
  return n%9 or n and 9


def digital_root(n):
    while n>10:
        n = sum([int(i) for i in str(n)])
    return n
'''
