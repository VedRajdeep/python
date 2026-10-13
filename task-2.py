##name entry##
name = input("Enter your name:  ")
txt = f"hello  {name}"
print(txt)

##marks Entery##
Python = int(input("Enter Python Makrs: "))
Mathematics = int(input("Enter Mathematics Marks: "))
Database = int(input("Enter Database Makrs: "))
Statistics = int(input("Enter Statistics Makrs: "))
Computer = int(input("Enter Computer Science Makrs: "))

##Total##
total = sum([Python, Mathematics, Database, Statistics ,Computer],100)

##Averge##
Average = total/5

Percentage = total/500*100

print(total)
print(Average)
print(Percentage)