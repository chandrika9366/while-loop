a=input("enter a")
i=0
sum=0
while i<len(a):
    b=a[i]
    c=(int(b)**3)
    sum=c+sum
    i=i+1
if int(a)==sum:    
     print("it is armstrong num")
else:
    print("not armstrong num")        