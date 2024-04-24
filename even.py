c=input("Enter a character")[0]
a=ord(c)
if(c>='a' and c<='z'):
 a=a-32
 print(chr(a))
elif(c>='A' and c<='Z')
 a=a+32
 print(chr(a))
else:
 print("Invalid Character")
