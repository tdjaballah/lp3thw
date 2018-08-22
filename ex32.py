the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
changes = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for n in the_count:
	print(f"This is count {n}.")

for fruit in fruits:
	print("The fruit is {}".format(fruit))

for i in changes:
	print(f"I got {i}.")

elements = []

for i in range(0, 6):
	print(f"Adding {i} to the list.")
	elements.append(i)

for i in elements:
	print(f"List element: {i}.")

elements = []

print(f"Adding all elements with one-liner.")
elements.extend(range(0,6))

for i in elements:
	print(f"New list element: {i}.")
