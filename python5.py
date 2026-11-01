total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    total += price * quantity

if total >= 2000:
    discount = total * 0.10
else:
    discount = total * 0.05

final = total - discount

print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill:", final)