from logging_config import *


class Bank:

    def __init__(self, bank_name):

        self.bank_name = bank_name


class Customer:

    def __init__(self, first_name, last_name, address):
        
        self.first = first_name
        self.last = last_name
        self.address = address

        # each time an instance is generated, log the customer's name (uncomment line 21 for testing)
        # logger.info('New Customer - Full Name: {} {}'.format(self.first, self.last))


    @property
    def fullname(self):
        """
        Returns the full name of a customer.
        """
        return f"{self.first} {self.last}" 


    def __repr__(self):
        return f"Customer - First Name: {self.first}, Last Name: {self.last}, Address: {self.address}"



class Account:

    def __init__(self, customer, account_type, balance):
        
        self.customer = customer
        self.account_type = account_type
        self.balance = balance

        # each time an instance is generated, log the customer's name, account type and starting balance
        logger.info(f"Customer: {self.customer.fullname} created a {self.account_type} account with a starting balance of ${self.balance: ,.2f}")

    
    def account_balance(self):
        return f"Your current account balance is: ${float(self.balance): ,.2f}"

    
    def deposit(self):
        """
        This method prompts the user to input a deposit amount.
        From which, the designated amount is added to the customer's account balance.

        Returns the deposited amount and the updated account balance.
        """
        deposit_amt = float(input(f"Enter deposit amount: "))

        # check that the deposit amount is greater than 0, else raise a Value Error
        if deposit_amt <= 0:
            raise ValueError("Deposit amount must be a positive number")
        

        self.balance += deposit_amt

        # confirm that the deposit has been successful by returning the deposit amount and new account balance
        return f"Amount Deposited: ${float(deposit_amt): ,.2f}.\nCurrent Account Balance: ${float(self.balance): ,.2f}"


    def withdrawal(self):
        """
        This method prompts the user to input a withdrawal amount.
        From which, the designated amount is withdrawn from the customer's account balance so long as the amount is less than
            or equal to the account balance.

        Returns the withdrawn amount and the updated account balance.
        """
        
        withdrawal_amt = input(f"Enter withdrawal amount: ")

        # check that withdrawal amount is less than or equal to the current account balance
        if self.balance >= int(withdrawal_amt):
            self.balance -= int(withdrawal_amt)

            # confirm that the withdrawal has been successful by returning the amount withdrawn and new account balance
            return f"Amount Withdrawn: ${float(withdrawal_amt): ,.2f}.\nCurrent Account Balance: ${float(self.balance): ,.2f}"
        
        else:
            return f"Insufficient Funds: Withdrawal amount must be less than or equal to the current account balance."


    def __repr__(self):
        return f"Customer Name: {Customer.fullname}, Account Type: {self.account_type}, Balance: ${self.balance: ,.2f}"



class Employee:
    
    # define Employee class attributes
    min_salary = 50000
    pct_bonus = 0.05


    def __init__(self, first_name, last_name, title, salary):

        self.first = first_name
        self.last = last_name
        self.title = title
        self.salary = salary

        # determine if salary is greater than or equal to the 'min_salary' (as defined above)
        # if not, set salary equal to the 'min_salary' amount
        try:
            if salary >= Employee.min_salary:
                self.salary = salary
            else:
                self.salary = Employee.min_salary
        
        except ValueError:
            return f"Salary must be a positive number"


    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    
    @staticmethod
    def eligible_bonus_amt(self):
        """
        Returns an employee's eligible bonus amount.
        Where the default bonus amount is set to 5% of an employee's salary.
        """
        return f'{self.fullname} is eligible for a ${self.salary * Employee.pct_bonus: ,.2f} bonus.'



    def __repr__(self):
        return f"Employee Name: {self.fullname}, Title: {self.title}, Salary: ${self.salary: ,.2f}"