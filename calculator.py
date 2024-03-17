num1=input("enter a number")
operator=input("enter a operator")
num2=input("enter a number")

num1=int(num1)
num2=int(num2)

if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)

else :
    print("sorry")    


