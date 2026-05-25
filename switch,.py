#switch-case statement(switch): An alternative to using many 'elif' statements
#                               execute some code if a value matches a 'case'
#                               benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     if day ==1:
#         return "it is sunday"
#     elif day ==2:
#         return "it is monday"
#     elif day ==3:
#         return "it is Tuesday"
#     elif day ==4:
#         return "it is wednesday"
#     elif day ==5:
#         return "it is Thursday"
#     elif day ==6:
#         return "it is Friday"
#     elif day ==7:
#         return "it is saturday"
#     else:
#         return "Not a valid day"
    

# print(day_of_week(1))




#module = a file containing code you want to include in your program
#         use 'import' to include a module (built-in or your own)
#         useful to break up a large program reusable separate files.

# we can create module of other file and use it in other file help to use that part and reduce the code size.

#print(help("modules"))







###############################################

#variable scope = where a variable is visible and accessible
#scope resolution = (LEGB) local->enclosed->global->built-in

# def func1():
#     a=1
#     def func2():
#         print(a)
#     func2()


# func1()



#global version

# def func1():
#     print(x)


# def func2():
#     print(x)

# x=3

# func1()
# func2()



#built-in


# from math import e

# def func1():
#     print(e)

# func1()


#if_name_ ==_main_:(this script can be imported OR run standalone)
#                  function and classes in this module can be reused
#                  without the main block of code executing

# def main():
#     # your program does here 

# if __name__=='__main__':
#     main()


############################################################

# python banking program

def show_balance(balance):
    print("************************")
    print(f"Ypour balance is ${balance:.2f}")
    print("*************************")

def deposit():
    print("***************************")
    amount=float(input("Enter an amount to be deposited: "))
    print("*****************************************")
    if amount <0:
        print("************************")
        print("That's not a valid amount")
        print("******************************")
        return 0
    else:
        return amount



def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("******************************")
        print("Insufficient funds")
        print("******************************")
    elif amount <0:
        print("******************************")
        print("Amount must be greater than 0")
        print("******************************")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running= True
    while is_running:
        print("******************************")
        print(" BANKING PROGRAM")
        print("******************************")
        print("Banking program")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.Exit")
        choice = input("Enter your choice(1-4):")
        if choice =='1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice =='4':
            is_running = False
        else:
            print("******************************")
            print("Invalid choice")
            print("******************************")
    
    print("******************************")
    print("Thank you having a nice day")
    print("******************************")

if __name__ =='__main__':
    main()
