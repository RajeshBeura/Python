class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("Total balance =",self.get_balance())

    def creadit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("Total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(1000,12345)
print(acc1.balance)
print(acc1.account_no)