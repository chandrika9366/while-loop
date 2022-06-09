i=1
a=int(input("enter number"))
while i<=a:
    b=int(input("enter number"))
    if b<a:
        print("number enter by you smallar")
    elif b>a:
        print("number enter by you greather")
    elif b==0:
        print("wow")
        break
    else:
        print("wrong") 