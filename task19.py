total_number = int(input("How many numbers you want to enter?: "))
number= []

for i in range(10):
    x = int(input(f"Enter number {i + 1}: "))
    number.append(x)

total = sum(number)
print(total)

Average = total/total_number
print(Average)

minimum = min(number)
print(minimum)

maximum = max(number)
print(maximum)

for x in number: 
    if(x > 0):
        print(f" Positive number {x}")
    elif(x < 0):
        print(f" Negative number {x}")
    elif(x == 0):
        print(f" Zero {x}")

for x in number:
    if(x % 2 == 0):
        print(f"Even {x}")
    else:
        print(f"Odd {x}") 