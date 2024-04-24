y=int(input("Enter a year"))
if(y%400==0 or y%100==0 and y%4==0):
 print("Leap year")
else:
 print("not a Leap year")