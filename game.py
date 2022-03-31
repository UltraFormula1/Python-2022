#######################################
#IMPORTS
#######################################
from adventurelib import *

#######################################
#DEFINE ROOMS
#######################################
Room.items = Bag()

entrance = Room("You are standing in a small room with a few potted plants on tables, and a picture of Weber hanging above. There is a newspaper lying next to the plant that appears to be opened on a specific page")
hall_1 = Room("You are at the start of a long hallway, there are exits around you on 4 sides including the way you just went. A massive shelf is to the side of you full of folders of information about the company. You see a segment labelled 'Employees' full of files.")
hall_2 = Room("You are now standing at the end of the hallway with 3 exits around you. One of the doors are locked, this could possibly lead to the bathroom. what apperars to be an ID card is hiding underneath the carpet you are standing on")
dining_room = Room("You are now in the dining room, and in the corner is the the brand new luxury of the TV. You have only seen these in the most rich of houses. There is a coffee table which appears to be on an angle about to fall over, maybe there is a body underneath there. On the coffee table is a phone that is looping some unresponded calls from 3 people. There is also a small, long yet thin object on the ground")
bedroom = Room("You make your way over to the bedroom of Weber, and already there is a lot to look at. The bed is neatly tidied, the bookshelf is all ordered, and all seems orderly. But as you start to investigate the bookshelf, 2 books fall off that both could provide information.")
bathroom = Room("After you unlock the bathroom door, you notice that this seems to be the one room where the murderer was sloppy in hiding any clues that they might've created. In the sink there is some hair near a razor, indicating someone shaved here. Also there is a soaked piece of paper in the toilet")
kitchen = Room("You make into the kitchen, and the floor is full of broken glass and open drawers. However one drawer labelled knives is closed, leading you to wonder what could be in it")
laundry_room = Room("When you make it to the laundry room, it is so dark that you can't use your notebook, however you can make out some shape on the floor under some unhung clothes, there also seems to be another id card inside one of the washing machines")
balcony = Room("You arrive on the apartment balcony and you get a good view over Detroit, sirens whail in the distance and gunshots fire as you see your fellow officers on another arrest. You also see a medium sized brown haired person limp by and he looks up at Weber's old apartment for a second with a suspicious look. You can't find any clues here.")
#######################################
#DEFINE CONNECTIONS
#######################################
entrance.east = hall_1
hall_1.east = hall_2
hall_1.north = bedroom
hall_1.south = dining_room
hall_2.south = kitchen
dining_room.east = kitchen
kitchen.south = laundry_room
dining_room.south = balcony

#######################################
#DEFINE ITEMS
#######################################
newspaper = Item("news", "newspaper", "paper", "Detroit Free Press")
newspaper.description = "You pick up the newspaper and scan through the headlines. Packard Motor Car Company celebrates 10 years of management by Edward Weber as sales pass Chrysler for the first time in 2 years"
knife = Item("knife", "bloody knife", "knife with blood")
knife.description = "You open the drawer and grab a pocket knife stashed in it, it is full of blood of course, but it appears that it has been mostly smeared off by some kind of cloth to make it look like a normal knife. Unfortunately for the suspect, there were no other knives in that drawer to disguise it."
id_card = Item("id card", "identification card", "id", "profile card", "card")
id_card.description = "You pick up the card and you can see it's obviously forged as it's made of the wrong material. The name printed on it is Barry Powers, you know that this is a name used commonly by criminals, and the only two who have a record of using it are Geroge Chambers and Ben Rowe."
diary = Item("diary", "Weber's Diary", "diary book", "journal")
diary.description = "You pck up the diary and find the last entry. It reads 'I have met up with the representative from Chrysler, he was a medium weight brown haired man who seemed to have a lot of trouble walking. He seemed like an alright chap until we had an arguement about a deal we tried to arrange with the two companies.' The page goes blank after that. Ben Rowe and Harvey Gardner both seem to match the description, but you know that it could only be Gardner being that he works for Ford."
book = Item("book", "company book", "Packard book", "Chrysler book")
book.description = "You pick up and read the book about Packard and it's history. The book lists two people under the names of B Rowe and G Chanmbers"
hair = Item("hair", "razor", "shavings", "shaved hair")
hair.description = "You investigate the hair shavings and find that they are of a light brown color, prbably closest to Harvey Gardner, but the lighting in the bathroom makes it hard to tell."
folder = Item("file", "files", "employee lst")
folder.description = "You browse through the employee list, nothing seems to be suspicious."
id_card2 = Item("second card", "id card 2", "second id card", "2nd id card", "card 2", "id card", "card")
id_card2.description = "The card is very wet and soggy, the washing liquid has almost detroyed the thing. But you attempt to read what the id card says anyway, and it appears to have another fake name. This could mean that the suspect has multiple backup id cards at the ready."
key = Item("object", "mysterious item", "item", "key", "bathroom key", "mysterious object", "unknown item")
key.description = "This must be an important key, keep it with you incase you find a use for it!"


