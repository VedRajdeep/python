# Initialize an empty list to act as our data store
students = []

while True:
    # Task List Menu System
    print("\n==============================")
    print(" STUDENT DATA MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add a Student")
    print("2. View All Students")
    print("3. Search for a Student")
    print("4. Update Student Marks")
    print("5. Delete a Student")
    print("6. Find Student with Highest Marks")
    print("7. Calculate Average Marks")
    print("8. Exit")
    print("==============================")
    
    choice = input("Enter your choice (1-8): ").strip()
    
    # 1. Add a student (Demonstrates Dictionary Creation and .append() list method)
    if choice == '1':
        print("\n--- Add New Student ---")
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: "))
        course = input("Enter Course: ").strip()
        marks = float(input("Enter Marks: "))
        
        # Store data inside a dictionary structure
        student_dict = {
            "Name": name,
            "Age": age,
            "Course": course,
            "Marks": marks
        }
        # Use list method to add the dictionary to our list
        students.append(student_dict)
        print(f"Student '{name}' added successfully!")
        
    # 2. View all students (Demonstrates Loops and Formatting)
    elif choice == '2':
        print("\n--- All Student Records ---")
        if len(students) == 0:  # Condition check
            print("No student records found.")
        else:
            for s in students:  # For loop iterating through the list
                print(f"Name: {s['Name']} | Age: {s['Age']} | Course: {s['Course']} | Marks: {s['Marks']}")
                
    # 3. Search for a student (Demonstrates Conditions and Loops)
    elif choice == '3':
        print("\n--- Search Student ---")
        search_name = input("Enter the student name to search: ").strip().lower()
        found = False
        
        for s in students:
            if s['Name'].lower() == search_name:  # Match case-insensitive name
                print(f" Found! Name: {s['Name']}, Age: {s['Age']}, Course: {s['Course']}, Marks: {s['Marks']}")
                found = True
                break  # Stop looping once found
        
        if not found:
            print(" Student not found.")
            
    # 4. Update student marks (Demonstrates Dictionary value modification)
    elif choice == '4':
        print("\n--- Update Student Marks ---")
        search_name = input("Enter student name to update marks: ").strip().lower()
        found = False
        
        for s in students:
            if s['Name'].lower() == search_name:
                new_marks = float(input(f"Enter new marks for {s['Name']}: "))
                s['Marks'] = new_marks  # Update the value inside the dictionary
                print(f" Marks updated successfully for {s['Name']}!")
                found = True
                break
                
        if not found:
            print(" Student not found.")
            
    # 5. Delete a student (Demonstrates Loops and the .remove() list method)
    elif choice == '5':
        print("\n--- Delete Student Record ---")
        search_name = input("Enter student name to delete: ").strip().lower()
        found = False
        
        for s in students:
            if s['Name'].lower() == search_name:
                students.remove(s)  # Use list method to remove the target dictionary
                print(f"🗑️ Student '{s['Name']}' deleted successfully!")
                found = True
                break
                
        if not found:
            print(" Student not found.")
            
    # 6. Find the student with the highest marks (Demonstrates custom loop filtering)
    elif choice == '6':
        print("\n--- Top Performing Student ---")
        if not students:
            print("No records available.")
        else:
            highest_student = students[0]  # Assume the first student has the highest marks
            for s in students:
                if s['Marks'] > highest_student['Marks']:  # Condition comparison
                    highest_student = s
            print(f"🏆 Top Student: {highest_student['Name']} with {highest_student['Marks']} Marks.")
            
    # 7. Calculate average marks (Demonstrates math inside loops)
    elif choice == '7':
        print("\n--- Class Average Calculation ---")
        if not students:
            print("No records available. Average is 0.")
        else:
            total_marks = 0
            for s in students:
                total_marks += s['Marks']  # Accumulate values using a loop
            
            average = total_marks / len(students)
            print(f"Total Records: {len(students)}")
            print(f"Class Average Marks: {average:.2f}")
            
    # 8. Exit
    elif choice == '8':
        print("\nExiting program. Goodbye!")
        break
        
    else:
        print("Invalid input! Please enter a number between 1 and 8.")
