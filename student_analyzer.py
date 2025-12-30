# Student Data Analyzer
# Author: Alyazia Alameri

students = {}
num_students = int(input("How many students? "))

for i in range(num_students):
    name = input("Student name: ")
    score = float(input("Student score: "))
    students[name] = score

scores = list(students.values())

average = sum(scores) / len(scores)
highest = max(scores)
lowest = min(scores)

print("\n--- Results ---")
print("Average score:", average)
print("Highest score:", highest)
print("Lowest score:", lowest)

print("\nStudent List:")
for name, score in students.items():
    print(name, ":", score)
