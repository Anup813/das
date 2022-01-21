row=int(input('enter'))
count=1
for i in range(row):
    for j in range(i):
        print(count,end=' ')
        count+=1
    print()