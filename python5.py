
# *args = alllows you to pass multiple non-keye arguments

def display_name(*args):
    for arg  in args:
        print(arg, end= " ")
        
display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

def print_address(**kwargs):
    for key,values in kwargs.items():
        print(F"{key}: {values}")
        
print_address(street="123 fake St.",
              city="Detroil",
              state="MI",
              zip="234534")

print(print_address)

def shipping_label(*args,**kwargs):
    for arg in kwargs:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(value, end=" ")
            
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 fake St.",
               apt="100",
               city="2341")
print()



import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")  
    
count(30, 25)      

def hello(greeting, title,first,last):
    print(F"{greeting} {title}{first}{last}")
hello("hello", "Mr", "Squarepants", "Spongebob")
print("1","2","3","4","6","7","8" ,sep="-")

def get_phone(country,area,first,last):
    return F"{country}-{area}-{first}-{last}"

phone_num  = get_phone(country=234,area=34342,first=2344,last=234)
print(phone_num)

def add(a,b,c):
    return a + b
print(add(1,2,4))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total  
print(add(1,2,3))  

def print_address(**kwargs):
    pass
print_address(street="234", city="@423",state=3434, zip="3434")


def shippnig_level(*args, **kwargs):
    pass

shipping_label("dr", "spongebob", "square", "III",
                street="234234 2fake it",
                apt="100", 
                city="detroit",
                state="MI",
                zip="340890")

# print(shipping_level)

def shiipng_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    print(F"{kwargs.get("street")}")
    print(F'{kwargs.get("city")} "{kwargs.get("atate")}, {kwargs.get("Zip")}' )   
          
shipping_label("dr.", "spongebob", "Squarepants",
srreet="2342 234 34234",
apt="234",
city="detroit"
)   

numbers  = (1,2,3,4,5,6,7,8)

for number in reversed(numbers):
    print(number, end=" ")
           
fruits = {"apple", "orange","banana", "coconut"}

for fruit in (fruits):
    print(fruit)

my_dictionary ={ "A":2,"B": 4,"C": 3,"D": 32}
for key,values in my_dictionary.items():
    print(key, values)

word ="APPLE "
letter = input("guess a letter in the secret word: ")

if  letter not in word:
    print(F"{letter} is not found") 
else: 
     print(F"there is a {letter}")  

students = {"spongebob", "patrick", "sandy"}

student = input("enter the ename of student: ")

if student not in students:
    print(F"{student} was not found")
else:
    print(F"{student} is a student")    

grades = {"sandy": "A", "squidward": "B", "spongebob": "C","patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(F"{student} grade is {grades[student]}")
else:
    print(F"{student} was not found")
        
email = input("Enter the Email: ")

if "@gmail" in email and  "." in email:
    print("Valid Email")
else:
    print("Invalid Email")            


doubles = []
for x in range(1,12):
    doubles.append(x*2)

print(doubles)    

doubles = [x/2 for x in range(1,12)]
triples = [y/ 3 for y in range(1,12)]
squares = [z* z for z in range(1,5)]

print(F"{squares}")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit[3] for fruit in  ["apple", "orange", "banana", "coconut"]]
print(fruits)

numbers = [1,2,-3,-4,-5,6,-7]
positive_num = [num for num in numbers if num >= 0]
negaative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
print(positive_num)
print(negaative_num)
print(even_num)
print(positive_num + even_num)

grades = [34,45,78,56,67,84,23]

passing_grades = [grade for grade in grades if grade>= 60]
print(passing_grades)

def day_of_week(day):
    match day:
        case 1:
            return ("return  its Sunday!")
        case 2:
            return ("Its Monday")
        case 3:
            return ("its thuesday")  
        case 4:
            return ("it is wednesday")   
        case 5:
            return ("its Thursday")
        case 6:
           return ("its firday")
        case 7:
           return ("it is Sturday")   
        case _:
            return ("not a valid day")                
        
print(day_of_week(1))        

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return False
        case "Monday" | "Tuesday" | "wednesday" | "friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))

print(help("math"))
        
