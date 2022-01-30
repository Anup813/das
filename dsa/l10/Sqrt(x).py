class Solution:
    def mySqrt(self, n: int) -> int:
        s=1
        e=n
        mid=round((s+e)/2)
        ans=0
        while s<=e:
            if mid*mid>n:
                e=mid-1
            elif (mid*mid<n):
                ans=mid
                s=mid+1
            elif (mid*mid==n):
                return mid
            mid=round((s+e)/2)
        return ans