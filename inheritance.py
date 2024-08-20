#parent class
class Animal:
    def sleep(self):#parent class method
        print("i can sleep")
    def eat(self):#parent class method
        print("i can eat")
#child class
class Dog(Animal):
    def bark(self): #child class
        print("i can bark!woof")
#create object of dog class
dog1=Dog()
dog1.eat() #of parent class
dog1.sleep() #of parent class
dog1.bark() #of child class