import math as m
# from math import e
a,b,c,d = 2,4,5,6
# print(e)
print(m.pi)      
print(m.e ** a)  
print(m.e ** b) 
print(m.e ** c) 
print(m.e ** d) 

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * m.pi *  radius

print(23)

# *args = alllows you to pass multiple non-keye arguments

def display_name(*args):
    for arg  in args:
        print(arg, end= " ")
        
display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

def print_address(**kwargs):
    for key,values in kwargs.items():
        print(F"{key}: {values}")
        
print_address(street="123 fake St.",
              city="Detroil",
              state="MI",
              zip="234534")

print(print_address)

def shipping_label(*args,**kwargs):
    for arg in kwargs:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(value, end=" ")
            
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 fake St.",
               apt="100",
               city="2341")
print()

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
# python DSA 2
print("hello world")

#  
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  

def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  

def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  

def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break

# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
# python DSA 2
print("hello world")

#  strings
word = "hello world"
Single_qoute_word = 'heloo '
print(" the wrold for the about section")
print(F"hello {word} and {Single_qoute_word}")

word = "Heryo wurld"

print(word[2])
print(word[-3])
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[5:2:-1])
print(word[::-2])
# print(word[::2])

a = "hello"
b ="world"
c = a + "  "+ b
print(c)

a = 1
b = "hello"
print(F" {b} {a} {a + 2}")
print ("hell " in "hello world")

#  variable casting
y = int(3.0)
z = float(3)

print(type(int("34")))

s = "hello world"
print(s[5])
print(s[-2])
print(s[1:])
print(s[-2:])

a = 4
b = 4 
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")    
    
if b >33:
    print("b is greater than a")   
elif a == b:
    print("a and b are equal")  
else:
    print("error")    

a = 200
b= 33
if b > a:
    print("b is grater than a")
elif a ==b:
    print( "a and b are equal")  
else:
    print("a is greter than b")     

a  = 233
b =323
c =233
if a> b and c > a:
    print("both conditions are true")
    
else:
    print("none")    

i = 1
while i < 4:
    print(i)
    i += 1 
fruits = ["apple", "banana", "cherry"]   
for x in fruits:
    print(x)
    
adj = ["red", "big","tasty"]    
word = ["shffle", "drawn", "toggle"]
for x in adj:
    for y in word:
        print(x,y)

for x in range(-301,-12):
    print(x)
        
for x in range(6):
    print(x)
for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  

def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  
      

    for y in range(2,10):
    print(y)          

for x in range(32, 2 ,-4):
    print(x)

i=  0 
while i <9:
    i +=1
    if i == 3:
        continue
    print(i)    
for i in range(9):
    if i == 3:
        continue
    print(i)

for i in range(9):
    if i > 3:
        break
    print(i)

i = 2
while i < 9:
    print(i)
    if i ==3:
        break
    i += 1

fruits = ["apple", "banana", "pineapple","orange"]

for fruit  in fruits:
    if fruit == "pineapple":
       print("found pineapple")
       break
else:
#     print("pineapple not found in the list")   

for num in range(10,14):
    for i in range(2,num):
        if num % i == 1:
        print(num)
            break
            
for num in range(10,4):
    for i in range(2,num):
        if num % i == 1:
            print(num)
            break


def my_function(fname):
    fname[0] = "anna"
    print(fname[0] + "rest")
# my_function("mola")    
data= ["emils"]
my_function(data)
print(data[0])

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(6))
print(my_function(3))

x= lambda a :a+20
print(x(5))
x =lambda s, c, v : s+c+v
print(x(32,34,12))
y = lambda name, email, password : name + email - password
print(y(23, 34, 23))

x = 0
while x >= 5:
    print(x)  

x = 0 
while x< 5:
    if x==2:
        continue
    print(x)
    x +=1

arr = [2,3,4,5,]
for i in range(len(arr)):
    i +=2
i =2
while i < len(arr):
    print(arr[i])
    i +=22
print(i)  



import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")  
    
count(30, 25)      

def hello(greeting, title,first,last):
    print(F"{greeting} {title}{first}{last}")
hello("hello", "Mr", "Squarepants", "Spongebob")
print("1","2","3","4","6","7","8" ,sep="-")

def get_phone(country,area,first,last):
    return F"{country}-{area}-{first}-{last}"

