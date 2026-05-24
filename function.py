#function= A block of reusable code 
#          place () after the function name to invoke it 

# def happy_birthday(name ,age):
#     print(f"happy birthday to {name}")
#     print(f"you are {age} old!")
#     print("happy birthday to you!")
#     print()

# happy_birthday("bro", 20)
# happy_birthday("steve", 30)
# happy_birthday("joe", 40)


#return = statement used to end a function
#         and send a result back to the caller


# def add(x, y):
#     z=x+y
#     return z

# k=add(1, 2)
# print(k)

############################################################

#default argument = A default value for certain parameters
#                    default is used when that argument is omitted 
#                   make your function more flexible, reduces # of arguments
#                  1.positional, 2.default, 3.keywords ,4.arbitrary

# def net_prices(list_prices, discount=0, tax=0.05):
#     return list_prices *(1-discount)*(1+tax)

# #print(net_prices(500))
# #print(net_prices(500, 0.1))
# #print(net_prices(500,0.1,0))



#keyword arguments = an argument preceded by an identifier
#                    helps with readability 
#                    order of argument doesn't matter
#                    1. positional 2.default 3.keyword 4.arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")


#hello("hello", "Mr.", "spongebob", "Squarepants")
# hello("hello",first="spongebob",last="Squarepants",title="Mr.")


###############################################################
#*args  =allows you to pass multiple non-key arguments
#**kwargs =allos you to pass multiple keywords-arguments
#           * unpacking operator
#           1.positional 2.default 3.keyword 4.arbitrary

# def add(*args):
#     total=0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4))

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")


# print_address(street="123 fake st.",
#               city="detroit",
#               state="mi",
#               zip="54321")



# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value,end=" ")

# shipping_label("Dr.","spongebob", "squarepants","III",
#                street="123 fake st.",
#                city="detroit",
#                state="mi",
#                zip="54321")




#iterables = An object/collection that can return its elements one at a time,
#            allowing it to be iterated over in a loop

# nums =(1,2,3,4,5)

# for num in nums:
#     print(num)



# my_dictionary ={"A":1,"B":2,"c":3}

# for key,value in my_dictionary.items():
#     print(f"{key}={value}")




#membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in


# word = "APPLE" 

# letter = input("Guess a letter in the secret word:")

# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")




#List comprehension = A concise way to create lists in python
#                     compact and easier to read than traditional loops
#                     [expression for value in iterable if condition ]

# doubles =[x*2 for x in range(1,11)]

# print(doubles)


grades=[85,79,50,61,30,24,67]
passing_grades =[ grade for grade in grades if grade >=60]

print(passing_grades)