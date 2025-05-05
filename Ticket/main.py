class Ticket():
	def __init__(self, cost):
		self.cost = cost

	def calcTicketCost(self, visitors):
		return self.cost * visitors


class StudentTicket(Ticket):
	def __init__(self, cost):
		super().__init__(cost)

	def calcTicketCost(self, visitors):
		return self.cost * visitors * (1 - 0.4)


a = Ticket(20)
print(a.calcTicketCost(4))

b = StudentTicket(20)
print(b.calcTicketCost(4))
