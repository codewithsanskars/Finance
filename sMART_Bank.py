import mysql.connector
mydb=mysql.connector.connect

def reg():
    name=input("Enter your name(as per adhaar)")
    age=int(input("Enter your age"))
    mob=int(input("Enter your mobile number"))
    adhar=int(input("Enter your Adhar Number"))
    pan=input("Enter your PAN number")
    paisa=int(input("Enter the money you want to deposit( Minimum Rs 100)"))
    if paisa<100:
        print("Please enter amount greater or equal than than 100")
        paisa=0
    else:
        print("Funds added succesfully")
    sql="insert into ismart values(%s,%s,%s,%s,%s,%s)"
    val=(name,age,mob,adhar,pan,paisa)
    self.mycursor.execute(sql,val)
    self.mydb.commit()
    print(self.mycursor.rowcount,"Data recorded successfully")
    
def deposit():
    p=int(input("Enter the money you want to deposit"))
    paisa=paisa+p
    print("Funds added successfully")
    jk=int(input("Press 1 to display your account balance"))
    if jk==1:
        print("You have",paisa ,"amount remaining")





print("Welcome to i_Smart Bank\n")
print("We have 3 choices of account opening:\n")
print("1. Savings")
print("2. Current")
print("3. i_smart savings\n")
print("Press '0' to know more about i_smart savings or 1/2/3 for respective choices")
x=int(input("Please enter your choices"))
if x==0:
    print("This is a new type of savings account introduced by our bank for intelligent and smart management of your precious money")
    print("Int this type of savings account your money will be debited automatically and will be distributed as per our criteria which you can customised as per your needs")
    print("This will provide you a better experience while dealing with money")
    print("Advantages:\n #Get rid of unwanted spendings\n #You'll always have money in case of emergencies\n #You'll become smart while dealing with money")
    print("Money will be divided in following manner:\n 50% of total money will be automatically invested in a Flexi Fixed Deposit which you can withdraw any time without any fees, and you'll get a fixed 7% return on your investment per annum\n Rest 40% will be for monthly expense")
elif x==1:
    sav()
elif x==2:
    cur()
elif x==3:
    ismart()
else:
    print("Invalid Entry")




class ismart():
    def fun():
     print("Press 1 to display your balance")
     print("Press 2 to deposit money")
     print("Press 3 to withdraw money")
     print("Press 4 to display total funds")
     n=int(input())
     if n==1:
         print("Your account balance is",paisa)
     if n==2:
         pa=int(input("Enter the money you want to deposit"))
         paisa+=pa
         print("Funds added successfully")
     if n==3:
         ap=int(input("Enter the money you want to withdraw"))
         paisa-=ap
     if n==4:
         print("jk")
     else:
        print("Invalid entry")


class savings():
    def fun():
     print("Press 1 to display your balance")
     print("Press 2 to deposit money")
     print("Press 3 to withdraw money")
     n=int(input())
     if n==1:
         print("Your account balance is",paisa)
     if n==2:
         pa=int(input("Enter the money you want to deposit"))
         paisa+=pa
         print("Funds added successfully")
     if n==3:
         ap=int(input("Enter the money you want to withdraw"))
         paisa-=ap
     else:
        print("Invalid entry")

class current():
    def fun():
     print("Press 1 to display your balance")
     print("Press 2 to deposit money")
     print("Press 3 to withdraw money")
     n=int(input())
     if n==1:
         print("Your account balance is",paisa)
     if n==2:
         pa=int(input("Enter the money you want to deposit"))
         paisa+=pa
         print("Funds added successfully")
     if n==3:
         ap=int(input("Enter the money you want to withdraw"))
         paisa-=ap
     else:
        print("Invalid entry")


class loans():
    print("We offer 4 types of loans that are:")
    print("1.Home Loan starting at 7.99%*")
    print("2.Car Loan starting at 8.99%*")
    print("3.Personal Loan starting at 11.99%*")
    print("4.Study Loan starting at 4.99%*")
    print("The interest rates of loans depends upon your cibil score and your management of money if you have an i_smart account")
    loan=int(input("Please enter your choice"))
    print("Please add your salary slip and Income Tax Return of past 4 years")
    print("We will go through your records and will contact you shortly")'''
print("Ok")