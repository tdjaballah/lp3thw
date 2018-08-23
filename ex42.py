## Animal is-a object
class Animal(object):
	pass

## Dog is-a animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object the (object) thing is unnecessary
class Person():

	def __init__(self, name):
		## Person has-a name
		self.name = name
		## Person has-a pet
		self.pet = None

## Employee is-a person
class Employee(Person):

	def __init__(self, name, salary):
		super().__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish():
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## Halibut is-a fish
class Halibut(Fish):
	pass

##rover is an instance of Dog
rover = Dog("Rover")

##satan is an intance of Cat
satan = Cat("Satan")

##mary is an instance of Person
mary = Person("Mary")

##mary has-a attribute pet which is satan
mary.pet = satan

##franck is an instance of Employee
franck = Employee("Franck", 20000)

##franck has-a attribute which is rover
franck.pet = rover

##flipper is an instance of Figh
flipper = Fish()

##crouse is an instance of Salmon
crouse = Salmon()

##harry is an instance of Halibut
harry = Halibut()
