

n=int(input('enter'))
ans=0
i=0
while(n!=0):
    bit=n&1
    ans=(bit*pow(10,i))+ans
    n=n>>1
    i+=1
print(ans)