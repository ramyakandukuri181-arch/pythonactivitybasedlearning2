menu = ["Idli", "Dosa", "Meals"]
prices = [30, 50, 100]
stock = [20, 15, 10]

total = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))

    if item in menu:
        index = menu.index(item)

        if quantity <= stock[index]:
            bill = prices[index] * quantity
            total += bill
            stock[index] -= quantity

            print("Order Successful")
            print("Item Bill:", bill)
        else:
            print("Insufficient Stock")
    else:
        print("Item Not Available")

print("Total Bill:", total)
print("Remaining Stock:", stock)