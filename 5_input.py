#1
input("Type in any key and press enter")
#2
input("Type in your name")
#3
input("Now type in your age")
#4
name = input("Type in your name")
#5
age = input("Now type in your age")
#6
movie = input("What is your favorite movie?")
#7
book = input("What is your favorite book?")
#8
adjective = input("Type in an adjective")
#9
noun = input("Type in a noun")
#10
verb = input("type in a verb")
#11
print(f"Hello {name}, I see you're {age} years old, good to meet you!")
print(f"{movie} is a good movie, but I don't think that {book} is a good read, however, I do recommend another book by the same author")
print(f"Your adjective is {adjective}, your noun is {noun} and your verb is {verb}")
#12
user_age = int(input("I need your age again please"))
#13
print(f"You will be {user_age +10} in 10 years")
#14
print(f"You were born in {2022 - user_age}")
#15
apples = int(input("How many apples do you have?"))
#16
friends = int(input("If you aren't a lonely loser, tell me how many friends you have?"))
#17
print(f"You can share {apples//friends} apples between your mates, and have{apples%friends} left over.")
#18
pizza = int(input("How many pizza's would you like?"))
#19
people = int(input("How many people want pizza?"))
#20
print(f"you're friends will each get {pizza*8//friends} slices and have {pizza*8%friends} remaining")
#21
dollars = int(input("How much money do you have?"))
#22
TV = int(input("How much is the TV"))
#23
print(f"You will have {dollars - TV} left after purchasing the TV")
#24
print(f"The TV will be {0.8*TV} while on a 20% off sale")
#25
bitcoin_amount = int(input("How much Bitcoin do you have?"))
#26
bitcoin_value = 64742
#27
print(f"Your bitcoin portfolio is worth {bitcoin_value*bitcoin_amount}.")
#28
weekly_wage = int(input("How much do you earn each week?"))
#29
tax_rate = int(input("What is the current tax rate?"))
#30
print(f"You will take home {weekly_wage*(1-tax_rate)} every week after paying taxes")
#31
book_name = input("Type in the name of a book you've read")
#32
print(book_name.lower())
print(book_name.upper())
print(book_name.title())
#33
number = int(input("Giuve me a number"))
#34
print("book_name"*number)