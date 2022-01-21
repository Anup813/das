# [1,2,3,4,5]
# [2,1,4,3,5]

def sawptwo(arr):
    n=len(arr)
    i=0
    for i in range(n):
        if (i+1<n):
           arr[i],arr[i+1]=arr[i+1],arr[i]
           print(arr[i+1])
        i+=2
        
    return arr

print(sawptwo([1,2,3,4,5]))

    