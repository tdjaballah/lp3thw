print("Let's do this.")

poem = '''
\tDans dans le vent comme un grain de poussiere,
\tEt dans un rayon de soleil, tout a coup,
\tSe mettre a briller
'''

print("--------")
print(poem)
print("--------")

four = 20 * 2 +10
print(f'This should be four : {four}')

def secret_formula(started):
	jelly_beans = started * 2
	jars = started / 10
	crates = jars / 4
	return jelly_beans, jars, crates

start_point = 10000
print(f'With a starting point of {start_point}:')
print('We get {} beans, {} jars and {} crates'.format(*secret_formula(start_point)))