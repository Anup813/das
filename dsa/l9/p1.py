def sumarr(arr):
    sum=0

    for i in range(len(arr)):
        sum+=arr[i]
    
    return sum

print(sumarr([1,2,3,9,9,9,9,9]))