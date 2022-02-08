class Account:
    def __init__(self,ac,name,typeofac,balance):
        self.ac=ac
        self.name=name
        self.typeofac=typeofac
        self.balance=balance
    def display(self):
        print("Account number", self.ac)
        print("Name:",str(self.name))
    def withdraw(self):
        if(self.balance==0):
            print("Acount balance =",self.balance)
        n=int(input("Enter amount to withdraw"))
        if(n>self.balance):
            print("insufficient balance")
        else:
            self.balance=self.balance-n
            print("Account balance",self.balance)
    def deposit(self):
        n=int(input("Enter amount to deposit"))
        self.balance=self.balance+n
        print("Account balance",self.balance)
obj=Account(112,"joyal","savings",100000)
obj.display()
print("1:deposit\n 2:withdraw")
n=int(input("enter your option"))
if(n==2):
    obj.withdraw()
elif(n==1):
    obj.deposit()
