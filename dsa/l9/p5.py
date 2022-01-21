# [2,2,2,3,3,3,4]
# 4

def finduqine(arr):
    ans=0

    for i in range(len(arr)):
        ans=ans^arr[i]
        print(ans)
    return ans

print(finduqine([2,3,4,4,2]))
