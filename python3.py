balance = 5000

deposit = int(input("Enter deposit amount: "))
balance += deposit

withdraw = int(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal successful")
else:
    print("Insufficient balance")

print("Final Balance:", balance)