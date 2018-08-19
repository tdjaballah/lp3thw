types_of_people = 10
x = f"There are {types_of_people} types of people." # 1

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # 2

print(x)
print(y)

print(f"I said: {x}") # 3
print(f"I also said: '{y}'") # 4

hilarous = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarous)) # 5

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)