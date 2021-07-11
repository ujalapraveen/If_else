age =int(input("enter the age="))
sex=input("enter the sex=")
if sex=="female" and age>=18 and age>=20:
    print("she will work in urban area")
elif sex=="male" and age>=20 and age<=40:
    print("He will work anywhere")
elif sex=="male" and age>=40 and age>=60:
    print("He will work in urban area")
else:
    print("error")
