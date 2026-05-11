# # # # # ex 1 
# # # # len = int(input("please enter lenght:"))
# # # # bre = int(input("please enter readth:"))

# # # # area = len * bre
# # # # print("the area of the rectangle:", area "cm")

# # # ad1= input("please enter an adjective1:")
# # # noun= input("please enter an noun(place,person,thing)")
# # # ad2= input("please enter an adjective2:")
# # # ver1= input("please enter an verb ending with ing:")
# # # ad3= input("please enter an adjective3:")

# # # print(f"today i went to a {ad1} zoo")
# # # print(f"in an exhibit, i saw a {noun}")
# # # print(f"{noun} was {ad2} and {ver1}")
# # # print(f"i was {ad3}")

# # import math
# # r = float(input("please enter radius:"))
# # p = math.pi
# # c = 2 * p * r

# # print(f"the perameter of the circule is:{c}")

# import math

# a = float(input("please enter side A"))
# b = float(input("please enter side B"))

# c = math.sqrt(pow(a , 2) + pow(b, 2 ))

# print(c)
################################EX2##########################################################


# import math

# op = input("please select operator(+,-,*,/)")
# num1 = float(input("please enter a 1st number:"))
# num2 = float(input("please enter 2nd number:"))

# if op == "+":
#     r = num1+num2
#     print(r)
# elif op == "-":
#     r = num1 - num2
#     print(r)
# elif op== "*":
#     r = num1 * num2
#     print(r)
# elif op== "/":
#     r = num1 / num2
#     print(r)
# else:
#     print("sorry try again")

########################################EX3#############################################

# w = float(input("please enter your weight:"))
# unit = input("is it in kilogram or pounds?(K or L):")

# if unit == "K":
#     w = w * 2.205
#     unit = "labs"
#     print(f"your weight is {w}{unit}")

# elif unit == "L":
#     w = w / 2.205
#     unit = "kg"
#     print(f"your weight is {w}{unit}")

# else:
#     print(f"{unit} in invalid")
############################### logic operation################################################

#####################################using or #####################################################

# temp = int(input("please enter your city temp:"))
# is_raining = False 

# if temp >= 35 or temp < 0 or is_raining:
#     print("the plan need to change")
# else:
#     print("you are ready to go")

# temp = int(input("please enter the temp:"))
# is_raining = False
################ using and ###########################################################
# if temp >= 20 and is_raining:
#     print("no chance to go")
# else:
#     print("ready to go")
###################### using not #######################################

# temp = int(input("please enter temp"))
# is_raining = False

# if temp >= 40 and is_raining:
#     print("no chance")
# elif temp< 30 and not is_raining:
#     print("kind off")
# else:
#     print("lets go")

#####################################################################################

# num = 3.2
# r = "even" if num % 2 ==0 else "odd"
# print(r)

# a = 2 
# b = 5 
# max_n = a if a > b else b
# min_n = a if a < b else b
# print (min_n)
# print(max_n)

#print(help(str))

# n = input("please enter username:")

# if len(n) > 12 :
#     print("your username is too long")
# elif not n.find(" ") == -1:
#     print(" you contain space in username")
# elif not n.isalpha():
#     print("it contain digits try again")
# else :
#     print (" thanks for your username")
#############################################################################################
# n = int(input("please enter number:"))

# if not n % 2 == 0:
#     print("weird")
# elif n == 2 or n== 4:
#     print(" not weird")
# elif n % 2 == 0 and 6 <= n <=20:
#     print("weird")
# elif n % 2 == 0 and n > 20:
#     print("not weird")
# else:
#     print("try again")

##### simple version

# n = int(input("please enter number"))

# if n % 2 != 0:
#     print("Weird")
# elif 2 <= n <= 5:
#     print("Not Weird")
# elif 6 <= n <= 20:
#     print("Weird")
# else:
#     print("Not Weird")

##############################################################################################

# a = int(input("1st"))
# b = int(input("2nd"))
# print(a + b)
# print(a - b)
# print(a * b )

#############################################################################################

# a = int(input())
# b = int(input())
# print(a//b)
# print(a/b)
#############################while loop######################################################

# name = input("please enter your name:")

# while name =="":
#     print("you did not enter your name:")
#     name = input("please enter your name:")

# print(f"hello {name}")
####################################python compoud interest calculator##############################

# p = 0
# r = 0 
# t = 0

# while p <= 0 : 
#     p = float(input("please enter the initial pricipal you invest:"))
#     if p < 0:
#         print("principal cant me negative or zero")
#     else:
#         break

# while r <= 0 :
#     r = float(input("please enter the rate offer:"))
#     if r < 0:
#         print("rate cant be negative or zero")
#     else:
#         break

# while t <= 0:
#     t = float(input("please enter the duration of time:"))
#     if t < 0:
#         print("time cant be negative or zero")
#     else:
#         break


# k = p * pow((1+(r/100)),t)

# print(f"balance after {t} yr will be {k} ")

########################### for loop ##########################################################

# for x in reversed(range(1,11)):
#     print(x)

# print("happy new year!")

# for x in range(1,21):
#     if x == 13 :
#         continue
#     else:
#         print(x)
####################################countdown timer program########################################

# import time 

# my_time = int(input("enter the time in sec:"))

# for x in range(my_time,0,-1):

#     seconds = x%60
#     minutes = int(x/60) % 60
#     hour = int(x/3600)
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("times up!")
################################ nested loop #####################################################

# for x in range(3):
#     for y in range(1,10):
#         print(y,end=" ")
#     print()
###################
# r = int(input("enter the# of the row:"))
# c = int(input("enter the# of the coulum:"))
# s = input("enter the# of the symbol:")

# for x in range(r):
#     for y in range(c):
#         print(s,end="")
#     print()

########################### shopping cart program################################################
# total = 0
# food = []
# price = []

# while True:
#     f = input("please enter the food you like(q to quit):")
#     if f =="q":
#         break
#     else:
#         p = float(input(f"please enter the price {f} "))
#         food.append(f)
#         price.append(p)

# print("----- your cart--------")

# for f in food:
#     print(f)

# for p in price:
#     total += p

# print()

# print(f"your total bill is {total}")

############## better version ###############################################################



# total = 0
# food = []
# price = []

# while True:
#     f = input("please enter the food you like(q to quit):")
#     if f =="q":
#         break
#     else:
#         p = float(input(f"please enter the price {f} "))
#         food.append(f)
#         price.append(p)

# print("----- your cart--------")

# for f in food or p in price:
#     total += p 
#     print(f"{f} -----> {p}")

# print()

# print(f"your total cost is {total} ")


######################################## 2D list #################################################

# f = ['apple','orange','banana','coconut']
# v = ['celery','carrot','potato']
# m = ['chicken','fish','turkey']

# g = [f,v,m]

# print(g)

# print(g[0] [0])

####################### num pad ###########################################################

# num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

# for row in num_pad:
#     for num in row:
#         print(num , end=" ")
#     print()

################################# dictionary ###############################################

# capital = {"usa":"washington D.C","India":"delhi","china":"beijing","russia":"moscow"}

#print(dir(capital))

# print(capital.get("usa"))

# capital.update({"germany":"berlin"})

# print(capital)

# capital.pop("china")
# print(capital)

# capital.popitem()
# print(capital)

# a = capital.keys()
# print(a)

# values = capital.values()
# print(values)

# items = capital.items()
# print(items)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is Not Prime")

