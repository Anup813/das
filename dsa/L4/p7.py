# from abc import ABC


# ABC
# ABC
# ABC

n=int(input('enter'))

for row in range(1,n+1):
    for col in range(1,n+1):
        print(chr(ord('A')+col-1),end=' ')
    print()