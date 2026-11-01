basic = int(input("Enter basic salary: "))
hra = basic * 0.20
da = basic * 0.10
bonus = 2000

gross = basic + hra + da + bonus
deduction = gross * 0.05
net = gross - deduction

print("Basic Salary:", basic)
print("HRA:", hra)
print("DA:", da)
print("Bonus:", bonus)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)