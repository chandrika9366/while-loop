#write a program to find the sum of following series:s=1+4-9+16-25+36....n terms?
a=int(input("enter num"))
i=2
b=1
print(b,end="")
while i<=a:
    if i%2==0:
        b=i**2
        print("+",b,end="")
    else:
        print("-",i**2,end="")
    i=i+1        