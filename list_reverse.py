list=[]
temp=0
n=int(input("Enter the length of list"))
for i in range(0,n):
    k=int(input("Enter the values"))
    list.append(k)
print(list)
p=n
print(list[0])
for l in range(0,int(n/2)):
    temp=list[l]
    list[l]=list[p-l-1]
    list[p-l-1]=temp
print(list)