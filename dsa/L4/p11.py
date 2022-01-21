# d
# cd 
# bcd 
# abcd 

n=5

for row in range(1,n+1):
    s=ord('A')+n-row
    for col in range(row):
        print(chr(s),end=' ')
        s+=1
    print()