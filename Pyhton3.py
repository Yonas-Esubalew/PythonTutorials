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

