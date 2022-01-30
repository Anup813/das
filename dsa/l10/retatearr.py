def retatearr(arr:list,k):
    if len(arr)==1:
        return arr
    # arr[:k],arr[k+1:]=arr[k+1:],arr[:k]
    n=len(arr)-1
    for i in range(k):
        arr.insert(arr[i],arr[n])
    return arr

print(retatearr([1,2,3,4,5,6,7],3))