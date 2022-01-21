row=int(input('enter'))

for i in range(1,row+1):
    for j in range(1,row+1):
        print(chr(ord('A')+i-1),end=' ')
    print()