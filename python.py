#  LESSSON ONE

#  Variables: A container for a value (string, integer, float, boolean)
#  A Variable behaves as if it was the vaue it contains
#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)

#  shoping cart program

foods =[]
prices = []
total = 0


while True:
    food = input("Ener a food to Buy (q to quite): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(F"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART ------")

for food in foods:
    print(food)      
for total in prices:
    total += price

print()
print(F"the total Price of {food} is  ${total}")       


# 2 dimensional List 

grocery = [["apple", "Orange", "banana", "coconut"],["celery", "carrots", "potatoes"], ["chicken", "fish", "tukey","bread"]
]

for collection in grocery:
    for food in collection:
        print(food, end=" ")
    print()    
    
    
    # ceate a telephone number Pad 
    
num_pad = ((1,2,3),(4,5,6),(7,8,9),("*", 0, "#"))
    
for row in num_pad:
    for num in row:
        print(num, end= " ")
    print()   
    
    #  python quiz game
    
questions = ("how many elemnts are in the predic table?: ",
                 "which animal lays the alrgest egg?: ",
                 "what is the most abundadnt gas on athmosphere",
                 "how bones are in the human body?: ",
                 "which planet in the solar system are the hootest?: ")
    
options = (("A. tyu","B. sdf","C. sfs","D.  sdf",),
           ("A.  sdfs","B.  sdfsdf","C. asd","D.  wer",),
           ("A. sdf","B. wer","C. sdfzxc","D. werq",),
           ("A. adxc","B. xcv","C. xcvv","D. asfd",),
           ("A. awef","B. xcvz","C. adfv","D. zxcv",),)

answers = ("D", "A", "C", "B","A")
guesses = []
score =  0 
question_num = 0 

for question in questions:
    print(" -------------------")
    print(question)
    for option in options[question_num]:
        print(option)
guess = input("Enter (A, B, C, D): " ).upper()
guesses.append(guess)    
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")  
else:
    print("Incorrect")  
    print(F"{answers[question_num]} is the correct answer")  
question_num += 1      
print("---------------")
print(" RESULTS ")   
print("---------------")  


print("answer: ", end=" ") 
for answer in answers:
    print(answer, end =" ")  
print()    

print("guesses: ", end=" ") 
for guess in guesses:
    print(guess, end = " ")  
print()    

score  = int(score / len(questions) * 100)

print(F"your score is {score}%")


#  dictionary = a collection of {key: value} pairs ordered and  changeable no duplication

capitals = {
    "USA": "Washington DC",
    "india": "new Delhi",
    "china": " beijing",
    "russia": "Moskow"
}

print(capitals.get("india"))

if capitals.get("japan"):
    print("tha tcapital exists")
else:
    print("that capital doesn't exit")  
    
    
print(capitals.update({"Germany": "berlin"}))  
print(capitals.update({"USA": "Detroit"}))    

capitals.pop("china")
capitals.popitem()
capitals.clear()

key = capitals.keys

print(key)

values = capitals.values()
print(values)

for key, value in capitals.items():
    print(F"{key}: {value}")

#  consesion stand Porgram

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popchorn": 6.00,
    "fries": 2.50,
    "chips": 32,
    "pretzel": 9.0,
    "soda": 90,
    "lemonade": 4.32
}
cart =  []
total =  0

print("-----------MENU---------")
for key, value in menu.items():
    print(F"{key:10}: ${value:.2f}")
print("------------------------")    





while True:
    food = input("Slelect an item (q to quite): ")
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu.get(food)        
    print(food, end= " ")    
        
print(cart)
print(F"total is: ${total:.2f}")


import random

low = 1
high = 100

number = random.randint(low, high)

print(number)


#  Strings

name = "yonas"
food = "pizza"
email = "bro123@gmail.com"
username = "bro code"

print(F"fill the username: {username}")
print(f"hello {name}")
print(f"your email is: {email}")
print(f"you like {food}")

# Integers 
age = 25
quantity = 3
num_of_students = 30
year = 2024


print(F"this is last year {year}")
print(F"you are {age} years old")
print(F"you are buying {quantity} items")
print(F"yoour Class has {num_of_students} Students")


