def find_even_index(arr):
    left, right, total=0, 0, 0
    for i in arr:
        total+=i
    right=total
    if left==right-arr[0]:
        return 0
    right-=arr[0]
    for i in range(1, len(arr)):
        left+=arr[i-1]
        right-=arr[i]
        if left==right:
            return i
    return -1


'''
def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
'''
