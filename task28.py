students = [
    {"name": "Amit", "age": 20, "course": "Python", "marks": 85},
    {"name": "Priya", "age": 21, "course": "Data Science", "marks": 92},
    {"name": "Rahul", "age": 22, "course": "Machine Learning", "marks": 78},
    {"name": "Sneha", "age": 20, "course": "Python", "marks": 95},
    {"name": "Vikram", "age": 21, "course": "Data Science", "marks": 64}
]

for x in students:
    print(f"Name: {x['name']},Age :{x['age']},Course: {x['course']},Marks: {x['marks']}")

highest_student = max(students,key = lambda x:x['marks'])
print(f"Highest Marks: {highest_student['name']} ({highest_student['marks']})")

Lowest_student = min(students,key = lambda x:x['marks'])
print(f"Highest Marks: {Lowest_student['name']} ({Lowest_student['marks']})")

total_marks = sum(x['marks'] for x in students)
average_marks = total_marks / len(students)
print(f"Average Marks: {average_marks:.2f}")