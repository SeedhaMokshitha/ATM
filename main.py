
# ATM Transaction Sequence Simulation

balance = 5000
withdrawal_limit = 2000

transactions = []
total_deposits = 0
total_withdrawals = 0
rejected_transactions = 0

print("===== ATM TRANSACTION SIMULATION =====")
print("Initial Balance: Rs.", balance)

# Transaction sequence
transaction_list = [
    ("Deposit", 1500),
    ("Withdraw", 1000),
    ("Withdraw", 2500),
    ("Deposit", 500),
    ("Withdraw", 2000),
    ("Withdraw", -300),
    ("Deposit", 0)
]

for transaction, amount in transaction_list:

    print("\nTransaction:", transaction, "| Amount: Rs.", amount)

    if amount <= 0:
        print("Rejected: Amount must be positive.")
        rejected_transactions += 1

    elif transaction == "Deposit":
        balance += amount
        total_deposits += amount
        transactions.append("Deposit: Rs. " + str(amount))
        print("Deposit successful.")

    elif transaction == "Withdraw":
        if amount > withdrawal_limit:
            print("Rejected: Withdrawal limit exceeded.")
            rejected_transactions += 1

        elif amount > balance:
            print("Rejected: Insufficient balance.")
            rejected_transactions += 1

        else:
            balance -= amount
            total_withdrawals += amount
            transactions.append("Withdrawal: Rs. " + str(amount))
            print("Withdrawal successful.")

    else:
        print("Invalid transaction type.")
        rejected_transactions += 1

    print("Current Balance: Rs.", balance)

# Final summary
print("\n===== TRANSACTION SUMMARY =====")
print("Initial Balance: Rs. 5000")
print("Total Deposits: Rs.", total_deposits)
print("Total Withdrawals: Rs.", total_withdrawals)
print("Rejected Transactions:", rejected_transactions)
print("Number of Successful Transactions:", len(transactions))
print("Final Balance: Rs.", balance)

print("\nSuccessful Transaction History:")
for item in transactions:
    print(item)
