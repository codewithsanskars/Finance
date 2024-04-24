print("Welcome to the Car Quiz   ")
x=int(input("Press '1' if you want to play,  Press any other key to exit   "))
score=0
if(x==1):
 print("Q1: Which of these car types has largest boot space in general?")
 print("Option 1: Hatchback ") 
 print("Option 2: Compact-SUV ")
 print("Option 3: Sedan ")
 print("Option 4: None of these ")
 s=int(input("Press 1/2/3/4           "))
 if(s==3):
  score+=1
  print("Right Answer")
 else:
  print("Wrong Answer")
 print("Q1: Which of these cars is best for offroading?")
 print("Option 1: Maruti Suzuki Grand Vitara") 
 print("Option 2: Hyundai Creta")
 print("Option 3: Skoda Superb")
 print("Option 4: Mahindra Thar")
 s=int(input("Press 1/2/3/4           "))
 if(s==4):
  score+=1
  print("Right Answer")
 else:
  print("Wrong Answer")
 print("Q1: Which of these cars is not sold in India ?")
 print("Option 1: Skoda Slavia ") 
 print("Option 2: Hyundai Verna ")
 print("Option 3: Honda City")
 print("Option 4: Ford Raptor ")
 s=int(input("Press 1/2/3/4           "))
 if(s==4):
  score+=1
  print("Right Answer")
 else:
  print("Wrong Answer")
 print("Q1: Which of these Automobile manufacturer produce most selling cars in India ?")
 print("Option 1: Skoda ") 
 print("Option 2: Maruti Suzuki ")
 print("Option 3: Honda ")
 print("Option 4: Volkswagen")
 s=int(input("Press 1/2/3/4           "))
 if(s==2):
  score+=1
  print("Right Answer")
 else:
  print("Wrong Answer")
 print("Q1: Which of these cars isn't listed according to it's near price?")
 print("Option 1: Skoda Slavia: 17.30 Lac ") 
 print("Option 2: Tata Nexon: 49.90 Lac  ")
 print("Option 3: Honda City: 16.80 Lac ")
 print("Option 4: Toyota Fortuner: 39.90 Lac ")
 s=int(input("Press 1/2/3/4           "))
 if(s==2):
  score+=1
  print("Right Answer")
 else:
  print("Wrong Answer")
 print("                        Your Score is", score,"out of 5           Thankyou!"  )
 if(score==5):
  print("Congratulations! You scored 100%      ")
 elif(score==0):
  print("Better Luck next time")
 else:
  print(" You were close!  ")	
else:
 print("Thankyou!")