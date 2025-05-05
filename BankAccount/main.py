class BankAccount:
  def __inti__(self, id, currency= "EURO"):
    self.id = id
    self.currency = currency
    self.balance = 0
   
  def deposit(self, quantity):
    self.balance += quantity
   
  def withdraw(quantity):
    self.balance -= quantity
   
  def printAmmount (self):
    print (f'Balance = {self.balance}')
    
  def printInfo(self):
    print (f' ID = {self.id}, currency = {self.currency}, balance = {balance}')

a = BankAccount()
print(a)
