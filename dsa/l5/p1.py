a=123
sum=0
p=1
while (0<a):
    sum+=a%10
    p*=a%10
    a=a//10
print(p+sum)
    
