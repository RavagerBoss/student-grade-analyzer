import csv

# Reads marks.csv
with open('marks.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

header = data[0]  # ['Name', 'Math', 'Physics', 'Chemistry', ...]
students = data[1:]

# Opens report.csv to write
with open('report.csv', 'w', newline='') as file:
    writer = csv.writer(file)

#  Writes header for new file
    writer.writerow(['Name', 'Total', 'Average', 'Result'])

    print("\n Final Report")
    print("----------------------------")

    for row in students:
        name = row[0]
        marks = list(map(float, row[1:6]))  # Assuming 5 subjects

        total = sum(marks)
        average = total / len(marks)
        result = 'PASS' if average >= 40 else 'FAIL'

        print(f"{name} - Total: {total}, Avg: {round(average, 2)}, Result: {result}")

#  Writes in new CSV
        writer.writerow([name, total, round(average, 2), result])