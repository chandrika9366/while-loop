a=int(input("enter num"))
product=1
while a>0:
    d=a%10
    product=product*d
    a=a//10                                                                               
print(product)    