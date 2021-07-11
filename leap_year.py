# Write a python program to check whether a year is leap year or not.

year=int(input("enter a year"))
if year%400==0and year%100!=0:
    print("it is aleap year")
elif year%400==0:
    print("it is a leap year")
else:
    print("it is not a leap year")




