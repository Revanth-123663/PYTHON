a=int(input("Enter amount in rupees:"))
notes=[500,200,100,50,20,10,5,2,1]
dict={}
for i in notes:
    if(a>=i):
        count=a//i
        dict[i]=count
        a-=count*i
print(dict)


