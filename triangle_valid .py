# Write a python program to input angles of a triangle and check whether triangle is valid or not.




first_angle=int(input("enter a first_angle ="))
second_angle=int(input("enter a second_angle ="))
third_angle=int(input("enter a third_angle ="))

sum=first_angle+second_angle+third_angle

if sum==180:
    print("it is valid ")

else:
    print("not valid")