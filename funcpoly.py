class Vehicle():

     def drive(self):
        pass

class Bike(Vehicle):
    
    def drive(self):
        return"I am ridding"

class Car(Vehicle):
  
    def drive(self):
        return "I am driving"

b1=Bike()
c1=Car()
print(c1.drive())
print(b1.drive())