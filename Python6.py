

# import math as example 
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)

# print(result)

# def funcc1():
#     a = 1
#     print(a)
    
# def func2():
#     b = 3
#     print(b)   
# funcc1()    

# func2()     

# from math import e

# def func1():
#     print(e)
    
#     e = 3
    
#     func1()
# print()    

# def main():
# if  __name__ == "__main__"   :
#     main() 

# print(__name__)

# def main():
#     print()
 
# if __name__ == "__main__" :
#     main()   
    
# def favorite_food(food):
#     print("your favorite food is {food}")    
    
# def main():
#     print("this is script") 
#     favorite_food("pizza")   
#     print("GOODBYE!")
    
# if __name__ == "__main__":
#     main()    

# def favorite_drink(drink):
#     food = print("your favorite drink is {drink}")
    
# print(F"{food} this is script")    

# python banking program


# def show_balance():
#     print(F"your balance is ${balance}:.2f")
# def deposit():
#     amount = float(input("Enter an amount to be deposited: "))
#     if amount < 0:
#         def withdraw():
#             pass
# def withdraw():
#     pass

# balance = 0
# is_running = True


# while is_running:
#     print("1.banking Program")
#     print("2.Show Balance")
#     print("3.Deposit")
#     print("4.Withdraw")
#     print("4.Exit")
    
# choice = input("Enter your choice (1/4): ")    
# if choice == "1":
#     show_balance()
# elif choice == "2":
#     deposit()
# elif choice == "3":
#     withdraw()
# elif choice == "4":
#     print("Exit")         
    
# print("Thank you have a nice day")       
# print("hello world")

# python banking program


balance = 0
# balanc = balance + 2
is_running = True

def show_balance():
    print(F"your balance is ${balance:.2f}")
def deposit():
    amount = input("Enter an amount to be deposited: ")
    if amount < 0:
        print("that is not a valid amount")
    else:
        return amount
def withdraw():
    pass


balance = 0
# balanc = balance + 2
is_running = True

while is_running:
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
    
    choice  = input("Enter your Chioce (1/4): ")
    
    if choice == "1":
        show_balance()
    elif choice  == "2":
        balance += deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("That is not valid Number")     
print("thank you! have a nice day")              
    