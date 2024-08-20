#Sorting objects of user defined class in Python
print(sorted([1,5,2,8]))
print(sorted("shriya".split()))

#user defined class
class My_User:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    def __repr__(self):
        return str((self.a,self.b))
#lists of objects
gfg=[My_User("shriya",1),
     My_User("computer",3),
      My_User("jim",2),
       My_User("physics",4),
        My_User("science",3)]

#sorting objects on the basis of the value
#sorted at variable
print(sorted(gfg,key=lambda x: x.b))

def func(num):
    temp=num
    prod=1
    while temp > 0:
        digit=temp%10
        prod = prod*digit
        temp //=10
    return prod
num=22.11
print("product of all digits {0} is {1}".format(num,func(num)))
func(num)