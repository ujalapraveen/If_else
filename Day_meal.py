day=input("enter the day =")
meal=input("enter the meal ")
if day=="monday":
    if meal=="breakfast":
        print("poha")
    else:
        print("nothing")
elif day=="tuesday":
    if meal=="lunch":
        print("roti sabji")
    else:
        print("nothing")
elif day=="Wednesday":
    if meal=="dinner":
        print("palak paneer")
    else:
        print("nothing")
elif day=="thrusday":
    if meal=="breakfast":
        print("maggie")
    else:
        print("nothing")
elif day=="friday":
    if meal=="evening":
        print("rice and dal")
    else:
        print("nothing")
elif day=="saturday":
    if  meal=="dinner":
        print("noodles")
    else:
        print("nothing")
else:
    print("food")