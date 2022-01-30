def pivotelement(arr):
    s=0
    e=len(arr)-1
    mid=round((s+e)/2)

    while (s<=e):
        if arr[mid]>=arr[0]:
            s=mid+1
        else:
            e=mid
        mid=round((s+e)/2)
    
    return s

print(pivotelement([3,8,10,17,1]))

