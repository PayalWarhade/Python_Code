# Python program to create Bankaccount 
class Bank_Account:
	def __init__(self):
		self.balance=0

	def deposit(self):
		depo_amount=float(input("Enter amount to be Deposited: "))
		self.balance += depo_amount
		print("\n Amount Deposited:",depo_amount)

	def interest_rate(self):
		interest_rate = float(input("Enter rate of interest: "))
		if depo_amount>=1000000:
			print("\n enter rate of interest between 2 to 4:",interest_rate)
		else:
			print("\n enter rate of interest between 6 to 8:",interest_rate)
		mat_amt = depo_amount+(depo_amount*interest_rate/100)

	def display(self):
		print("\n  maturity amount =",mat_amt)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.interest_rate()
s.display()
