marks = [
    [85, 90, 80],
    [75, 88, 92],
    [95, 90, 98]
]

for i in range(len(marks)):
    total = sum(marks[i])
    average = total / len(marks[i])

    print("Student", i + 1)
    print("Total:", total)
    print("Average:", average)

subject_totals = [0, 0, 0]

for row in marks:
    for j in range(3):
        subject_totals[j] += row[j]

print("Subject Totals:", subject_totals)

print("Top Student:",
      marks.index(max(marks, key=sum)) + 1)