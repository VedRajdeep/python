students_python = {"Amit", "Priya", "Rahul", "Sneha", "Vikram"}
students_data_science = {"Rahul", "Sneha", "Deepak", "Ananya", "Vikram"}

both_subjects = students_python.intersection(students_data_science)



all_unique_students = students_python.union(students_data_science)

print("Python Students:      ", students_python)
print("Data Science Students:", students_data_science)
print("1. Learning Both:     ", both_subjects)
print("2. All Unique Total:  ", all_unique_students)
