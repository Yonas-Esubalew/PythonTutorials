#  IF = Do Some Code Only IF Some Conditon Is True
#  Else Do Something Else

age = int(input("Enter Your Age: "))

if age == 18:
    print("this is adult")
elif age < 0:
    print("Not Exit on Earth")   
elif age > 100:
    print("you are old to signup")     
else:
    print("this is Child")    
    
    
    
response = input("Would you like Food? (Y/N): ")    

if response == "Y":
    print("have Some Food")
else:
    print("no food for you!")    
    
    
name =  input("Enter your name: ")
if name == "":
    print("please fill the name!")
else:
    print(F"hello {name}")  
  
  
    #  for Boolean value
    
for_sale = False

if for_sale:
    print("this item is not For Sale")  
else:
    print("This Item Was Not For Sale")   
    
is_online = True       
    
if is_online:
    print("the user is Online")
else:
    print("the User is offline")        
          
          
          
        #  Python Calculator  
operator = input("Enter An Operator (+ - * /): ")   
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == "+":
    result = num1 + num2
    print(F"The Result is {result}")
elif operator == "-":
    result = num1 - num2
    print(F"The Result is {result}")
elif operator == "*":
    result = num1 * num2
    print(F"The Result is {result}")
elif operator == "/":
    result = num1 / num2
    print(F"The Result is {result}")
else:
    print(F"{operator} is not a Valid Opretor")
    
    
    #  Pyhton Weight Convertor
