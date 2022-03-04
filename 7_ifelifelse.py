#1
ice_cream = int(input("How many ice creams do you have?"))
if ice_cream > 20:
	print("There isn't enough ice cream in stock right now")
#2
distance = int(input("How far do you intend to travel? (KM)"))
if distance > 200:
	print("You might need to refuel during the trip!")
#3
age = int(input("How old are you?"))
if age >= 18:
	print("You are now an adult, congrats!")
else:
	print("You are a minor")
#4
movie = input("What is your favorite movie?")
if movie.lower() == "megamind":
	print("You have a big brain, and excellent taste")
else:
	print("Come on man, we all know Megamind is a masterpiece! It was obviously made by a big brain!")
#5
darth = input("Have you ever heard the tragedy of Darth Plageus the Wise?")
if darth.lower() == "no":
	print("I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
elif darth.lower() == "yes":
	print("Good on you")
else:
	print("Oh, you must be a fan?")
#6
director = input("Who directed Forrest Gump?")
if director.lower() == "robert zemeckis":
	print("corect!")
else:
	print("Wrong, Robert Zemeckis directed the film.")
#7
score = 0
q1 = input("Who was the drummer in the Beatles?")
if q1.lower() == "ringo starr":
	print("Correct!")
	score = score + 1
else:
	print("WRONG")
q2 = int(input("What year did Atlanta, Georgia host the Olympics?"))
if q2 == 1996:
	print("correct")
	score = score + 1
else:
	print("WRONG")
q3 = input("Which TF2 class runs the fastest and has the ability to double jump?")
if q3.lower() == "scout":
	print("correct")
	score = score + 1
elif q3.lower() == "soldier" or q3.lower() == "engineer" or q3.lower() == "pyro" or q3.lower() == "demoman" or q3.lower() == "heavy" or q3.lower() == "sniper" or q3.lower() == "medic" or q3.lower() == "spy":
	print("Wrong class")
else:
	print("WRONG! That is not a TF2 class!")
q4 = input("Which album lead to Michael Jackson\'s last world tour?")
if q4.lower() == "history":
	print("Correct")
	score = score + 1
elif q4.lower() == "off the wall" or q4.lower() == "thriller" or q4.lower() == "bad" or q4.lower() == "dangerous" or q4.lower() == "blood on the dance floor" or q4.lower() == "invincible" or q4.lower() == "xscape":
	print("Wrong MJ album!")
else:
	print("WRONG. That was not an MJ album!")
q5 = int(input("What year did Daffy Duck first appear in a Looney Tunes short?"))
if q5 == 1937:
	print("Correct!")
	score = score + 1
else:
	print("You\'re Despicable!")
print(f"you're total score is {score}")