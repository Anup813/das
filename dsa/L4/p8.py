# from distutils.bcppcompiler import BCPPCompiler


# A B C
# B C D
# C D E

n=int(input('enter'))

for row in range(1,n+1):

    for col in range(1,n+1):
        print(chr(ord('A')+col+row-2) ,end=' ')
 
    print()

        