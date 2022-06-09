a=int(input("enter a"))
i=1
while i<=5:
    b=int(input("enter num"))
    if a<b:
        print("you are smaller")
    elif b>a:
        print("you are greather")
    elif a==b:
        print("wow")
        break
    else:
        print("wrong")
    i=i+1   