#create bank acc class wid deposit withdraw function
class Bank_Acc:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
    def deposit(self):
        amount=float(input("enter amount to be depoisted"))
        self.balance +=amount
        print("\n Amount Deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be Withdraw:"))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:",amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("\n Net available balance=",self.balance)
#create object of class
s=Bank_Acc()
s.deposit()
s.withdraw()
s.display()