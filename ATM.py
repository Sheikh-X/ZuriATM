
import random
import database
import validation
from getpass import getpass


def init():
    print("Welcome to Iyesaf Bank")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()

    elif have_account == 2:

        register()

    else:
        print("You have selected invalid option")
        init()


def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password);

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("****** Register *******")

    email = input("Enter your email address : \n")
    first_name = input("Enter your first name : \n")
    last_name = input("Enter your last name : \n")
    password = getpass("Enter password you want to use : \n")

    account_number = generation_account_number()

    is_user_created = create(account_number, first_name, last_name, email, password)

    if is_user_created:

        print("Your Account Has been created")
        print(" == ==== ====== ===== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it safe")
        print(" == ==== ====== ===== ===")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4)Close Account  (5) Exit \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 5:

        close_account()
    elif selected_option == 4:

        exit()    
    else:

        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation():
    print("withdrawal")
    balance = get_current_balance
    withdraw = int(print("Enter Amount to withdraw: \n "))
    if (balance >= withdraw):
        new_balance = int(balance - withdraw)
        print("Kindly take your cash, your new balance is: \n")
        print(new_balance)
    else:
        print("Insufficient balance")
    

def deposit_operation():
    print("Deposit Operations")
    deposit = int(input("How much do you want to deposit: \n"))
    balance = get_current_balance
    new_balance = int(balance + deposit)
    print("Deposit successful, your new balance is: \n")
    print(new_balance)

    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance


def generation_account_number():
    return random.randrange(1111111111, 9999999999)


def set_current_balance(user_details, balance):
    user_details[4] = balance


def get_current_balance(user_details):
    return user_details[4]

def close_account(user_details): 
    print("Your account has been closed succesffuly, kindly take your cash" )

def logout():
    login()

   


init()