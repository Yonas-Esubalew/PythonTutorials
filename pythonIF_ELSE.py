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


 Inedexing Accessing elements of Sequence using [], [start, end, step]

credit_number = "1244-34533-54454-34242"
last_digits = credit_number[-4:]
print(F"XXXX-XXXX-XXXX-{last_digits}")
