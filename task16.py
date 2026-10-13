number = []

for i in range(10):
    x = int(input(f"Enter Number {i + 1}: "))
    number.append(x)

print("your numbers are",number,min(number),max(number))
