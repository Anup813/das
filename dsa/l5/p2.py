
class Solution:
    def reverse(self, x: int) -> int:
        num=abs(x)
        sum=0
        main=0
        while (0<num):
            r=num%10
            
            sum=(sum*10)+r
            num=num//10
        
        
        if (x<0):
            main=-sum
        else:
            main=sum
            
        if (main > (2 ** 31 - 1) or main < (-1 * (2 ** 31))):
            return 0
        else:
      
            return main