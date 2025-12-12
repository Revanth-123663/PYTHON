r=10
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end='')
    temp=2*r-1-2*i
    for k in range(temp):
        print("*",end='')
    print()