weight = float(input("Enter your Weight: "))
unit = input("Kilograms Or Pounds? (K or L): ")
    
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(F"your Weight is: {round(weight)} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."
    print(F"your Weight is: {round(weight)} {unit}")
else:
    print(F"{unit} was not Valid.")      
    
#  Temprature Convertor Code
unit = input("is this Tem is Celcius or Farenheit (C/F): ")
temp = float(input("Enter The Temprature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    unit = "F"
    print(F"the updated temprature is: {round(temp)} {unit}")
elif unit == "F":
    temp = round((temp * 5) / 9 - 32, 1)
    unit = "C"
    print(F"the updated temprature is: {round(temp)} {unit}")
else:
    print(F"{unit} Is an Invalid Unit of Measurenment")    
        
        # logical operators = evaluate Multiple conditinos (or, and, not)
        
        # or = at least one conditinos must be true
        # and = both conditions are must be true
        # not = inverts the condition(not false, not true)
temp = 25 
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("the schedule are Cancelled ")    
else:
    print("the schedule are still Sheduled")    
temp  = -7
is_sunny = True

if temp >= 28 and is_sunny:
    print("it is hot outside 🎆")
    print("its sunny 🎉")
elif temp <= 0 and  not is_sunny:
    print("it is Cold outside")   
    print("it is sunny") 
elif 28 > temp > 0 and not is_sunny:
    print("it is WARM outside 🧥")
    print("it is SUNNY 🎉")
else:
    print("normal value of the formal stuation")
          
          
    #  conditional expression = a one-line shortcut of if-else statement (ternary operator )
    #  print or Assign one of two values based on a condition
    # X if Condition else Y
    
num = 6
a = 4 
b = 5


print("positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

max_num = a if a > b else b
print(max_num)

min_num = b if b > a else a
print(min_num)

age = 3
status = "adult" if age>= 18 else "Child"
print(status)

temp = 0
weather  = "HOT" if temp > 20 else "COLD"
print(weather)
      
user_role = ""

access_level = "Full acess" if user_role == "Admin" else "Limited Acess"    
print(access_level)

# username must not contain digits

username = input("Enter A username: ")

if len(username ) > 12:
    print("your username more than 12 characters")
elif not username.find(" ") == -1:
    print("your username can't contain spaces")   
elif not username.isalpha():
    print("your username can't contain numbers")
else:
    print(F"welcome to {username}")
    
    
    
name = input("Enter your full name: ")
result = len(name)
result = name.find("i")
print(result)

update_name = name.lower()
print(update_name)
result = name.isdigit()
print(result)
result = name.isalpha()
print(result)

ex = input("enter the noun: ")

result = ex.count('o')
print(result)


phone_number = input("please ener the number: ")
number = phone_number.replace("-", "")
print(number)


# validate user input exercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits


username = input("Please Enter the Username: ")

length = len(username)

if length > 12:
    print("username is no more than 12")
elif not username.find(" ")   == -1:
    print("username must not contain spaces")  
elif not username.isalpha():
    print("username must Not Contain Digits")    
else:
    print(F"welcome {username}")    


#  Inedexing Accessing elements of Sequence using [], [start, end, step]
credit_number = "1244-34533-54454-34242"
last_digits = credit_number[-4:]
print(F"XXXX-XXXX-XXXX-{last_digits}")


# validate user input exersise
username = input("please Enter the username: ")

if len(username) >= 12:
    print("username is no more than 12 characters")
elif not username.find(" ") == -1:
    print("username must not spaces")
elif not username.isalpha():
    print("username must not contain digits")    
else:
    print(F"the valid username is {username}")    


# Indexing 
credit_number = "12344-23123-123123-12313"

print(credit_number[2])
print(credit_number[:5])
print(credit_number[::5])
print(F"xxxxx-xxxx-xxxx-{credit_number[-5]}")

credit_number = credit_number[::-1]
print(credit_number)

# format specifiers

price1 = 34.3434
price2 = 345.343434
price3 = 2.345434534

print(f"price 1 is {price1:.4f}")
print(F"price 2 is {price2:.4f}")
print(F"price 3 is {price3:.4f}")

# while loop  execute some code while some condition remains true

name = input("please enter the name: ")

if name =="":
    print("you dis not enter username")
else:
    print(f"HEllo {name}")    
    
while name == "":
    print("you did not enter your name")
    # name = input("please enter your name ")
print(F"hello {name}")    


age  = int(input("please enter the age: "))

while age < 0:
    print("age can't be negative")
    age   = int(input("please enter the age: "))
print(F"you are {age} years OLd")    

food  = input("Enter a food you like (q to quite): ")

while not food  == "q":
    print(F"you like {food}")
    food = input("enter another food you like (q to quite): ")
print("bye")    


num = int(input("please enter the no betweeen 1  - 10 : "))

while num < 0 or num > 10:
    print(F"your {num} is not valid")
    num = int(input("please emter the no between 1 - 10 : "))
print(F" the no is {num}")    

# python compound Interest Calculator

principle = 0
rate = 0
time = 0
avr_rate = 1 + rate/100

amount = principle * pow(avr_rate, time)

while principle <= 0:
    principle = float(input("Enter the principle Amount: "))
    if principle <= 0:
        print("principle cant be lass than or equal to zero ")    
    break
while rate <= 0:
    rate = float(input("Enter the principle Amount: "))
    if rate <= 0:
        print("principle cant be lass than or equal to zero ") 
    break   
while time <= 0:
    time = float(input("Enter the principle Amount: "))
    if time <= 0:
        print("principle camt be lass than or equal to zero ")    
    break       
print(principle)        
print(rate)
print(time)

print(F"the amount of All Interest is {amount}")

# for loops = excute ablock of code a fixed number of times
# iterate over the range string, sequence

for x in (range(1, 11)):
    if x == 5:
        break
    else:
        print(x)
    
import time
# time.sleep(4)
# print("TIME'S UP!") 

my_time  = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    print(F"00:00:{seconds}")
    time.sleep(1)
print("Time's Up")  

 
# nested loop =     A loop within another loop (outer, inner)
#    outer loop:
    #   inner loop:


rows = int(input("Enter the rows: "))
columns = int(input("enter the colmns: "))
symbol = input("enter the symbol: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

# Collection = single avriable used to store Multiple values
# List [], set{}, Tuple()

fruits = {"apple", "orange","banana", "coconut"}
print(len(fruits))
print("banana" in fruits)
fruits.add("pineapple")
fruits.remove("orange")
fruits.pop()
fruits.clear()

for x in fruits:
    print(x)


while True:
    food = input("Enter a food to buy (q to quite): ")
    if food == "q":
        break
    else:
        price = float(input(F"Enter the price of A {food}: $"))
        food.append(food)
        price.append(price)

friuts = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery","carrots", "potatoes" ]
meats = ["chiken", "fish", "turkey"]

groceries = [friuts, vegetables, meats]     

print(groceries[1][1] ) 