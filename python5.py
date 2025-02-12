

# *args = alllows you to pass multiple non-keye arguments

# def display_name(*args):
#     for arg  in args:
#         print(arg, end= " ")
        
# display_name("Dr.", "SpongeBob", "harold",  "Squarepants")        

# **kwargs = allowa ypu to pass multiple keyword-arguments

# def print_address(**kwargs):
#     for key,values in kwargs.items():
#         print(F"{key}: {values}")
        
# print_address(street="123 fake St.",
#               city="Detroil",
#               state="MI",
#               zip="234534")

# print(print_address)

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