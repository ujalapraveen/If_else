# Write a program to check whether the trianlge is equilateral isosceles or scalene triangle.


side1=int(input("enter the  side1 ="))
side2=int(input("enter the side2 ="))
side3=int(input("enter the  side 3="))

if side1==side2==side3==3:
    print("IIt is equilateral triangle")

elif side1==side2 !=side3 or side2==side3 !=side1 or side3==side1!=side2:
    print("isosceles triangle")

else:
    print("scalene triangle")