phone_num  = get_phone(country=234,area=34342,first=2344,last=234)
print(phone_num)

def add(a,b,c):
    return a + b
print(add(1,2,4))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total  
print(add(1,2,3))  

def print_address(**kwargs):
    pass
print_address(street="234", city="@423",state=3434, zip="3434")


def shippnig_level(*args, **kwargs):
    pass

shipping_label("dr", "spongebob", "square", "III",
                street="234234 2fake it",
                apt="100", 
                city="detroit",
                state="MI",
                zip="340890")

# print(shipping_level)

def shiipng_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    print(F"{kwargs.get("street")}")
    print(F'{kwargs.get("city")} "{kwargs.get("atate")}, {kwargs.get("Zip")}' )   
          
shipping_label("dr.", "spongebob", "Squarepants",
srreet="2342 234 34234",
apt="234",
city="detroit"
)   

numbers  = (1,2,3,4,5,6,7,8)

for number in reversed(numbers):
    print(number, end=" ")
           
fruits = {"apple", "orange","banana", "coconut"}

for fruit in (fruits):
    print(fruit)

my_dictionary ={ "A":2,"B": 4,"C": 3,"D": 32}
for key,values in my_dictionary.items():
    print(key, values)

word ="APPLE "
letter = input("guess a letter in the secret word: ")

if  letter not in word:
    print(F"{letter} is not found") 
else: 
     print(F"there is a {letter}")  

students = {"spongebob", "patrick", "sandy"}

student = input("enter the ename of student: ")

if student not in students:
    print(F"{student} was not found")
else:
    print(F"{student} is a student")    

grades = {"sandy": "A", "squidward": "B", "spongebob": "C","patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(F"{student} grade is {grades[student]}")
else:
    print(F"{student} was not found")
        
email = input("Enter the Email: ")

if "@gmail" in email and  "." in email:
    print("Valid Email")
else:
    print("Invalid Email")            


doubles = []
for x in range(1,12):
    doubles.append(x*2)

print(doubles)    

doubles = [x/2 for x in range(1,12)]
triples = [y/ 3 for y in range(1,12)]
squares = [z* z for z in range(1,5)]

print(F"{squares}")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit[3] for fruit in  ["apple", "orange", "banana", "coconut"]]
print(fruits)

numbers = [1,2,-3,-4,-5,6,-7]
positive_num = [num for num in numbers if num >= 0]
negaative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
print(positive_num)
print(negaative_num)
print(even_num)
print(positive_num + even_num)

grades = [34,45,78,56,67,84,23]

passing_grades = [grade for grade in grades if grade>= 60]
print(passing_grades)

def day_of_week(day):
    match day:
        case 1:
            return ("return  its Sunday!")
        case 2:
            return ("Its Monday")
        case 3:
            return ("its thuesday")  
        case 4:
            return ("it is wednesday")   
        case 5:
            return ("its Thursday")
        case 6:
           return ("its firday")
        case 7:
           return ("it is Sturday")   
        case _:
            return ("not a valid day")                
        
print(day_of_week(1))        

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return False
        case "Monday" | "Tuesday" | "wednesday" | "friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))

print(help("math"))
        
import math as m
# from math import e
a,b,c,d = 2,4,5,6
# print(e)
print(m.pi)      
print(m.e ** a)  
print(m.e ** b) 
print(m.e ** c) 
print(m.e ** d) 

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * m.pi *  radius

print(23)

# *args = alllows you to pass multiple non-keye arguments

def display_name(*args):
    for arg  in args:
        print(arg, end= " ")
        
display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

def print_address(**kwargs):
    for key,values in kwargs.items():
        print(F"{key}: {values}")
        
print_address(street="123 fake St.",
              city="Detroil",
              state="MI",
              zip="234534")

print(print_address)

def shipping_label(*args,**kwargs):
    for arg in kwargs:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(value, end=" ")
            
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 fake St.",
               apt="100",
               city="2341")
print()



import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")  
    
count(30, 25)      

def hello(greeting, title,first,last):
    print(F"{greeting} {title}{first}{last}")
hello("hello", "Mr", "Squarepants", "Spongebob")
print("1","2","3","4","6","7","8" ,sep="-")

