
################## arthmetic calculator######################################################


# print("arthmetic calculator")
# a=float(input("enter the  number a:"))
# b=float(input("enter the number b:"))
# operator=input("enter (+,-,*,/):")

# if operator == "+":
#     result=a+b
#     print(result)
# elif operator == "-":
#     result=a-b
#     print(result)
# elif operator =="*":
#     result=a*b
#     print(result)
# elif operator =="/":
#     result=a/b
#     print(result)
# else:
#     print("choice is in correct choose again")



################weight convertor#######################################################

# w=float(input("enter the weight:"))
# unit=input("enter the unit of the weight(K or L):")

# if unit =="K":
#     w= w*2.205
#     unit ="Lbs"
# elif unit =="L":
#     w=w/2.205
#     unit ="Kgs"
# else:
#     print(f"your{unit} is invalid")

# print(f"you weight is {w} {unit}")


################################### logical operator############################################

#logic operator: evaluate multiple condition(or,and,not)
#                or = at least one contidition must be true
#                and = both conditions must be true 
#                not = inverts the condtion (not false, not true)

#######      or #####################

# temp = -5
# is_running = False

# if temp > 35 or temp < 0 or is_running:
#     print("the outdoor event is cancelled")
# else:
#     print("the outdoor event is still on") 


############ and & not ##################################

# temp = 25
# is_sunny = False

# if temp >=28 and is_sunny:
#     print("its hot outside")
#     print("it is sunny")
# elif temp <=0 and is_sunny:
#     print("its cold outside")
#     print("it is sunny")
# elif 28>temp>0 and is_sunny:
#     print("its warm outside")
#     print("it is sunny")

# elif temp >=28 and not is_sunny:
#     print("its hot outside")
#     print("it is cloudy")
# elif temp <=0 and not is_sunny:
#     print("its cold outside")
#     print("it is cloudy")
# elif 28>temp>0 and not is_sunny:
#     print("its warm outside")
#     print("it is cloudy")


#################### conditional operator ##########################################################

# conditional operator= A one-line shortcut for the if-else statement(ternary operator)
#                       print or assign one of two values based on a condition
#                       x if condition else y 

# num = 5
# print("positive"if num >0 else "negative")
# result= "even" if num%2==0 else "odd"

# print(result)



###################### string ########################################################################

#name = input("enter the name:")
# n = len(name)

# n= name.find(" ")
# n = name.rfind(" ") # from the last one to find 
# n = name.capitalize() #only the first word of the sentece capatalize 
#n = name.upper() # all the character capatalize
#n=name.lower() #all the character get lower
#n=name.isdigit() #tell the string contain only digit if number + character given then still return false
#n=name.isalpha() #tell the string conatain alpha and it also give false if space is there 
#n=name.count(" ") #count from the string need to count and tell the number of that present in it
#n=name.replace(" ","-") # replace the  first one from the second one 

#print(n)



############################ indexing ###########################################################################

#indexing = accessing element of a sequence using [] (indexing operator)
# [start : end: step]

#credit_number = "1234-5678-9012-3456"

#print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[::2])




#################################loops###################################################################################

####### while loop ######################
# execute some code while some condition remain true

# name = input("enter the name:")

# if name =="":
#     print("you did not enter the name")
#     name = input("enter the name:")
# print(f"Hello {name}")




########################## python comand interest calculator #####################################################################

# p=0
# r=0
# t=0

# while p <=0:
#     p= float(input("enter the principle:"))
#     if p <=0:
#         print("cant be less than equal to zero")

# while r <=0:
#     r= float(input("enter the rate:"))
#     if r <=0:
#         print("cant be less than equal to zero")

# while t <=0:
#     t= int(input("enter the time:"))
#     if t <=0:
#         print("cant be less than equal to zero")

# result = p *pow((1+r/100),t)

# print(f"the balance after {t} will be {result}")


############################################### for loop #####################################################

# for loop = execute a block of code a fixed number of time.
#             you can iterate over a range , string,sequence,etc.

# for x in range(1,11):
#     print(x)


############## countdown timer #################################

# import time

# my_time=int(input("enter the time in seconds:"))

# for x in range(my_time,0,-1):
#     seconds = x%60
#     min = int(x/60)%60
#     hour =int(x/3600)
#     print(f"{hour}:{min:02}:{seconds}")
#     time.sleep(1)

# print("time's up!")



################ nested loops ##################################

#nested loop = A loop within another loop(outer,inner)
#               outer loop:
#                    inner loop:

rows = int(input("enter the  rows:"))
col = int(input("enter the columns:"))
sym = input("enter a symbol to use:")

for x in range(rows):
    for y in range(col):
        print(sym,end="")
    print()


