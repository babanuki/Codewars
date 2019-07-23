def square_digits(num):
    l=list(str(num))
    s=''
    for i in l:
        s+=str(int(i)**2)
    return int(s)




'''
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
'''
