x = float(input("Enter percentage: "))

if 90 <= x <= 100:
    print("A+")

elif( 80 <= x <=89):
    print("A")

elif( 70 <= x <=79):
    print("B")

elif(60 <= x <=69):
    print("C")

elif(50 <= x <=59):
    print()

elif(40 <= x <=49):
    print()

elif(0 <= x <=39):
    print("fail")

else:
    print("Invalid percentage! Please enter a value between 0 and 100.")