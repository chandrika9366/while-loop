num=input("enter num")
b=len(num)
c=0-len(num)
sum=""
i=-1
while c<=i:
    a=int(num[i])
    sum=sum+a
    i=i-1
print(sum)
if num==sum:
    print("it is palindrome") 
else:
    print("it is not palindrome")       