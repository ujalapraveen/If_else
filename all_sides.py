# Write a python program to input all sides of a triangle and check whether the triangle is valid or not.




side1=int(input("enter the sides of triangle ="))
side2=int(input("enter the side of triangle ="))
side3=int(input("enter the side of triangle ="))
if side1==side2==side3:
    print("valid triangle")
else:
    print("not valid triangle")