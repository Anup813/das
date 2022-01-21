# *****
#  ****
#   ***
#    **
#     *


n=5

for row in range(n+1):
    for s in range(row):
        print(' ',end=' ')
    for st in range(n-row+1):
        print('*',end=' ')
    print()