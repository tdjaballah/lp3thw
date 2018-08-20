def add(a, b):
	print(f"ADDing {a} + {b}")
	return a + b

def substract(a,b):
	print(f"SUBSTRACT {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"MULTIPLY {a} * {b}")
	return a * b

def divide(a, b):
	print(f"DIVIDE {a} / {b}")
	return a / b

age = add(10,5)
height = multiply(40, 2)
weight = divide(1003, 8)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}")