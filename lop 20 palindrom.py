a=int(input("enter palindrome"))
k=a
i=0
n=0
len=len(str(a))
while i<len:
      r=a%10
      n=n*10+r 
      a=a//10
      i=i+1
if k==n:
    print("palindrome number")
else:
    print("not palindrome")       