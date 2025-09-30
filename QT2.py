class Account:
    def __init__(self, balance, acc):
        self.balance = balance
        self.account_number = acc

    def deposit(self, amount):
        self.balance += amount
        print("Rs", amount, "was deposited")
        print("total balance =", self.get_balance())

    def credit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was credited")
        print("total balance =", self.get_balance()) 

    def get_balance(self):
        return self.balance


acc1 = Account(1000, "12345")
acc1.deposit(500)   
acc1.credit(200)    
acc1.get_balance()        
print("total balance =", acc1.get_balance())