def get_phone(country,area,first,last):
    return F"{country}-{area}-{first}-{last}"

phone_num  = get_phone(country=234,area=34342,first=2344,last=234)
print(phone_num)

def add(a,b,c):
    return a + b
print(add(1,2,4))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total  
print(add(1,2,3))  

def print_address(**kwargs):
    pass
print_address(street="234", city="@423",state=3434, zip="3434")


def shippnig_level(*args, **kwargs):
    pass

shipping_label("dr", "spongebob", "square", "III",
                street="234234 2fake it",
                apt="100", 
                city="detroit",
                state="MI",
                zip="340890")

# print(shipping_level)

def shiipng_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    print(F"{kwargs.get("street")}")
    print(F'{kwargs.get("city")} "{kwargs.get("atate")}, {kwargs.get("Zip")}' )   
          
shipping_label("dr.", "spongebob", "Squarepants",
srreet="2342 234 34234",
apt="234",
city="detroit"
)   

numbers  = (1,2,3,4,5,6,7,8)

for number in reversed(numbers):
    print(number, end=" ")
           
fruits = {"apple", "orange","banana", "coconut"}

for fruit in (fruits):
    print(fruit)

my_dictionary ={ "A":2,"B": 4,"C": 3,"D": 32}
for key,values in my_dictionary.items():
    print(key, values)

word ="APPLE "
letter = input("guess a letter in the secret word: ")

if  letter not in word:
    print(F"{letter} is not found") 
else: 
     print(F"there is a {letter}")  

students = {"spongebob", "patrick", "sandy"}

student = input("enter the ename of student: ")

if student not in students:
    print(F"{student} was not found")
else:
    print(F"{student} is a student")    

grades = {"sandy": "A", "squidward": "B", "spongebob": "C","patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(F"{student} grade is {grades[student]}")
else:
    print(F"{student} was not found")
        
email = input("Enter the Email: ")

if "@gmail" in email and  "." in email:
    print("Valid Email")
else:
    print("Invalid Email")            


doubles = []
for x in range(1,12):
    doubles.append(x*2)

print(doubles)    

doubles = [x/2 for x in range(1,12)]
triples = [y/ 3 for y in range(1,12)]
squares = [z* z for z in range(1,5)]

print(F"{squares}")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit[3] for fruit in  ["apple", "orange", "banana", "coconut"]]
print(fruits)

numbers = [1,2,-3,-4,-5,6,-7]
positive_num = [num for num in numbers if num >= 0]
negaative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
print(positive_num)
print(negaative_num)
print(even_num)
print(positive_num + even_num)

grades = [34,45,78,56,67,84,23]

passing_grades = [grade for grade in grades if grade>= 60]
print(passing_grades)

def day_of_week(day):
    match day:
        case 1:
            return ("return  its Sunday!")
        case 2:
            return ("Its Monday")
        case 3:
            return ("its thuesday")  
        case 4:
            return ("it is wednesday")   
        case 5:
            return ("its Thursday")
        case 6:
           return ("its firday")
        case 7:
           return ("it is Sturday")   
        case _:
            return ("not a valid day")                
        
print(day_of_week(1))        

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return False
        case "Monday" | "Tuesday" | "wednesday" | "friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))

print(help("math"))
        
import math as m
# from math import e
a,b,c,d = 2,4,5,6
# print(e)
print(m.pi)      
print(m.e ** a)  
print(m.e ** b) 
print(m.e ** c) 
print(m.e ** d) 

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * m.pi *  radius

print(23)

# *args = alllows you to pass multiple non-keye arguments

def display_name(*args):
    for arg  in args:
        print(arg, end= " ")
        
display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

def print_address(**kwargs):
    for key,values in kwargs.items():
        print(F"{key}: {values}")
        
print_address(street="123 fake St.",
              city="Detroil",
              state="MI",
              zip="234534")

print(print_address)

def shipping_label(*args,**kwargs):
    for arg in kwargs:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(value, end=" ")
            
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 fake St.",
               apt="100",
               city="2341")
print()



import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")  
    
count(30, 25)      

def hello(greeting, title,first,last):
    print(F"{greeting} {title}{first}{last}")
