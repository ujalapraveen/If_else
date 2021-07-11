first=int(input("enter the first age ="))
second=int(input("enter the second age ="))
third=int(input("enter the third age ="))
if first>=second and first>=third:
    print("oldest is first")
elif second>=first and second>=third:
     print("oldest is second")
elif third>=first and third>=second:
    print("oldest is third")
else:
    print("we are equall")