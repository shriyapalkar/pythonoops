print(len("program"))
print(len(["python","java","c"]))
print(len({"name":"shriya",
       "add":"kudal"}))

#Class Polymorphism in Python
class Cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I am a Cat.My name is {self.name}.I am {self.age}years old")
    def make_sound(self):
        print("meow")
        
class Dog:
        def __init__(self,name,age):
            self.name=name
            self.age=age
        def info(self):
            print("I am a Dog.My name is {self.name}.I am {self.age}yrs old")
        def make_sound(self):
            print("bark")
                   
cat1=Cat("kitty",2.4)
dog1=Dog("fluffy",4)
for animal in(cat1,dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
    
class Mumbai:
    def __init__(self,name,population):
        self.name=name
        self.population=population
    def info(self):
        print(f"Name of City is {self.name} city population is{self.population}")
    
class Pune:
    def __init__(self,name,population):
        self.name=name
        self.population=population
    def info(self):
        print(f"Name of City is {self.name} city .Population is {self.population}")
    
city1=Mumbai("mumbai",1000000)
city2=Pune("Pune",2000000)
for city in (city1,city2):
    city.info()


        

        
        
        