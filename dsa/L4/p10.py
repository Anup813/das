# from calendar import c
# from tkinter import E


# A
# B c
# C D E
# D E F G

n=5

for row in range(1,n+1):
    for col in range(row):
        print(chr(ord('A')+row+col-1),end=' ')
    print()