num1=int(input("Enter a number 1 : "))
num2=int(input("Enter a number 2 : "))
num3=int(input("Enter a number 3 : "))
if (num1>num2 and num1<num3) or (num1<num2 and num1>num3):
    print("The second largest number is:",num1)
elif (num2>num1 and num2<num3) or (num2<num1 and num2>num3):
    print("The second largest number is:",num2)
else:
    print("The largest number is:",num3)
