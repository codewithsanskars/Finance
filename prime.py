n=int(input("Enter a number"))
a=0
for i in range(1,n+1):
   if n%i==0:
      a+=1
if a==2:
   print("  Prime number") 
else:
   print("Composite Number")  
    