states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New York': 'NY',
	'Michigan': 'MI'
}

cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("California's abbreviation is:", states['California'])

print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("California has ", cities[states['California']])

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}.")

print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has {city}.")

print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}.")
	print(f"And {state} has {cities[abbrev]}.")

print('-' * 10)
state = states.get('Texas')

if not state:
	print("Sorry, no Texas down there.")

city = cities.get('TX', 'No TX')
print(f"The city for the state 'TX' is: {city}.")