hello("hello", "Mr", "Squarepants", "Spongebob")
print("1","2","3","4","6","7","8" ,sep="-")

def get_phone(country,area,first,last):
    return F"{country}-{area}-{first}-{last}"

phone_num  = get_phone(country=234,area=34342,first=2344,last=234)
print(phone_num)

def add(a,b,c):
    return a + b
print(add(1,2,4))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total  
print(add(1,2,3))  

def print_address(**kwargs):
    pass
print_address(street="234", city="@423",state=3434, zip="3434")


def shippnig_level(*args, **kwargs):
    pass

shipping_label("dr", "spongebob", "square", "III",
                street="234234 2fake it",
                apt="100", 
                city="detroit",
                state="MI",
                zip="340890")

# print(shipping_level)

def shiipng_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    print(F"{kwargs.get("street")}")
    print(F'{kwargs.get("city")} "{kwargs.get("atate")}, {kwargs.get("Zip")}' )   
          
shipping_label("dr.", "spongebob", "Squarepants",
srreet="2342 234 34234",
apt="234",
city="detroit"
)   

numbers  = (1,2,3,4,5,6,7,8)

for number in reversed(numbers):
    print(number, end=" ")
           
fruits = {"apple", "orange","banana", "coconut"}

for fruit in (fruits):
    print(fruit)

my_dictionary ={ "A":2,"B": 4,"C": 3,"D": 32}
for key,values in my_dictionary.items():
    print(key, values)

word ="APPLE "
letter = input("guess a letter in the secret word: ")

if  letter not in word:
    print(F"{letter} is not found") 
else: 
     print(F"there is a {letter}")  

students = {"spongebob", "patrick", "sandy"}

student = input("enter the ename of student: ")

if student not in students:
    print(F"{student} was not found")
else:
    print(F"{student} is a student")    

grades = {"sandy": "A", "squidward": "B", "spongebob": "C","patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(F"{student} grade is {grades[student]}")
else:
    print(F"{student} was not found")
        
email = input("Enter the Email: ")

if "@gmail" in email and  "." in email:
    print("Valid Email")
else:
    print("Invalid Email")            


doubles = []
for x in range(1,12):
    doubles.append(x*2)

print(doubles)    

doubles = [x/2 for x in range(1,12)]
triples = [y/ 3 for y in range(1,12)]
squares = [z* z for z in range(1,5)]

print(F"{squares}")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit[3] for fruit in  ["apple", "orange", "banana", "coconut"]]
print(fruits)

numbers = [1,2,-3,-4,-5,6,-7]
positive_num = [num for num in numbers if num >= 0]
negaative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
print(positive_num)
print(negaative_num)
print(even_num)
print(positive_num + even_num)

grades = [34,45,78,56,67,84,23]

passing_grades = [grade for grade in grades if grade>= 60]
print(passing_grades)

def day_of_week(day):
    match day:
        case 1:
            return ("return  its Sunday!")
        case 2:
            return ("Its Monday")
        case 3:
            return ("its thuesday")  
        case 4:
            return ("it is wednesday")   
        case 5:
            return ("its Thursday")
        case 6:
           return ("its firday")
        case 7:
           return ("it is Sturday")   
        case _:
            return ("not a valid day")                
        
print(day_of_week(1))        

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return False
        case "Monday" | "Tuesday" | "wednesday" | "friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))

print(help("math"))
        
import math as m
# from math import e
a,b,c,d = 2,4,5,6
# print(e)
print(m.pi)      
print(m.e ** a)  
print(m.e ** b) 
print(m.e ** c) 
print(m.e ** d) 

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * m.pi *  radius

print(23)

# *args = alllows you to pass multiple non-keye arguments

def display_name(*args):
    for arg  in args:
        print(arg, end= " ")
        
display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

def print_address(**kwargs):
    for key,values in kwargs.items():
        print(F"{key}: {values}")
        
print_address(street="123 fake St.",
              city="Detroil",
              state="MI",
              zip="234534")

print(print_address)

def shipping_label(*args,**kwargs):
    for arg in kwargs:
        print(arg, end=" ")
    print()
    for value  in kwargs.values():
        print(value, end=" ")
            
