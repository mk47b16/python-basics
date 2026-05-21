############### collection ######################################
# collection = single "variabe" used to store multiple values
# list= [] ordered and chageable, duplicates OK
# set ={} unordered and immutable, but add/remove OK, no duplicates
# tuples =() ordered and unchangeable, duplicates OK , faster

# fruits = ["apple","orange","banana","coconut"]

#print(help(fruits))

#fruits.sort()

# for x in fruits:
#    print(x)

########### sets #############################

# fruits = {"apple","orange","banana","coconut"}

# # fruits.add("pineapple")

# # fruits.remove("apple")
# fruits.pop()
# fruits.clear()


# print(fruits)

############## tuple ##################################

# fruits = ("apple","orange","banana","coconut")
# # special one more count

# print(fruits.count("banana"))



#################### shoping cart program #############################

# food=[]
# prices=[]
# total=0

# while True:
#     f = input("enter a food to buy(q to quit):")
#     if f =='q':
#         break
#     else:
#         price = float(input(f"Enter the price of a{f}: $"))
#         food.append(f)
#         prices.append(price)


# print("----- your cart -----")

# for x in food:
#     print(x)

# for y in prices:
#     total+= price

# print()

# print(f"your total price is: ${total}")


######## dimensional collection #######################################

# 2D List

# groceries = [["apple","orange","banana","coconut"],
#              ["celery","carrots","potatos"],
#              ["chicken","fish","turkey"]]

# for x in groceries:
#     for y in x:
#         print(y,end=" ")
#     print()



#2D tuple

# num_pad = ((1,2,3),
#            (4,5,6),
#            (7,8,9))

# for x in num_pad:
#     for y in x:
#         print(y,end=" ")
#     print()


################## dictionary #######################################
# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# capitals= {"Usa":"washington D.C",
#            "India":"New Delhi",
#            "china":"beijing"}


#print(capitals.get("India"))

#capitals.update({"Germany":"Berlin"})
#capitals.pop("china")
#capitals.popitem()
#capitals.clear()

# keys=capitals.keys()
# print(keys)

# values=capitals.values()
# print(values)

# items=capitals.items()
# print(items)


#print(capitals)



################ concession stand program ###################################

# menu = {"pizza":3.00,
#         "nachos":4.50,
#         "popcorn":6.00,
#         "fries":2.50,
#         "chips":1.00,
#         "pretzel":3.50,
#         "soda":1.00}

# cart =[]
# total=0

# print("-------menu----------")
# for k,v in menu.items():
#     print(f"{k}:${v:.2f}")

# print("---------------------")

# while True:
#     food = input("select an item(q to quit): ").lower()
#     if food =='q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)

# print("---------------- your order --------------------")

# for food in cart:
#     total = total + menu.get(food)
#     print(food,end=" ")

# print()
# print(f"Total is :${total:.2f}")


############## random number #####################################
import random
low =1
high =100
options = ("rock","paper","scissors")



#num = random.randint(low, high)
#num = random.random()

option = random.choice(options)
print(option)