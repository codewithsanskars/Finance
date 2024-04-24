import os
import random
import string
import csv

class CarReg:
    def __init__(self, make, model, owner, sno, reg_year, state):
        self.make = make
        self.model = model
        self.owner = owner
        self.sno = sno
        self.reg_year = reg_year
        self.state = state
        self.reg_no = self.reg_no_gen()

    def reg_no_gen(self):
        rn = random.randrange(10000)
        rn_str = f"{rn:04}"
        reg_no = f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_uppercase)}{rn_str}"
        return reg_no

    def write(self):
        with open(f"{self.owner}.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Make", "Model", "Owner", "Serial Number", "Registration Year", "State", "Registration Number"])
            writer.writerow([self.make, self.model, self.owner, self.sno, self.reg_year, self.state, self.reg_no])

    def print_data(self):
        with open(f"{self.owner}.csv", "r") as file:
            content = file.read()
            print(content)

make = input("Enter your vehicle's Brand or Manufacturer: ")
model = input("Enter your vehicle's model name: ")
owner = input("Enter the owner name of the vehicle: ")
sno = input("Enter the owner serial number of the vehicle: ")
reg_year = input("Enter the registration year of the vehicle: ")
state = input("Enter the state name of RTO: ")

car = CarReg(make, model, owner, sno, reg_year, state)
car.write()
os.system('cls')
car.print_data()
