
from abc import ABC, abstractmethod

#Abstract class Ticket
class Ticket(ABC):
    
    #Constructor which assigns base price of a ticket
    def __init__(self, cost):
        self.cost = cost

    #Abstract method to calculate ticket price
    @abstractmethod
    def calcTicketCost(self, visitors):
        pass
      
class NormalTicket(Ticket):
    def __init__(self,cost):
      super().__init__(cost)
      
    def calcTicketCost(self , visitors):
      
      price = self.cost * visitors
      
      if 1 <= visitors <= 3:
        return price
      elif 4 <= visitors <= 7:
        return price * (1-0.1)
      elif 8 <= visitors <= 10:
        return price * (1-0.15)
      else:
        return price * (1-0.2)
        
class StudentTicket(Ticket):
    def __init__(self, cost):
      super().__init__(cost)
      
    def calcTicketCost(self, visitors):
      return self.cost * visitors * (1-0.4)
      
a = NormalTicket(20)
print(a.calcTicketCost(2))
print(a.calcTicketCost(5))
print(a.calcTicketCost(8))
print(a.calcTicketCost(20))
  
b = StudentTicket(20)
print(b.calcTicketCost(4))