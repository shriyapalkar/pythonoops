class Rupy_credit_card:
    def __init__(self,card_name,credit_limit):
        self.card_name=card_name 
        self.credit_limit=credit_limit
    def info(self):
        print(f"This is {self.card_name}.Set limit is{self.credit_limit}")    
        
        
class Visa_creditcard:
    def __init__(self,card_name,credit_limit):
        self.card_name=card_name
        self.credit_limit=credit_limit
    def info(self):
        print(f"This is {self.card_name}.Set limit is{self.credit_limit}")    
        
r1=Rupy_credit_card("Axis Rupay credit card",100000)
v1=Visa_creditcard("Axis visa credit card",300000)
for Axis_Bank in(r1,v1):
    Axis_Bank.info()
        