a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
a1=[int (i) for i in str(a)]
b1=[int (i) for i in str(b)]
c1=[int (i) for i in str(c)]
x=max(a1)+max(b1)+max(c1)
y=min(a1)+min(b1)+min(c1)
print(x+y) 
