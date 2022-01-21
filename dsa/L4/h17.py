# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1


n=5

for row in range(n):
    for P1p1 in range(1,n-row+1):
        print(P1p1,end=' ')
    for P1p2 in range(row):
        print('*',end=' ')
    for P2p1 in range(1,row+1):
        print('*',end=' ')
    for P2p2 in range(n-row,0,-1):
        print(P2p2,end=' ')
    print()