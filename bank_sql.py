import sqlite3

connection = sqlite3.connect('BankAccounts.db')
print("Database Opened Successfully...")

def CreateAccount():
	Account_number = input("Enter the Account Number: ")
	Account_holder_name = input("Enter Account Holder Name: ")
	Account_balance = input("Enter Initial Balance: ")
	connection.execute(f"insert into bank(Account_number, Account_holder_name, Account_balance) values('{Account_number}', '{Account_holder_name}', '{Account_balance}');");
	connection.commit()
	print("Account Created Successfully...")

def ShowAllAccounts():
	cursor = connection.execute("select * from bank")
	for row in cursor:
		print("_" * 30)
		print("Account Number: ", row[0])
		print("Account Holder Name: ", row[1])
		print("Avaliable Balance: ", row[2])

def Transaction():
	Debit_account_number = int(input("Enter Account Number to Debit Amount: "))
	Debit_amount = int(input("Enter how much Amount to be debit: "))
	Credit_account_number = int(input("Enter Account Number to Credit Amount: "))
	cursor = connection.execute("select * from bank")
	try:
		for row in cursor:
			if(row[0] == Credit_account_number):
				connection.execute(f"Update bank set Account_balance = Account_balance - {Debit_amount} where Account_number = {Debit_account_number}")
				connection.execute(f"Update bank set Account_balance = Account_balance + {Debit_amount} where Account_number = {Credit_account_number}")
				print("Amount Transfered Successfully...")
				connection.commit()
	except:
		rollback(connection)
		print("Transaction Failed!!!")

def Exit():
	print("Thank You...")
	exit()

while True:
	print("\n_____BANK CUSTOMER DETAILS_____")
	print("1.Create An Account\n2.Show All Accounts\n3.Transaction Details\n4.Exit\n")
	menu = [CreateAccount, ShowAllAccounts, Transaction, Exit]
	try: 
		menu[int(input("Enter your choice: "))-1]()
	except IndexError:
		print("Invalid input!!!")

 