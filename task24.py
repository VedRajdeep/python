number = [12,23,34,56,23,34,34]
name = ["Alice","Joey","Bob","Anny","Many"]

squares = [x**2 for x in range(1,11)]
Even = [x for x in range(1,51) if x % 2 == 0]
greater_then_50 = [x for x in number if x > 50]
name_string_A = [z for z in name if z.startswith(('A','a'))]

print(f"Squares of numbers from 1 to 10.{squares}")
print(f"Even numbers from 1 to 50.{Even}")
print(f"Numbers greater than 50 from a given list.{greater_then_50}")
print(f"Names starting with the letter A.{name_string_A}")