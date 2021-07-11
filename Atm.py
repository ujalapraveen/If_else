print("Welcome")
print("swipe your card")
amt=int(input("enter amount"))
pin=int(input("enter your pin"))
if pin==1234:
    trans=input("Balance enquiry, withdrawal,deposit,quit")
    if trans =="Balance enquiry":
        print(amt)
    elif trans=="withdrawal":
        a=int(input("enter your amount"))
        amt=amt-a
        print("take your cash")
        print("Remaining Balance=",amt)
    elif trans=="deposit":
        b=int(input("enter your amount"))
        amt=amt+b
        print("your total amount=",amt)
    elif trans=="quit":
        print("exit")
else:
    print("pin is wrong")
print("Thankyou for banking with us")