#######################################
#DEFINE BAG
#######################################

Room.items = Bag()

#######################################
#ADD IETMS TO BAG
#######################################
entrance.items.add(newspaper)
hall_1.items.add(folder)
hall_2.items.add(id_card)
bathroom.items.add(hair)
kitchen.items.add(knife)
bedroom.items.add(book)
bedroom.items.add(diary)
laundry_room.items.add(id_card2)
laundry_room.items.add(key)

#######################################
#DEINIE VARIABLES
#######################################

current_room = entrance
inventory = Bag()
body_searched = False
used_key = False
tv_watched = False
phone_listened = False
phone_ringing = False
secret_word = False

#######################################
#BINDS (e.g "@when(look)")
#######################################


@when("check notes")
@when("check notebook")
@when("read notebook")
@when("read notes")
def notes():
	if current_room == laundry_room:
		print("You can't read your notes here.")
	else:
		print("Notes: Harvey Gardner is a 25 year old brown haired man of medium size, with a large moustache and is currently working at rival company Chrysler. Benjamine Rowe is a 37 year old that looks similar to Gardner, but has a smaller moustache, and has a criminal activity, however, he works for Packard. George 'Youth' Chambers also works for the company, but he is a 19 year old criminal with black hair and no facial hair.")


@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")
	if phone_ringing:
		print("you can hear the phone ringing")


@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
def get_item(item):
	global phone_ringing
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
		print(t.description)
		if t == knife:
			current_room.description = ("You make into the kitchen, and the floor is full of broken glass and open drawers.")
		if t == newspaper:
			current_room.description = ("You are standing in a small room with a few potted plants on tables, and a picture of Weber hanging above.")
		if t == id_card:
			current_room.description = ("You are now standing at the end of the hallway with 3 exits around you. One of the doors are locked, this could possibly lead to the bathroom.")
		if "book" in inventory or "diary" in inventory and current_room == bedroom:
			current_room.description = ("You make your way over to the bedroom of Weber, and already there is a lot to look at. The bed is neatly tidied, the bookshelf is all ordered, and all seems orderly.")
		if t == folder:
			current_room.description = ("You are at the start of a long hallway, there are exits around you on 4 sides including the way you just went. A massive shelf is to the side of you full of folders of information about the company.")
		if t == hair:
			current_room.description = ("You enter the bathroom")
		if t == id_card2:
			current_room.description = ("When you make it to the laundry room, it is so dark that you can't use your notebook, however you can make out some shape on the floor under some unhung clothes")
		if t == key:
			current_room.description = ("When you make it to the laundry room, it is so dark that you can't use your notebook. There seems to be another id card inside one of the washing machines")
		if "key" in inventory and "id card 2" in inventory and current_room == laundry_room:
			current_room.description = ("When you make it to the laundry room, it is so dark that you can't use your notebook.")
	else:
		print(f"You don't see an {item}")


	if len(inventory) >= 5:
		print("The phone starts ringing")
		phone_ringing = True


@when("inventory")
def check_inventory():
	print("you are carrying")
	for item in inventory:
		print(item)


@when("search body")
@when("look at body")
@when("search man")
@when("search table")
@when("search coffee table")
def search_body():
	global body_searched
	if current_room == dining_room and body_searched == False:
		print("you search the body of Weber, and find that he has been stabbed in the gut multiple times, his skull also seems to be cracked and very fragille")
		body_searched = True
	elif current_room == dining_room and body_searched == True:
		print("You already searched the body")
	else:
		print("There is nothing here")


