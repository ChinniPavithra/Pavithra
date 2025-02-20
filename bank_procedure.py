import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(host='138.68.140.83', database='dbPavithra', user='Pavithra', password='Chinni@123')
cursor = connection.cursor()

def CreateAccount():
	AccountNumber1 = input("Enter the Account Number: ")
	AccountHolderName1 = input("Enter Account Holder Name: ")
	Balance1 = input("Enter Initial Balance: ")
	cursor.callproc('create_account', args = [AccountNumber1, AccountHolderName1, Balance1])
	connection.commit()
	print("Account Created Successfully...")

def ShowAllAccounts():
	print("_____All Bank Accounts_____")
	cursor.callproc('show_all')
	for row in cursor.stored_results():
		result = row.fetchall()
	print(tabulate(result, headers = ["AccountNumber", "AccountHolderName", "Balance"], tablefmt = "github"))

def UpdateName():
	AccountNumber1 = input("Enter the Account Number: ")
	AccountHolderName1 = input("Enter Account Holder NEW Name: ")
	cursor.callproc('update_name', args = [AccountNumber1, AccountHolderName1])
	connection.commit()
	print("Name Updated Successfully...")
 
def UpdateBalance():
	AccountNumber1 = input("Enter the Account Number: ")
	Balance1 = float(input("Enter Balance: "))
	cursor.callproc('update_balance', args = [AccountNumber1, Balance1])
	connection.commit()
	print("Balance Updated Successfully...")

def UpdateDetails():
	print("1.Update Name\n2.Update Balance")
	choice = [UpdateName, UpdateBalance]
	try:
		choice[int(input("Enter your choice: "))-1]()
	except IndexError:
		print("Invalid Choice!!!")

def SearchAccount():
	AccountNumber1 = input("Enter the Account Number: ")
	cursor.callproc('search_account', args = [AccountNumber1])
	for row in cursor.stored_results():
		result = row.fetchall()
	print(tabulate(result, headers = ["AccountNumber", "AccountHolderName", "Balance"], tablefmt = "github"))

def DeleteAccount():
	AccountNumber1 = input("Enter the Account Number: ")
	cursor.callproc('delete_account', args = [AccountNumber1])
	connection.commit()
	print("Account Deleted Successfully...")

def SortByName():
	print("_____Sorted Order by Name_____")
	cursor.callproc('sort_by_name')
	cursor.callproc('show_all')
	for row in cursor.stored_results():
		result = row.fetchall()
	print(tabulate(result, headers = ["AccountNumber", "AccountHolderName", "Balance"], tablefmt = "github"))

def SortByBalance():
	print("_____Sorted Order by Balance_____")
	cursor.callproc('sort_by_balance')
	cursor.callproc('show_all')
	for row in cursor.stored_results():
		result = row.fetchall()
	print(tabulate(result, headers = ["AccountNumber", "AccountHolderName", "Balance"], tablefmt = "github"))

def Sort():
	print("1.Sort by Name\n2.Sort by Balance")
	choice = [SortByName, SortByBalance]
	try:
		choice[int(input("Enter your choice: "))-1]()
	except IndexError:
		print("Invalid Choice!!!")

def Exit():
	print("Thank You...")
	exit();

while True:
	print("\n_____BANK CUSTOMER DETAILS_____")
	print("1.Create An Account\n2.Show All Accounts\n3.Update Details\n4.Search an Account\n5.Delete an Account\n6.Sort\n7.Exit\n")
	menu = [CreateAccount, ShowAllAccounts, UpdateDetails, SearchAccount, DeleteAccount, Sort, Exit]
	try: 
		menu[int(input("Enter your choice: "))-1]()
	except IndexError:
		print("Invalid input!!!")

 