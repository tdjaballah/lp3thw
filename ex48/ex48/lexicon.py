lexicon = {'direction': ['north', 'south', 'east', 'west'],
		   'verb': ['go', 'kill', 'eat'],
		   'stop': ['the', 'in', 'of'],
		   'noun': ['bear', 'princess', 'sandwich']}

def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def search_word(word):
	n = convert_number(word)
	if n == None:
		for key, values in lexicon.items():
			for value in values:
				if value == word:
					return (key, value)
		return ('error', word)
	else:
		return ('number', n)

def scan(words):
	split_words = words.split(' ')
					
	return [search_word(w) for w in split_words]
		