@when("watch tv")
@when("watch television")
def watch_tv():
	global tv_watched
	if current_room == dining_room and tv_watched == False:
		print("You turn on the tv as a news program from NBC begins, they are reporting on the murder of Weber, and state tha all that is known so far about the suspect is that they had some sort of association to a car company")
		tv_watched = True
	elif current_room == dining_room and tv_watched == True:
		print("You turn on the tv again, and it just seems to be another rerun of some kind of western movie")
	else:
		print("There is no TV here!")


@when("listen to phone")
@when("listen to telephone")
@when("listen to answerphone")
def listen_phone():
	global phone_listened
	if phone_ringing and current_room==dining_room and phone_listened == True:
		print("Ah, good to see you. We are running out of time on this case, and we need to know who actually killed Weber. You'd better have an answer boy! Who did it?")
		answer = input(">")
		while True:
			if answer.lower() == "benjamine rowe":
				print("Alright, I'll look into it... \nYes, it does seem like he is the most likely suspect, thank you for giving us the clues neccesary to catch him! How about we go grab some doughnuts for the squad later, eh? \nYou win! But did you find the secret word?")
				break
			elif answer.lower() == "george chambers" or answer.lower() == "harvey gardner":
				print("Okay I'll look into it... \n Um, pal? It looks like your data doesn't match the suspect that you have identified, but we don't have enough time for any more bulshit gueses! You're fired! \nYou lose")
				break
			elif answer.lower() == "benjamine rowe" and secret_word == True:
				say("""
					The Beatles Get Back

					Jo Jo was a man who thought he was a loner
					But he knew it couldn't last
					Jo Jo left his home in Tucson, Arizona
					For some California grass

					Get back, get back
					Get back to where you once belonged
					Get back, get back
					Get back to where you once belonged
					Get back Jo Jo
					Go home

					Get back, get back
					Get back to where you once belonged
					Get back, get back
					Back to where you once belonged
					Get back, Jo

					Sweet Loretta Martin thought she was a woman
					But she was another man
					All the girls around her say she's got it coming
					But she gets it while she can

					Oh, get back, get back
					Get back to where you once belonged
					Get back, get back
					Get back to where you once belonged
					Get back, Loretta

					Go home
					Oh, get back, get back
					Get back to where you once belonged
					Get back, get back
					Get back to where you once belonged

					Get back
					Woo...

					I'd like to say thank you on behalf of the group and ourselves, and I hope we've passed the audition!
					""")
				break
			else:
				print("Are you drunk or something, kiddo? That is NOT, and I repeat NOT a suspect!")
		quit()

	if current_room == dining_room and phone_listened == False:
		print("You listen to the answerphones, two of them are just normal employees discussing about work and are not suspects, but the third answerphone is a heavily distorted message that is too distorted to listen to, but you can just make out the voice of Ben Rowe")
		tv_watched = True
	elif current_room == dining_room and phone_listened == True:
		print("The phone doesn't respond.")
	else:
		primt("There is no phone here!")


@when("use ITEM")
def use(item):
	if item == "key" and current_room == hall_2:
		print("You use the key and the door opens with a squeak, probably needs to be oiled")
		print("You can now go to the bathroom in the north")
		used_key = True
		hall_2.north = bathroom
	else:
		print("You can't use that here")

@when("get back")
def get_back():
	print("congratulations, you typed in the secret phrase!")
	secret_word = True


#######################################
#MAIN FUNCTION
#######################################
def main():
	print("Detroit Noir Mystery \nThe year is 1949, shortly after the war. You are a failing detective working for the Detroit Police Depatment and you are sent to a crime scene to investigate the murder of the owner of the Packard car company, Edward Weber, on the 13th of May. The murder took place at 7:00PM shortly after he returned to his home after a cerimonial dinner. The suspect has done well to hide their tracks, although some witnesses have lead to the police identifying three potential suspects. Harvey Gardner is a 25 year old brown haired man of medium size, with a large moustache and is currently working at rival company Chrysler. Benjamine Rowe is a 37 year old that looks similar to Gardner, but has a smaller moustache, and has a criminal activity, however, he works for Packard. George 'Youth' Chambers also works for the company, but he is a 19 year old criminal with black hair and no facial hair. You hope that this investigation will be your big break and will help you be recognised by the police for being the best of the best. But you only have a limited time to investigate the crime scene before the police base calls back, and you have to make the decision as to who killed Weber, one wrong call and you could be fired. \nYou make your way to the apartment...")
	print(current_room)
	start()
	#start the main loop

main()