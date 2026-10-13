##input##
Name = str(input("Enter your name: "))
Age = int(input("Enter Your Age: "))
Height = float(input("Enter Your Hight: "))
Marks = int(input("Enter marks: "))

##conversion##
text = f" hii{Name}\n Your Age is {Age}\n Your Hight is {Height}\n and Your makrs are {Marks} "
print(text)
##the values and their types.##
print(Name,type(Name))

print(Age,type(Age))

print(Height,type(Height))

print(Marks,type(Marks))

print("After 5 years your age will be",int(Age+5))
