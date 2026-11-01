marks = []

for i in range(5):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)
average = total / 5

print("Total Marks:", total)
print("Average:", average)

if min(marks) >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")

if average >= 90:
    print("Grade: A")
elif average >= 75:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: D")