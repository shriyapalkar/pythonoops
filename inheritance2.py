#parent class
class Vehicle:
    def drive(self):
        print("we can drive car")
    def run(self):
        print("we can run car")
#child class
class Honda(Vehicle):
    def colour(self):
        print("honda has colour")
honda1=Honda()
honda1.drive()
honda1.run()
honda1.colour()