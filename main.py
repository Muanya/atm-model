from Account import Account, input_integer, gen_acc_no
from Account import update_user, verify_user, save_user
from time import sleep


"""
What is yield in python
why can't function be declared below
Why does my program run twice

"""

def register_user():
	while True:
		username = input("Enter Your Username:\n")

		duplicate = verify_user(username)

		if duplicate is None:
			break

		print("Username already exists! \n Try again...")



	while True:
		password1 = input("Enter your password:\n")
		password2 = input("Re-enter your password:\n")

		if password1 == password2:
			break
		
		print("The two passwords should be the same!\n Try again!\n")

	print("Generating Account number")
	acc = gen_acc_no()
	sleep(2)
	print('Generated sucessfully')
	print ('Your account number is {}\n'.format(acc))


	amt = input_integer("Enter amount to start with: \n", "Invalid amount!\n Setting balance to =N= 0.00")

	if amt < 0:
		amt = 0

	sleep(3)
	user = Account(username, password1, acc, amt)
	save_user(user)

	print('Registration Successful!')
	


def process_registered_user():
	user = input('Enter your username\n')

	current_user = verify_user(user)

	if current_user is not None:
		password = input('Enter your password:\n')

		if password == current_user.get_password():
			print(f'\n\nWelcome {current_user.username}!\n\n')
			print('Select an option below:')
			print('1. Withdraw \t\t 4. Change Pin ')
			print('2. Deposit \t\t 5.Check Balance')
			print('3. Transfer \t\t 6.Transaction History \n')

			option = input_integer('What\'s your choice?\n', 'Invalid character selected!')

			if option == 1:
				current_user.withdraw_money()
				update_user(current_user)
			elif option == 2:
				current_user.deposit_money()
				update_user(current_user)
			elif option == 3:
				current_user.transfer_money()
				update_user(current_user)
			elif option == 4:
				current_user.change_pin()
				update_user(current_user)
				print('Pin changed sucessfully!\n')
			elif option == 5:
				print("Account Number: {}".format(current_user.account_no))
				print('\n Account balance is:\n =N= {}'.format(current_user.balance))
			elif option == 6:
				current_user.get_history()

			else:
				print('Invalid option selected!')

		else:
			print("Sorry!\n The password you entered is incorrect!")

	else:
		print('User does not exist!')

	


"""
	Note: Register accounts to get started.
"""

play = 'y'

while play == 'y':

	print('Welcome to Zuri ATM\n')
	
	print('1. Register \t\t 2. Already registered \n')

	option = input_integer('Select an option: ', '\n Invalid input! \n')

	if option == 1:
		register_user()
		play = input("Do you want to perform a transaction? (y/n)\n")
	elif option == 2:
		process_registered_user()
		play = input("Do you want to perform another transaction? (y/n)\n")
	else:
		print("\n")
		play = 'y'




print('\n\n\t Thank you for banking with us')



