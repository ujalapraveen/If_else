num1=int(input("enter a 1st no ="))
num2=int(input("enter a 2nd n ="))
num3=int(input("enter a 3rd no ="))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,"is a second minimum ")
    else:
        print(num3,"is a second minimum")
elif num2>num1 and num2>num3:
    if num1 >num3:
        print(num1,"is a second minimum")
    else:
        print(num3,"is a second minimum")
elif num3>num1 and num3>num2:
    if num2>num1:
        print(num2,"is a second minimum ")
    else:
        print(num1,"is a second minimum")
else:
    pass