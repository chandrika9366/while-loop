#28.write a program to find the sum of the following series(accept values of x and n from user)1+x/1!+x2/2!+....xn/n!x+x2/2+...xn/n?
a=int(input("enter num"))
i=0
sum=1
b=1
while i<=a:
    sum=sum+i
    i=i+1
    print(b,"+","x","/",i,"!","+",end="")
    b=b+1
    
print(sum)