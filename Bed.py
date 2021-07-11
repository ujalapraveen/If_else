girls=int(input("enter the girls ="))
bed=int(input("enter the bed ="))
if girls==bed:
    print("bed girls is equal")
elif girls>bed:
    print("bed is less",girls-bed)

else:
    print("girls is more",bed-girls)



file=open("Q3.txt","a")
file.write("navgurukul is the best place for learning")
file.write('\n')
file.close()
file=open("Q3.txt","r")
print(file.read)
file.close()