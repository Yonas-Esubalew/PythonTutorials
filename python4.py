import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
import random 
# number = random.randint(1,20)
number = random.random()
# print(number)
options = ("bread", "paper", "scissor")
option = random.choice(options)
cards = ["2","@","4","4","6","7","8","8"]

random.shuffle(cards)
print(cards)


# python number Guessing Game

low_num =1
high_num = 100
answer = random.randint(low_num,high_num)
guesses = 0
is_running = True

print("Pyhton Number Guessing Game")
print(F"select the number between {low_num} and {high_num}")
# print(answer)

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print("that number is out of range")
    else:
        print("Invalid guess")
        print(F"Select a number between {low_num}  and{high_num}")


import random

options = ("rock", "paper", "scissors")
running =True

while running:
    player = None
    computer = random.choice(options)


    while player not in options:
        player = input("Enter a Choice (rock, paper, scissors: )")

# print(F"player: {player}")
# print(F"computer: {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissors":
        print("you win")
    elif player == "paper" and computer =="rock":
        print("you Win")
    elif player == "scissors" and computer == 'paper':
        print("You Win")  
    else:
        print("You Lose!!")  
    
    play_again = input("play again? (y/n): ").lower()            

    if not play_again == "y":
        running = False
    
    print("Thanks For Playing!")    


import random
# unicode character
# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"),
}

dice = []
total = 0
num_of_dice = int(input("how many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))
    
 
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)  
    
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="") 
    print()    
           
for die in dice:
    total += die     
print(F"the total is {total}")


# function = a block of reusable code
#    place () after the function name to invoke it

def happy_brithday(age,name):
    print(F"Happy birthday to {name}")
    print(F"you are {age} old")
    print("happy birthday")
    print()
    
    
happy_brithday("Bro", 23)
happy_brithday("Steve",34)
happy_brithday("Joe",23)

def display_invoice(username, amount, due_date):
    print(F"Hello {username}")
    print(F"your bill of ${amount:.2f} is due: {due_date}")
    
display_invoice("yonas", 30.4653, "01/01")    

# return = statement used to endva function and send a result back to the caller
def add(x,y):
    z = x + y
    return z

def substract(x,y):
    z = x - y
    return z

def multiply(x,y):
    z = x * y
    return z

def divide(x,y):
    z = x / y
    return z

print(add(2,4))
print(substract(32,34))
print(multiply(23,34))
print(divide(234,34))


def create_name(first, last):
    first = first.upper()
    last = last.upper()
    return first + " " + last

full_name = create_name("bro", "code")

print(full_name)

def net_price(list_price, discount=0, tax =0.05):
    return list_price * (1- discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 23, 45))

import time

def count(end, start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")  
count(10, 4)      

def hello(greeting, title, first,last):
    print(F"{greeting} {title} {first}{last}")
    
hello("hello","Mr.", "Squrepants", "Spongebob") 

for x in range(1, 23, 4):
    print(x, end=" ")   

print("1","2","3","4","5","6", sep="-")

def get_phone(country, area, first, last):
    return F"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=12,area=12,first=23,last=3)

print(phone_num)

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,45,3))    
