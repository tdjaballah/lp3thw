import sys

import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

script, input_encoding, error = sys.argv

print(sys.getdefaultencoding())
def main(language_file, encoding, errors):
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<--->", cooked_string)


languages = open("ex23_languages.txt", encoding='utf-8')

main(languages, input_encoding, error)