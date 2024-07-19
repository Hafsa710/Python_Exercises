#Example 2: Debit & Credit

class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no=acc

    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("RS.",amount,"was debited")
        print("tota balance=",self.get_balance())

         #credit method
    def credit(self,amount):
        self.balance += amount
        print("RS.",amount,"was credited")
        print("total balance=" ,self.get_balance())

    def get_balance(self):
        return self.balance       

acc1 = Account(10000,4749)
acc1.debit(1000)
acc1.credit (500)
