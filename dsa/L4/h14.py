#     1
#    22
#   333
#  4444
# 55555

n=5

for row in range(1,n+1):
    for s in range(n-row):
        print(' ', end=' ')
    for st in range(row):
        print(row ,end=' ')
    print()