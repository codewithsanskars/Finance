import os
set={""}
n=int(input("Enter no. of tasks you want to insert  "))
for i in range(0,n):
    ch=str(input("Enter task  "))
    os.system('cls')
    set.add(ch)
print(set) 
a=int(input("Press 1 to add a task and 0 to remove a task  "))
if a==1:
    ch=str(input("Enter task to be added  "))
    os.system('cls')
    set.add(ch)
    print(set)
elif a==0:
    ch=str(input("Enter task to be removed  "))
    os.system('cls')
    set.remove(ch)
    print(set)
else:
  print("Invalid entry")