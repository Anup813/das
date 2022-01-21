#      1
#     121
#    12321
#   1234321
#  123454321




n=5

for row in range(1,n+1):
    for p1 in range(n-row):
        print(' ',end=' ')
    for p2 in range(1,row+1):
        print(p2,end=' ')
    for p3 in range(row-1,0,-1):
        print(p3,end=' ')
    print()