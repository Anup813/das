
def bitwiseComplement( n: int):
    if n==0:
        return 1
    m=n
    mask=0
    while (m!=0):
        mask=(mask<<1) | 1
        m=m>>1
    ans=(~n)&mask
    return ans

print(bitwiseComplement(5))