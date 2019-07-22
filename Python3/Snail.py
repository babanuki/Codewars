def snail(array):
    n=len(array)
    ans=[]
    def snailM(sz, cnt):
        ans.extend(array[cnt][cnt:sz-cnt])
        for i in range(cnt+1, sz-cnt-1):
            ans.append(array[i][sz-cnt-1])
        ans.extend(array[sz-cnt-1][sz-cnt-1:cnt:-1])
        for i in range(sz-cnt-1, cnt, -1):
            ans.append(array[i][cnt])
    for i in range(0, int((n+1)/2)):
        snailM(n, i)
    return ans
    




'''
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
    
    
# my implementation/explanation of the solution by foxxyz
def snail(array):
  if array:
    # force to list because zip returns a list of tuples
    top_row = list(array[0])
    # rotate the array by switching remaining rows & columns with zip
    # the * expands the remaining rows so they can be matched by column
    rotated_array = zip(*array[1:])
    # then reverse rows to make the formerly last column the next top row
    rotated_array = rotated_array[::-1]
    return top_row + snail(rotated_array)
  else:
    return []
    

def snail(array):
    a = []
    while array:
        a.extend(list(array.pop(0)))
        array = zip(*array)
        array.reverse()
    return a
'''
