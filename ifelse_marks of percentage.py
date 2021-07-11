


# Write a python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F

sub1=int(input("enter of a marks first physics="))
sub2=int(input("enter of the marks second Biology="))
sub3=int(input("enter of the marks third Matheamtics= "))
sub4=int(input("enter of the marks fourth Computer="))
sub5=int(input("enter of the marks fifth chemistry="))
total=sub1+sub2+sub3+sub4+sub5
percentage=total/500*100
print("totala marks",total)
print("marks percentage",percentage)
if percentage>=90:
    print("Grade :A")
elif percentage>=80:
    print("Grade:B")
elif percentage>=70:
    print("Grade :c")
elif percentage>=60 :
    print("Grdae:D")
elif percentage>=40:
    print("Grade:E")
else:
    print("Grade:F")







