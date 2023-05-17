from bankaccount import bankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankAccount(int_rate=10, balance=0)
        self.account1 = bankAccount(iny_rate=10,balance=0)
        
    
    
    
    def make_deposit(self, amount):
        num = 0
        print("select your account",num)
        if num == 1:
            self.account.deposit()
        if num == 2:
            self.account1.deposit()
        else:
            print("account not found")
        return self
        
    
    def make_withdrawal(self,amount):
        self.account.withdraw()
        return self
    
    def display_user_account(self):
        bankAccount.display_account_info()
        return self
    
    	
money = bankAccount(10,0)
money.deposit(80)
money.withdraw(50)
money.display_account_info()


