def withdraw(balance,amount):
    if amount>balance:
        raise Exception("Insufficient funds")
    else:
        return balance-amount
balance=200
amount=int(input("Enter the amount to withdraw"))
result=withdraw(balance,amount)
print(result)

