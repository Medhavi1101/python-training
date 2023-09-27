class Account:
    pass

def create(acc_number,name,password, balance, interest_rate):
    a=Account()
    a.acc_number=acc_number
    a.name=name
    a.password=password
    a.balance = balance
    a.interest_rate = interest_rate
    return a
            
def deposit(a,amount):
    if amount > 0:
        a.balance += amount
        return f'Deposit of {amount} is successful. New balance is: {a.balance}'
    else:
        return f'Desposit failed. Amount must be greater than zero.'

def withdraw(a, amount, attempted_password):
    if amount > 0:
        if amount <= a.balance and attempted_password == a.password:
            a.balance -= amount
            return f'Withdrawal of {amount} is successful. New balance is: {a.balance}'
        elif attempted_password != a.password:
            return f'Withdrawal failed. Incorrect password.'
        else:
            return f'Withdrawal failed. Insufficient balance.'
    else:
        return f'Withdrawal failed. Amount must be greater than zero.'
    
    
def info(a):
        return f'Account Number: {a.acc_number}\nName: {a.name}\nBalance: {a.balance}\nInterest Rate: {a.interest_rate}'

def credit_interest(a):
    monthly_interest = a.balance * (a.interest_rate / 1200)
    a.balance += monthly_interest
    return f'Interest credited: {monthly_interest}. New balance: {a.balance}'
    

def test_account(acc_number,name,password, balance, interest_rate):
    a=create(acc_number,name,password, balance, interest_rate)
    print(info(a))
    print(deposit(a,500))
    print(withdraw(a,200, "password@p"))
    print(credit_interest(a))

test_account('192837', "Medhavi", "password@p", 2000, 5.0)