# Float
price = 456.46
gpa = 3.45
distance = 458.89
pi = 3.14


print(F" the exact value of pi is: {pi}")
print(F"your GPA Is: {gpa}")
print(F"the price is is ${price}")
print(F"the distance is {distance}km")

# Boolean

for_sale = True
is_online = False
is_admin = True

if is_admin:
    print("this person is Admin")
else:
    print("its Not Admin")    

if for_sale:
    print("that item is for sale")
else:
    print("that item is not Available")       
    
if is_online:
    print("you are online")
else:
    print("you are offline")        
    
    
# LESSON TWO 

#  Typecasting: the process of a variable from one data type to another str(), int(), float(), bool()


name = ""
age = 30
gpa = 2.5
is_student = True


name = bool(name)

print(name)
print(type(name))
print(type(is_student))

gpa = int(2.5)

gpa += 1
print(gpa)
print(type(gpa))

age = float(30)

print(type(age))
print(age)


age = str(25)

age += "1"
print(age)
print(F"the value is same but diffrent type {type(age)}")



# LESSON THREE

#  input() : A function that prompts the user to enter data   Returns the entered data as a String.

name = input("What is your name?: ")
# simple code
age = int(input("how old are you?: "))

# Typecasting
age = int(age)
age = age + 1

print(F"Hello {name}!")
print("HAPPY BIRTH DAY!")
print(F"you are {age} years Old!")


#  Exercisse 1 Rectangle Area Calc
width = int(input("enter the width of REC: "))
length = int(input("Enter The Length OF REC: "))

Area = length * width
print(F"The Area Is {Area}cm^2")
print(type(Area))
 

#  Exercise 2 Shopping Cart program

item = input("please enter the item: ")
price = float(input("please enter the price: "))
quantity = int(input("Please enter the qty: "))

total = price * quantity

print(F"total of the item Cost = {total}")



# Eexercise THREE
# Madlibs Game
#  word game Where you create A Story
# by filling blanks with random words

Country_name = input("please fill Contry: ")
verb0 = input("please enter the verb: ")
verb1 = input("please fill verb3: ")
noun = input("please fill the 4: ")
verb2 = input("enter the Number: ")
verb3 = input("the success: ")
divide = input("please input Divided: ")
last = input("please fill divide: ")


print(F"In the eighteen century {Country_name} mathematician lapse who also {verb0} gambling defind the {verb1} of an {noun} as the {verb2} of {verb3} outcomes {divide} by number of possible {last}.")
# In eighteenth century 1French mathematician 
# Laplace who also 2studied gambling defined the 
# 3probability of an 4event as the 5number of 
# 6successful outcomes 7divided by number of 
# possible 8outcomes.


# Augmented Assignment Operator

friends = 13
friends = friends + 1
# Below are Augmented Assignment Operator 
friends += 1
print(friends)
friends -= 1
print(friends)
friends *= 5
print(friends)
friends /= 4
print(friends)
friends = friends ** 2
print(friends)

remainder = friends % 4
print(remainder)


# Some Basic Functions
x = 3.14
y = -4
z = 5

result = round(x)
result = abs(y)
result = pow(3, 4)
result = max(x,y,z)
result = min(x,y,z)
print(result)


import math
print(math.pi)
print(math.e)

x = -9.1
# result = math.sqrt(x)
print(result)
result = math.ceil(x)
# result = math.floor(x)

print(result)
 
 
#  Calculate Circumference of Circle
import math

radius = float(input("please enter the radius: "))
circumference = 2 * math.pi * radius
print(F" The Circumference is: {round(circumference)}")


#  Area Of A circle

import math

radius = float(input("plase input the radius: "))
area = math.pi * pow(radius, 2)
print(F"the Area of a circle is: {round(area)}")

#  Area of Hypotnus of Aright Angle Triangle

import math

a = float(input("please enter the height: "))
b = float(input("please enter the width: "))
c = math.sqrt(pow(a,2) + pow(b,2))
x = round(c, 3)
print(F"the Hypotnus of the Triangle is: {x}")
  
  