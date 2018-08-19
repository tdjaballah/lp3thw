formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("un", "deux", "trois", "quatre"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Parfois, le beau temps me chagrine",
	"Un soleil doux, une brise fine",
	"Le sable du square sur mon jean",
	"Les villes sans mer sont orphelines"))
#Ce n'est pas de moi, mais du lauréat prix poésie ratp 2018

