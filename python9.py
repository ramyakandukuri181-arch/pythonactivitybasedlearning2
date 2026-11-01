products = [
    ("Pen", 10, 50),
    ("Book", 100, 5),
    ("Bag", 500, 2),
    ("Pencil", 5, 100)
]

total_value = 0

for name, price, stock in products:
    value = price * stock
    total_value += value

    print("Product:", name)
    print("Price:", price)
    print("Stock:", stock)
    print("Value:", value)

    if stock < 10:
        print("Restock Required")
    else:
        print("Stock Available")

print("Total Inventory Value:", total_value)