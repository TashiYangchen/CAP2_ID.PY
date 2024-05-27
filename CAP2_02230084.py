# Terminal Banking Application
'''Brief Desription about the question: 
This is a Python script for a simple banking system that allows users to create accounts (saving/checking) ,log in,
check their balance, deposit/withdraw (with error handling), and delete their accounts.'''
# Solution: 
import os #The lines import the os module, which offers functions for interacting with the operating system
import json # The json module, which provides functions for handling JSON data.

class Account: # This code defines a class named BankAccount to represent a bank account.
#The class has four attributes:
    def __init__(self, account_number, password, account_type, balance=0): 
        #  The __init__ method initializes a new BankAccount object with given values for the four attributes.
        self.account_number = account_number # account_number: Unique identifier for the account.
        self.password = password # password: For account security.
        self.account_type = account_type # account_type:  e.g., checking, savings.
        self.balance = balance # Current amount of money in the account.

    def deposit(self, amount): # The deposit method allows adding money to the account by increasing the balance.
        self.balance += amount

    def withdraw(self, amount): #The withdraw method allows removing money from the account if there's sufficient balance.
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def delete(self): # The delete method is a placeholder for future implementation of account deletion logic.
        pass

class PersonalAccount(Account): # The provided code defines subclasses of a general Account class.
    pass
class BusinessAccount(Account):
    pass
'''The code defines subclasses (likely PersonalAccount and BusinessAccount) that inherit the core functionalities 
(deposit, withdraw) from a general Account class.
These subclasses are currently empty shells with no unique features for specific account types.
This design allows future extension where these subclasses can be customized for personal or business needs.'''

def create_account():
    account_number = input("Enter account number: ")
    password = input("Enter password: ")
    account_type = input("Enter account type (Personal/Business): ")
    '''This function creates a new account:
Asks user for account number, password, and type (personal or business).
Creates a new PersonalAccount or BusinessAccount based on the type.
Saves the account information (likely including number, password, and type) to a file named "accounts.txt" 
in JSON format.'''
    if account_type.lower() == "personal":
        account = PersonalAccount(account_number, password, account_type)
    else:
        account = BusinessAccount(account_number, password, account_type)

    with open("accounts.txt", "a") as file:
        file.write(json.dumps({
            "account_number": account.account_number,
            "password": account.password,
            "account_type": account.account_type,
            "balance": account.balance
        }) + "\n")

def login():
    account_number = input("Enter account number: ")
    password = input("Enter password: ")

    with open("accounts.txt", "r") as file:
        for line in file:
            account = json.loads(line)
            if account["account_number"] == account_number and account["password"] == password:
                return account

    print("Invalid account number or password")
    return None
'''This function enables a user to log into their account. 
It prompts the user to enter their account number and password, then verifies these credentials against the 
accounts listed in "accounts.txt". If a match is found, the function returns the corresponding account details. 
If no match is found, it displays an error message and returns None.'''
def main(): #It displays a menu to the user and handles their input
    while True: # starts an infinite loop with while True:. This loop will continue running until the program is terminated.
        print("1. Create account") #Inside the loop, it prints a menu with two options: "1. Create account" and "2. Login".
        print("2. Login")
        choice = input("Enter your choice: ")
        # #It then prompts the user to enter their choice and stores the user's input in the choice variable.
        if choice == "1": # If choice is "1", it calls the create_account() function to allow the user to create a new account.
            create_account()
        elif choice == "2":
            account = login()
            # The program allows users to log in (choice 2) and manage their account if successful. This account 
            # management involves a loop that lets them check balance, deposit, withdraw, delete their account, or 
            # log out until they choose the latter.
            while True:
                    print("1. Check balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Delete account")
                    print("5. Logout")
                    sub_choice = input("Enter your choice: ")

                    if sub_choice == "1":
                        print(f"Your balance is {account['balance']}")
                    elif sub_choice == "2":
                        amount = float(input("Enter amount to deposit: "))
                        account["balance"] += amount
                    elif sub_choice == "3":
                        amount = float(input("Enter amount to withdraw: "))
                        if amount > account["balance"]:
                            print("Insufficient funds")
                        else:
                            account["balance"] -= amount
                    elif sub_choice == "4":
                        # Implement deletion logic here
                        pass
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice") 
                        # If the user enters an invalid choice (i.e., something other than "1" or "2"), 
                        # the program will do nothing and continue running the main loop.

if __name__ == "__main__":
    main()
'''The main() function is called at the end of the script, after the class and function definitions, with the line 
if __name__ == "__main__":main(). This line ensures that the main() function is only called if the script is run 
directly, not if it's imported as a module..'''