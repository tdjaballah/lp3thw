class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

happy_bday = Song(["Joyeux anniversaire !", "Joyeux anniversaire Thibault!"])

far_from_any_road = Song(["From the dusty mesa", "Her looming shadow grows", "Hidden in the branches of the poison creosote"])

happy_bday.sing_me_a_song()

far_from_any_road.sing_me_a_song()

print(far_from_any_road.lyrics)