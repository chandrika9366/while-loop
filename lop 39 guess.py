a=int(input("enter a"))
i=1
while i<=9:
    b=int(input("enter b"))
    if b==a:
        print("you gues right")
        break
    i=i+1
else:
    print("you guest wrong")  