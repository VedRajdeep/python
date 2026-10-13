
number = int(input("Enter Your Number: "))

if(number):
    result = 1
    for i in range(1 , number +1):
        result *= i
    print (f"the factorial of {number} is {result}")
else:
    print("Enter Valid Value")
