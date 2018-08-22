print("""You enter a dark room with two doors.
	Do you go thourgh door #1 or #2?""")

prompt = ">\t"
door = input(prompt)

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")

	bear = input(prompt)

	if bear == "1":
		print("The bear eats your face off. Good job!")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")
	else:
		print(f"Well doing {bear} is probably better.")
		print("Bear runs away.")

elif door == "2":
	print("You stare into the endless abyss at Chatelet Les Halles.")
	print("1. Visiting the nike store.")
	print("2. Buying metro ticket.")
	print("3. Drinking beer at the pub.")

	activity = input(prompt)

	if activity == "1" or activity == "2":
		print("You save your day. Good job!")
	else:
		print("You're drunk and can't retrieve home. Well done!")

else:
	print("You stumble around and fall on a knife and die. Well done!")