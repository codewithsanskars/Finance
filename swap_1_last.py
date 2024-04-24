n=int(input("Enter the number"))
count=0
while n>0:
    count+=1
print(count)


n=int(input("Enter No."))
list=[]
while n>0:
    r=int(n%10)
    list.append(r)
    n=int(n/10)
l=len(list)
temp=list[0]
list[0]=list[l-1]
list[l-1]=temp
print(list)
for i in list:
    print(list[i-1],end="")
