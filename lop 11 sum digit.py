a=int(input("enter num"))
sum=0
while a>0:
    d=a%10
    sum=sum+d
    a=a//10
print(sum)    