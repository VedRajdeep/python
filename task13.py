number = input("Enter number between 1 to 50: ")
ending_number = int(number)

total_sum = sum(range(1,ending_number + 1))
if(ending_number < 50):
    print(f"Ending number is {ending_number} and {total_sum}")
else:
    print("Enter Valid Vale")