## Banking System: Python OOP


### Introduction
In this project, a simple banking system was designed using Python OOP techniques. The project itself is comprised of the following: `main`, `banking_system_classes` and `logging_config`.

### File Name: `main.py`
1. Upon execution, the user is prompted to provide information about themselves, along with an initial deposit amount.
2. Once entered, the information is captured in a CSV file called `banking_system_user_data` (assuming that such a file does not already exist within the same directory).
3. At which point, the user may select from a list of options, such as: Viewing Account Balance, Make a Deposit, Make a Withdrawal, and Exit.
> **_NOTE:_** For testing, uncomment lines 11-14 and 35-37 (from `main.py`) to enable step #2 (above)

</br>

### File Name: `banking_system_classes.py`
- Contained within are 3 classes: Customer, Account and Employee.
- The `Customer` class represents the customer's name and address.
- The `Account` class represents a customer's account type, current balance and list of options (as listed in point #3 above).
- Lastly, the `Employee` class includes an employee's name, title and salary.
> **_NOTE:_** For testing, uncomment line 20 (from `banking_system_classes.py`) to enable logging

</br>

### File Name: `logging_config.py`
- Logging is implemented to allow for error and warning messages to be printed to both the terminal and a log file which is to be stored in a logs folder.
- As such, two log handlers are created: `FileHandler` and `StreamHandler`.