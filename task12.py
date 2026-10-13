user_input = int(input("Enter a number btween 1 to 10 print Table: "))

if user_input in range(1,11):
    for i in range(1,11):
        print(f"{user_input} x {i} = {user_input * i}")
else:
    print("Enter valid number")