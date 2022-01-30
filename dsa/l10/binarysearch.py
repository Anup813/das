
def binsearch(arr,k):
    s=0
    e=len(arr)-1
    mid=round((s+e)/2)
    while (s<=e):
        if k==arr[mid]:
            return mid
        elif k>arr[mid]:
            s=mid+1
        else:
            e=mid-1
        mid=round((s+e)/2)  
    return -1

print(binsearch([3,6,8,12,34,44],4))