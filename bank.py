import os
import sys
while(1):
 print("Welcome to Lootera Bank")
 t=int(input("Press '1' to open an account  "))
 if(t==1):
   name=input("Enter your name      ")
   age=input("Enter your age       ")
   ad=input("Enter your Adhaar Number        ")
   pasw=input("Create Password         ")
   os.system('clear')
   rs=int(input("Enter the amount you want to deposit in your account          "))
   os.system('clear')
   i=int(input("Congratulations!, Your account has been created Press '0' to login "))
  if(i==0):
   n1=input("Enter your name")
   p1=input("Enter passwrord")
   os.system('clear')
   if(n1==name and p1==pasw):
            	print("Press '1' to diplay your account balance")
            	print("Press '2' to deposit money")
            	print("Press '3' to withdraw money")  
            	f=int(input())
            	os.system('clear')
            	if(f==1):
                	print("Your current account balance is",rs )
            	if(f==2):
                	r1=int(input("Enter the amount you want to deposit"))
                	rs+=r1
                	os.system('clear')
                	print("Your account balance has been successfully updated to ",rs)
               
            	if(f==3):
                	r1=int(input("Enter the amount you want to withdraw"))
                	rs-=r1
                	os.system('clear')
                	print("Your account balance has been successfully updated to ",rs)
        	else:
                	print("Login Error Please try again")
    	else:
        	sys.exit()      