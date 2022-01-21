# a
# bb
# ccc

n=5

for row in range(1,n+1):
    for col in range(row):
        print(chr(ord('A')+row-1),end=' ')
    print()