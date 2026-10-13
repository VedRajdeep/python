students = [
    {"Name": "Alice Smith", "Age": 20, "Course": "Computer Science", "Marks": 85.5},
    {"Name": "Bob Jones", "Age": 21, "Course": "Data Science", "Marks": 42.0},
    {"Name": "Charlie Brown", "Age": 19, "Course": "Mathematics", "Marks": 78.0},
    {"Name": "Diana Prince", "Age": 22, "Course": "Physics", "Marks": 95.0},
    {"Name": "Evan Wright", "Age": 20, "Course": "Computer Science", "Marks": 65.5},
    {"Name": "Fiona Gallagher", "Age": 21, "Course": "Data Science", "Marks": 48.0},
    {"Name": "George Stark", "Age": 23, "Course": "Physics", "Marks": 72.0},
    {"Name": "Hannah Abbott", "Age": 19, "Course": "Mathematics", "Marks": 88.5},
    {"Name": "Ian Malcolm", "Age": 22, "Course": "Computer Science", "Marks": 35.0},
    {"Name": "Julia Roberts", "Age": 20, "Course": "Data Science", "Marks": 91.0}
]


print("=========================================================")
print("                  ALL STUDENT RECORDS                    ")
print("=========================================================")
for s in students:
    print(f"Name: {s['Name']:<16} | Age: {s['Age']} | Course: {s['Course']:<18} | Marks: {s['Marks']}")
print("=========================================================\n")



total_students = len(students)


total_marks = 0
passed_count = 0
failed_count = 0
above_75_students = []


highest_student = students[0]
lowest_student = students[0]


for s in students:
    current_marks = s["Marks"]
    total_marks += current_marks
    
   
    if current_marks >= 50:
        passed_count += 1
    else:
        failed_count += 1
        
    
    if current_marks > 75:
        above_75_students.append(s["Name"])
        
    
    if current_marks > highest_student["Marks"]:
        highest_student = s
        
    
    if current_marks < lowest_student["Marks"]:
        lowest_student = s


average_marks = total_marks / total_students
highest_marks = highest_student["Marks"]
lowest_marks = lowest_student["Marks"]



print("=========================================================")
print("               STUDENT PERFORMANCE REPORT                ")
print("=========================================================")
print(f"1. Total Number of Students   : {total_students}")
print(f"2. Class Average Marks        : {average_marks:.2f}")
print(f"3. Highest Mark in Class      : {highest_marks}")
print(f"4. Lowest Mark in Class       : {lowest_marks}")
print(f"5. Number of Students Passed  : {passed_count}")
print(f"6. Number of Students Failed  : {failed_count}")

print(f"\n7. Students scoring above 75 ({len(above_75_students)} total):")
for name in above_75_students:
    print(f"   - {name}")

print(f"\n8. Highest Scoring Student    : {highest_student['Name']} ({highest_student['Marks']} Marks in {highest_student['Course']})")
print(f"9. Lowest Scoring Student     : {lowest_student['Name']} ({lowest_student['Marks']} Marks in {lowest_student['Course']})")
print("=========================================================")
