Name = str(input("Student Name: "))
Roll = int(input("Roll Number: "))

Maths = int(input("Enter Maths Marks: "))
Sci = int(input("Enter Sci Marks: "))
Eng = int(input("Enter Eng Marks: "))
Hindi = int(input("Enter Hindi Marks: "))
Guj = int(input("Enter Guj Marks: "))

Total = sum([Maths]+[Sci]+[Eng]+[Hindi]+[Guj])
print(Total)

Percentage = Total/500*100
print(Percentage)

if(90<= Percentage <=100):
    print("A+")
elif(80<= Percentage <=89):
    print("A")
elif(70<= Percentage <=79):
    print("B")
elif(60<= Percentage <=69):
    print("C")
elif(50<= Percentage <=59):
    print("D")
else:
    print("Fail")

if(Percentage >= 40):
    print("Pass")

