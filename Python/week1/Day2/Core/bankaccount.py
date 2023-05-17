class bankAccount:
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"your balance : {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
             print("Insufficient funds: Charging a $5 fee")
             self.balance = self.balance - 5
        else:
            self.balance = self.balance - amount
            print(f"your balance : {self.balance}")
            
    def display_account_info(self):
        print(f"Balance :{self.balance}")  
       
    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance + (self.int_rate *0.1)
            print(f"your account after interest : {self.balance}")
        else:
            print("your account is empty")
        



# test BankAccount
account = bankAccount(10,100)
account.deposit(20)
account.withdraw(30)
account.display_account_info()
account.yield_interest()


