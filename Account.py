from time import sleep
import pickle
import os


filename = 'accounts.pkl'

def input_integer(info, err_msg):
	try:
		integer = int(input(info))
	except:
		integer = 0
		print(err_msg)

	return integer

class Account(object):
	""" Class for holding account infomation """
	def __init__(self, username, password, balance=0):
		self.username = username
		self.password = password
		self.balance = balance
		self.history = [('Deposited =N= '+ str(balance)+' (Starting balance)')]

	def __str__(self):
		return ("Username: "+self.username)

	def get_password(self):
		return self.password

	def change_pin(self):
		old = input('Enter former password: \n')
		if old == self.password:
			
			while True:
				new = input('Enter new password:\n')
				new2 = input('Re-enter new password:\n')

				if new == new2:
					break
				
				print('The two password must be the same! Try again\n')

			self.password = new # There's a problem here
			
		else:
			print('Invalid Password!')

	def withdraw_money(self):
		amt = input_integer('Enter amount to withdraw (maximum of 50000):\n =N= ', 'Invalid amount entered')

		if amt <= self.balance:
			if amt > 50000 or amt <= 0:
				print('Amount not within acceptable range')
			else:
				print('Processing...\n')
				sleep(5)
				self.balance -= amt
				history = 'Withdrew '+str(amt)
				self.history.append(history)
				print('Take your cash!')
				print('Thanks for banking with us!')
				print("Your new account balance is =N= {}".format(self.balance))
		else:
			print('Insufficient fund')

	def deposit_money(self):
		amt = input_integer('Enter amount to deposit (maximum of 50000)\n =N= ', 'Invalid amount entered')

		if amt <= 0 or amt > 50000:
			print('Amount not within acceptable range!')
		else:
			print('Processing...')
			sleep(5)
			self.balance+=amt
			history = 'Deposited '+str(amt)
			self.history.append(history)
			print("Succesfull!")
			print("Your new account balance is =N={}".format(self.balance))

	def transfer_money(self):
		receiver = input("Enter Recipient account number\n")
		receiver_bank = input("Enter Recipient bank\n")
		amt = input_integer('Enter amount to transfer (maximum of 50000)\n =N= ', 'Invalid amount entered')

		if amt <= 0 or amt > 50000:
			print('Amount not within acceptable range!')
		else:
			if amt <= self.balance:
				print('Processing...')
				sleep(5)
				self.balance-=amt
				history = 'Transfered '+str(amt) +' to Account: '+ receiver + '. Bank: '+receiver_bank
				self.history.append(history)
				print('Transfer was succesfull!') 
				print("Your new account balance is =N= {}".format(self.balance))
			else:
				print("Insufficient fund!")


	def get_history(self):
		print('\n TRANSACTION HISTORY \n ')
		for i in self.history:
			print('=> {}'.format(i))
		
		print('\n Current balance is =N= {}\n'.format(self.balance))




def save_user(obj, filename=filename):
	accounts = load_object()
	accounts.append(obj)
	with open(filename, 'wb') as output:
		pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)


def load_object(filename=filename):
	# if file does not exist, create one with empty accounts
	if not os.path.isfile(filename):
		accounts = []
		with open(filename, 'wb') as output:
			pickle.dump(accounts, output, pickle.HIGHEST_PROTOCOL)

	with open(filename, 'rb') as f:
		accounts = pickle.load(f)
	return accounts


def verify_user(username):
	database = load_object()
	for user in database:
		if username == user.username:
			return user
	return None


def update_user(mod_user):
	database = load_object()
	for i, u in enumerate(database):
		if mod_user.username == u.username:
			del database[i]
			break

	database.insert(i, mod_user)

	with open(filename, 'wb') as output:
		pickle.dump(database, output, pickle.HIGHEST_PROTOCOL)

