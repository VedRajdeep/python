number = []

for i in range(10):
    x = int(input(f"Enter Number {i + 1}: "))
    number.append(x)

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