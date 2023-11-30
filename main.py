from banking_system_classes import *

import csv
import os

csv_file = "banking_system_user_data.csv"
header = ["First Name", "Last Name", "Address", "Account Type", "Balance"]

# instantiate a CSV file with the designated headers (uncomment lines 11-14 for testing)
# user inputs will then be stored within this file
# if not os.path.exists(csv_file):
#     with open(csv_file, "a", newline = "") as file:
#         csv_writer = csv.writer(file)
#         csv_writer.writerow(header)


bank_name = 'Fictional Bank'

while True:

    # collect user inputs for the Customer class
    first_name = input(f"Enter your first name: ")
    last_name = input(f"Enter your last name: ")
    address = input(f"Enter your address: ")
    account_type = input(f"Type of Account - Checking or Savings: ")

    # check that account type equals checking or savings, else prompt the user for valid input
    if account_type.lower() not in ["checking", "savings"]:
        print("\nPlease select 1 of the 2 options provided: Checking or Savings")
        account_type = input(f"Type of Account - Checking or Savings: ")
        
    balance = int(input(f"Enter deposit amount: "))

    # save the collected user inputs to the 'banking_system.csv' file (uncomment lines 35-37 for testing)
    # with open(csv_file, "a", newline = "") as file:
    #     csv_writer = csv.writer(file)
    #     csv_writer.writerow([first_name, last_name, address, account_type, balance])

    # generate instances of the Customer and Account classes based on user inputs
    customer_1 = Customer(first_name, last_name, address)
    account_1 = Account(customer_1, account_type, balance)
 
    # nested 'while' loop enables users to perform multiple transactions in a single instance
    # ie. a customer may want to view their account balance first, before depositing or withdrawing funds
    while True:

        print(f"\nPlease select from the following options:")
        print(f"1) View Account Balance\n2) Make a Deposit\n3) Make a Withdrawal\n4) Exit\n")

        selection = int(input("Please select an option: "))

        # determine if user selection is valid
        if selection in range(1, 5):

            if selection == 1:
                print(account_1.account_balance())
                
            elif selection == 2:
                print(account_1.deposit())

                
            elif selection == 3:
                print(account_1.withdrawal())   
                
                
            elif selection == 4:
                print(f"Thank you for banking with us today!")
                exit()
            

        else:
            raise ValueError("To select an option, please enter the corresponding number (1 - 4)")


        # check if user wishes to perform another action, in which case the while loop may continue runnint
        response = input("\nDo you wish to perform another transaction? (Y/N)")
        
        if response.lower() == 'n':
            print(f"Thank you for banking with us today!")
            exit()