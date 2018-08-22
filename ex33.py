global i 

i = 0
numbers = []

cond = (i < 6)

def iter(i, list):
	print(f'At the top i is {i}.')
	list.append(i)
	print("Numbers now : {}".format(list))

while cond :
	iter(i, numbers)
	i += 1
	cond = (i < 6)
	print(f"Now i is {i}.")

print("The numbers : {}".format(numbers))