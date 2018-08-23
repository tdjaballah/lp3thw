try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My exercise 46',
	'author': 'Thibault Djaballah',
	'url': 'https://github.com/thibault-djaballah/lp3thw',
	'author_email':'myemail@hotmail.fr',
	'version': '0.1',
	'intall_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'ex46'
}

setup(**config)