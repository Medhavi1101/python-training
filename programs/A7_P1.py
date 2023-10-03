class Bank:
    def __init__(self, bank_name, address):
        self.bank_name = bank_name
        self.address = address
        self.accounts = {}

    def create_account(self, acc_type, acc_number, acc_holder_name, initial_balance = 0):
        if acc_number not in self.accounts:
            if acc_type == "Savings":
                new_account = SavingsAccount(acc_number, acc_holder_name, initial_balance)
            elif acc_type == "Current":
                new_account = CurrentAccount(acc_number, acc_holder_name, initial_balance)
            elif acc_type == "Overdraft":
                new_account = OverdraftAccount(acc_number, acc_holder_name, initial_balance)
            else:
                return "Invalid account type"
            
            self.accounts[acc_number] = new_account
            return f"Account {acc_number} created for {acc_holder_name} with an initial balance of {initial_balance}"
        else:
            return f"Account with this account number already exists."
        
    def get_account_balance(self, acc_number):
        if acc_number in self.accounts:
            return f"Account {acc_number} balance: {self.accounts[acc_number].balance}"
        else:
            return "Account not found."

class BankAccount:
    def __init__(self, acc_number, acc_holder_name, balance = 0):
        self.acc_number = acc_number
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def authenticate(self, password):
        if password == self.password:
            return True
        else:
            return False
    
    def change_password(self, oldPassword, newPassword):
        if self.authenticate(oldPassword):
            self.password = newPassword

    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            return f"Deposit of {amount} is successful. New Balance: {self.balance}"
        else:
            return f"Desposit failed. Amount must be greater than zero."
        
    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self.balance -= amount 
            return f" withdraw of {amount} successful. New Balance: {self.balance}"
        else:
            return f"Invalid withdrawal amount or insufficient funds."
        
    def transfer(self, to_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
            return f"Transferred {amount} to {to_account.acc_holder_name}. New Balance: {self.balance}"
        else:
            return f"Invalid transfer amount or insufficient funds"
        
    def credit_interest(self, interest_rate):
        if interest_rate > 0:
            interest = (self.balance * interest_rate) / 100
            self.balance += interest
            return f"Interest credited. New Balance: {self.balance}"
        else:
            return f"Invalid interest rate"
        
class SavingsAccount(BankAccount):
    def __init__(self, acc_number, acc_holder_name, min_balance = 5000, interest_rate = 1.5):
        super().__init__(acc_number, acc_holder_name)
        self.min_balance = min_balance
        self.interest_rate = interest_rate

    def credit_interest(self):
        if self.interest_rate > 0:
            interest = (self.balance * self.interest_rate) / 100
            self.balance += interest
            return f'Interest credited. New Balance {self.balance}'
        else:
            return f'Invalid Interest Rate'

    def withdraw(self, amount):
        if amount < self.balance - self.min_balance:
            self.balance -= amount
            return f"Withdraw successful. New Balance: {self.balance}"
        else:
            return f'Invalid withdrawal amount'


class OverdraftAccount(BankAccount):
    def __init__(self, acc_number, acc_holder_name, max_balance, balance, ODFee, ODLimit,  interest_rate = 1.5 ):
        super().__init__(acc_number, acc_holder_name)
        self.balance = balance
        self.max_balance = balance
        self.ODLimit = ODLimit
        self.ODFee = ODFee
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        ODLimit = (self.max_balance * 0.1) / 100
        if 0 < amount <= self.balance + self.ODLimit:
            self.balance -= amount
            if self.balance < 0:
                ODFee = (self.balance * 1)/100
                self.balance -= ODFee
            return f"Withdraw successful. New Balance: {self.balance}"
        else:
            return f'Invalid withdrawal amount'
        
    def update_max_balance(self):
        if self.balance > self.max_balance:
            self.max_balance = self.balance
        

class CurrentAccount(BankAccount):
    def __init__(self, acc_number, acc_holder_name, balance = 0):
        super().__init__(acc_number, acc_holder_name, balance)

        
        
class ATM:
    def __init__(self, bank):
        self.bank = bank

    def run(self):
        while True:
            print("\n1. Create Account")
            print("2. Check Account Balance")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                acc_type =  input("Enter account type (Savings / Current / Overdraft):")
                acc_number = input("Enter account number: ")
                acc_holder = input("Enter account holder's name: ")
                initial_balance = float(input("Enter initial balance: "))
                print(self.bank.create_account(acc_type, acc_number, acc_holder, initial_balance))

            elif choice =="2":
                acc_number = input("Enter account number: ")
                print(self.bank.get_account_balance(acc_number))

            elif choice == "3":
                acc_number = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                if acc_number in self.bank.accounts:
                    print(self.bank.accounts[acc_number].deposit(amount))
                else:
                    print("Account not found.")

            elif choice == "4":
                acc_number = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                if acc_number in self.bank.accounts:
                    print(self.bank.accounts[acc_number].withdraw(amount))
                else:
                    print("Account not found.")

            elif choice == "5":
                from_acc_number = input("Enter your account number: ")
                to_acc_number = input("Enter recepient's account number: ")
                amount = float(input("Enter transfer amount: "))
                if from_acc_number in self.bank.accounts and to_acc_number in self.bank.accounts:
                    from_account = self.bank.accounts[from_acc_number]
                    to_account = self.bank.accounts[to_acc_number]
                    print(from_account.transfer(to_account, amount))
                else:
                    print("Account not found.")

            elif choice =="6":
                print("Thank you!!!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

my_bank = Bank("ICICI", "Manyata")
atm = ATM(my_bank)
atm.run()



        


    