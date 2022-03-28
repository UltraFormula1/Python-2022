from adventurelib import *

@when("brush teeth")
def brush_teeth():
	say("""
		You squirt a bit too much toothpaste onto your
		brush and dozily jiggle it round your mouth
		""")

@when("watch video")
def watch_video():
	say("""
		You watch a video on Youtube by videogamedunkey
		you find it very funny and rewind a part that you found funny
		""")

@when("listen to music")
def listen_music():
	say("""
		You listen to some Michael Jackson songs
		you listen to his 1987 albumn Bad
		you listen to the whole album and wonder why Leave Me Alone is not on your Vinyl copy
		""")

@when("play gmod")
def gmod():
	say("""
		You play some Garry's Mod on your computer
		you load up the constuct map and creat clones of Dr. Kleiner
		you kill all of the clones with the Tsar Bomba
		your character also dies from the radiation
		your computer crashes and boots back to the login menu                                                                                                                                                                                                                                                      
		""")

def main():
	start()

if __name__ == '__main__':
	main()