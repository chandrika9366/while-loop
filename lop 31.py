a=int(input("enter a"))
i=1
b=1
sum=0
while i<=a:
    b=i*b
    sum=sum+b
    i=i+1
    print(sum,end=",")