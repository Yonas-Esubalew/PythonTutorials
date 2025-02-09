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
    
#  Temprature Convertor CodeC
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
        