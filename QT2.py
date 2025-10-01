class Account:
    def __init__(self, name, balance, acc):
        self.name = name                 
        self.balance = balance           
        self.account_number = acc        

    def deposit(self, amount):
        self.balance += amount
        print(self.name, "deposited Rs", amount)
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance -= amount
        print(self.name, "credited Rs", amount)
        print("Total balance =", self.get_balance()) 

    def get_balance(self):
        return self.balance


acc1 = Account("Razaq Shah", 1000000 , "12345")
acc1.deposit(44499)   
acc1.credit(500000)
print("Final balance of", acc1.name, "=", acc1.get_balance())


