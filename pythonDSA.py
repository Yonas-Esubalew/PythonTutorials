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
