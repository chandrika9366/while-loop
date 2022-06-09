sum=0
i=1
a=int(input("enter a"))
while i<a:
      b=int(input("enter equel"))
      sum=sum+b
      print(sum)
      i=i+1
total_sum=sum
ararage=total_sum//a
print(ararage) 
if ararage%5==0:
    print("multiple of 5")
else:
    print("not multiple of 5")         