# 1
# 23
# 345
# 4567

row=5

for i in range(1,row+1):
    for j in range(i):
        print(i,end=' ')
        i-=1
    print()
