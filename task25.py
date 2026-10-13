x = ("Ved",21,"Data Science","Ahmedabad")
print(f"Name:{x[0]}")
print(f"Age:{x[1]}")
print(f"Course:{x[2]}")
print(f"City:{x[3]}")
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)