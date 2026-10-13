number = int(input("Enter Number: "))
if(number > 1):
    for i in range(2, number):
        if(number % i == 0):
            print("Its Not a prime number")
            break
    else:
        print("Its a Prime number")
else:
    print("not a prime number")
