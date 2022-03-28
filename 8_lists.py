#1
Fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(Fibonacci)
#2
fruit = ['apple', 'banana', 'mandarin', 'grape', 'watermelon']
print(fruit)
#3
Youtubers = ['videogamedunkey', 'Steven He', 'The Detail', 'AntDude', 'The Act Man', 'Scott The Woz']
print(Youtubers)
#4
songs = []
songs.append('Michael Jackson - Bad')
songs.append('The Beatles - Get Back')
songs.append('Michael Jackson - Smooth Criminal')
songs.append('Gorillaz - Feel Good Inc.')
songs.append('The Beatles - Abbey Road Medley')
print(songs)
#5
books = []
books.append(input("Type in a book"))
books.append(input("Type in a 2nd book"))
books.append(input("Type in a 3rd book"))
books.append(input("Type in a 4th book"))
books.append(input("Type in a 5th book"))
books.sort()
print(books)
#6
pizza_toppings = []
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
pizza_toppings.append(input("Type in a pizza topping and press enter"))
if pizza_toppings[-1] == "":
	pizza_toppings.pop()
print(pizza_toppings)
#7
fruits = ['apple', 'banana', 'mandarin', 'grape', 'watermelon']
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
fruits.append(input("Type in a fruit"))
if fruits.lower([-1]) == "apple" or fruits.lower([-1]) == "banana" or fruits.lower([-1]) == "grape" or fruits.lower([-1]) == "mandarin" or fruits.lower([-1]) == "watermelon":
	fruits.pop()
	print("That is already in the list, dumbass")
print(fruits)
#8
names = ['John', 'Paul', 'George', 'Ringo', 'Michael']
names.sort()
print(names)
names.reverse()
print(names)
#9
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
prime.reverse()
print(prime)
print("The length of this list is", len(prime))
#10
verbs = ['tell', 'show', 'think', 'walk', 'eat', 'run', 'accept', 'die', 'dry']
verbs.sort()
print(verbs)