n=5

for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()

for k in range(n+1,1,-1):
    for i in range(1,k):
        print("*",end=' ')

    print()