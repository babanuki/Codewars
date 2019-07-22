def move_zeros(array):
    i=0
    cnt=0
    while i<len(array):
        if array[i]==0 and array[i] is not False:
            del array[i]
            cnt+=1
        else:
            i+=1
    while cnt>0:
        array.append(0)
        cnt-=1
    return array
    
    
    
    '''
    def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
    
    
    def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    '''
