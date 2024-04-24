import os
while(True):
    print("\n 1. Add Record")
    print("\n 2. Display record")
    print("\n 3. Search record by name")
    print("\n 4. Search Record by roll no.")
    print("\n 5. Delete Record by roll no.")
    print("\n 6. Update student Record")
    print("\n 7. EXIT")
    n=int(input("Enter your choice"))
    os.system('cls')
    if n==7:
        break
    elif n==1:
        print("Enter student info")
        n=input("Enter your name")
        r=input("Enter your roll no.")
        cl=input("Enter your class")
        fees=("Enter your fees")
        per=input("Enter youor percentage")
        f=open(std.txt,"a")
        f.write(n+" "+r" "+cl+" "+fees+" "+per+" ")
        f.close()
    elif n==2:
        print("\n\nList of students\n\n")
        print("Name-Roll no.-class--Fees-Percentage")
        f=open("std.txt","r")
        while(True):
            d=f.readline()
            l=len(d)
            if l==0:
                break
            print(d.strip())
        f.close()
    elif n==3:
        search=input("Enter student name")
        f=open("std.txt","r")
        fl=0
        while(True):
            t=f.readline()
            l=len(t)
            if l==0:
                break
            g=t.split('_')
            if(g[0]==search):
                print("\nRecord Found\n")
                print("\nName is ",g[0])
                print("\nRol no. is ",g[1])
                print("\nClass is ",g[2])
                print("\nFees is ",g[3])
                print("\nPercentage is ",g[4])
                fl=1
                break
            if (fl==0):
                print("Record not found")
            f.close()
            
    elif n==4:
            search=input("Enter student roll no.")
            f=open("std.txt","r")
            fl=0
            while(True):
                t=f.readline()
                l=len(t)
                if l==0:
                    break
                g=t.split("_")
                if g[1]==search:
                 print("\nRecord Found\n")
                print("\nName is ",g[0])
                print("\nRol no. is ",g[1])
                print("\nClass is ",g[2])
                print("\nFees is ",g[3])
                print("\nPercentage is ",g[4])
                fl=1
                break
            if (fl==0):
                print("Record not found")
            f.close()
    elif n==5:
            search=input("Enter student name")
            f=open("std.txt","r")
            tt=open("temp.txt","w")
            fl=0
            while(True):
                t=f.readline()
                l=len(t)
                if l==0:
                    break
                g=t.split("_")
                if g[0]!=search:
                    tt.write(t)
                if g[0]==search:
                    n=1
            f.close()
            tt.close()
            if n==1:
                print("Record deleted successfully")
                os.remove("std.txt")
                os.rename("temp.txt","std.txt")
            if n==0:
                print("Record not found")
    elif n==6:
        n=0
        search=input("Enter student name")
        f=open("std.txt","r")
        tt=open("temp.txt","w")
        fl=0
        while(True):
            t=f.readline()

                
    
            
            
                

            
