#rate of interest for method overriding
class Bank:
    def getroi(self):
        pass
class SBI(Bank):
    def getroi(self):
        return 7
class hdfc(Bank):
    def getroi(self):
        return 8
class boi(Bank):
    def getroi(self):
        return 7.5
s1=SBI()
h1=hdfc()
b1=boi()
print("sbi roi:",s1.getroi())
print("hdfc roi:",h1.getroi())
print("boi roi:",b1.getroi())

    