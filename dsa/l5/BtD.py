

n=int(input('enter'))

ans=0
i=0

while(n!=0):
    digit=n%10
    # print(digit)
    if (digit==1):
        ans=ans+pow(2,i)
    n=n/10
    i+=1
print(ans)