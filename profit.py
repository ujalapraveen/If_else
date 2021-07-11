# Write a python program to calculate profit or loss.

cost_price=int(input("enter a cost price "))
selling_price=int(input("enter a seeling price"))

if cost_price>selling_price:
    print("profit")
elif cost_price==selling_price:
    print("no profit no loss")
else:
    print("loss")