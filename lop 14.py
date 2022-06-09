a=input("enter num")
k=list(a)
l=len(k)
p=1
c={0:"zero",1:"one",2:"two",3:"tree",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
while p<l:
   print(c[int(k[p])],end="")  
   p=p+1 