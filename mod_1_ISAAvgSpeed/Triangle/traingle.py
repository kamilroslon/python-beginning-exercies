import math

a = input("Provide a:")
b = input("Provide b:")

casted_a = float(a)
casted_b = float(b)

c = math.sqrt(math.pow(casted_a,2) + math.pow(casted_b, 2))

print("c equals:", c)