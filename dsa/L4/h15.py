# 12345
#  2345
#   345
#    45
#     5




n=5

for row in range(1,n+1):
    for s in range(row):
        print(' ',end=' ')
    for st in range(row,n+1):
        print(st,end=' ')
    print()