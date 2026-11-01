marks = [85, 90, 75, 95, 80]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

for m in marks:
    if m >= 85:
        print(m, "Excellent")
    elif m >= 50:
        print(m, "Good")
    else:
        print(m, "Needs Improvement")