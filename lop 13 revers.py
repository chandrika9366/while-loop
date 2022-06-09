a=int(input("enter a"))
r=0
while a>0:
    b=a%10
    r=r*10+b
    a=a//10
    print(r)