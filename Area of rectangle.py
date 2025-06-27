class rec:
    def set_dim(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
l=[]
ch=int(input("Enter the number of rectangles:"))
for i in range(ch):
    r=rec()
    length=int(input("Enter the length:"))
    breadth=int(input("Enter the breadth:"))
    r.set_dim(length,breadth)
    l.append(r)
    
pos=0
for i in l:
    print("Area of rectangle is {}".format(pos))
    print("Area is",i.area())
    pos=pos+1
