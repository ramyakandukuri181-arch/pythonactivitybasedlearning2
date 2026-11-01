prepared = [100, 120, 150, 100, 200]
served = [90, 100, 120, 95, 150]

for i in range(5):
    waste = prepared[i] - served[i]
    percentage = (waste / prepared[i]) * 100

    print("Day", i + 1)
    print("Food Waste:", waste)
    print("Waste Percentage:", percentage)

    if percentage > 20:
        print("High Food Waste")
    else:
        print("Acceptable Food Waste")