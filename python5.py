

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