shipping_label("Dr.", "Spongebob", "Squarepants", "III", 
               street="123 fake St.",
               apt="100",
               city="2341")
print()



import time
def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("done!")  
    
count(30, 25)      

def hello(greeting, title,first,last):
    print(F"{greeting} {title}{first}{last}")
hello("hello", "Mr", "Squarepants", "Spongebob")
print("1","2","3","4","6","7","8" ,sep="-")

def get_phone(country,area,first,last):
    return F"{country}-{area}-{first}-{last}"

phone_num  = get_phone(country=234,area=34342,first=2344,last=234)
print(phone_num)

def add(a,b,c):
    return a + b
print(add(1,2,4))

def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total  
print(add(1,2,3))  

def print_address(**kwargs):
    pass
print_address(street="234", city="@423",state=3434, zip="3434")


def shippnig_level(*args, **kwargs):
    pass

shipping_label("dr", "spongebob", "square", "III",
                street="234234 2fake it",
                apt="100", 
                city="detroit",
                state="MI",
                zip="340890")

# print(shipping_level)

def shiipng_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    print(F"{kwargs.get("street")}")
    print(F'{kwargs.get("city")} "{kwargs.get("atate")}, {kwargs.get("Zip")}' )   
          
shipping_label("dr.", "spongebob", "Squarepants",
srreet="2342 234 34234",
apt="234",
city="detroit"
)   

numbers  = (1,2,3,4,5,6,7,8)

for number in reversed(numbers):
    print(number, end=" ")
           
fruits = {"apple", "orange","banana", "coconut"}

for fruit in (fruits):
    print(fruit)

my_dictionary ={ "A":2,"B": 4,"C": 3,"D": 32}
for key,values in my_dictionary.items():
    print(key, values)

word ="APPLE "
letter = input("guess a letter in the secret word: ")

if  letter not in word:
    print(F"{letter} is not found") 
else: 
     print(F"there is a {letter}")  

students = {"spongebob", "patrick", "sandy"}

student = input("enter the ename of student: ")

if student not in students:
    print(F"{student} was not found")
else:
    print(F"{student} is a student")    

grades = {"sandy": "A", "squidward": "B", "spongebob": "C","patrick": "D"}

student = input("Enter the name of a student: ")

if student in grades:
    print(F"{student} grade is {grades[student]}")
else:
    print(F"{student} was not found")
        
email = input("Enter the Email: ")

if "@gmail" in email and  "." in email:
    print("Valid Email")
else:
    print("Invalid Email")            


doubles = []
for x in range(1,12):
    doubles.append(x*2)

print(doubles)    

doubles = [x/2 for x in range(1,12)]
triples = [y/ 3 for y in range(1,12)]
squares = [z* z for z in range(1,5)]

print(F"{squares}")

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit[3] for fruit in  ["apple", "orange", "banana", "coconut"]]
print(fruits)

numbers = [1,2,-3,-4,-5,6,-7]
positive_num = [num for num in numbers if num >= 0]
negaative_num = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
print(positive_num)
print(negaative_num)
print(even_num)
print(positive_num + even_num)

grades = [34,45,78,56,67,84,23]

passing_grades = [grade for grade in grades if grade>= 60]
print(passing_grades)

def day_of_week(day):
    match day:
        case 1:
            return ("return  its Sunday!")
        case 2:
            return ("Its Monday")
        case 3:
            return ("its thuesday")  
        case 4:
            return ("it is wednesday")   
        case 5:
            return ("its Thursday")
        case 6:
           return ("its firday")
        case 7:
           return ("it is Sturday")   
        case _:
            return ("not a valid day")                
        
print(day_of_week(1))        

def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return False
        case "Monday" | "Tuesday" | "wednesday" | "friday":
            return False
        case _:
            return False

print(is_weekend("sunday"))

print(help("math"))
        
import math as m
# from math import e
a,b,c,d = 2,4,5,6
# print(e)
print(m.pi)      
print(m.e ** a)  
print(m.e ** b) 
print(m.e ** c) 
print(m.e ** d) 

def square(x):
    return x ** 2
def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * m.pi *  radius

print(23)