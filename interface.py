#!/usr/bin/env python3.8
from passlock import User, Credentials

def function():
	print("                          __    __   __  ")
	print("                         |  |  |  | |  | ")
	print("                         |  |__|  | |  | ")
	print("                         |   __   | |  | ")
	print("                         |  |  |  | |  | ")
	print("                         |__|  |__| |__| ")
function()

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username,password)
    return check_user
def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to credential list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false
    """
    return Credentials.if_credential_exist(account)


def generate_Password():
    '''
    generates a random password for user.
    '''
    auto_password=Credentials.generatePassword()
    return auto_password
def copy_password(account):
    """
    A funct that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account)
def passlocker():
    print("Hello Welcome to your Accounts Password Place...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ex":
    #     print("nice having you. Welcome again.......bye!")
    # elif short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        # password = input("Password: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_Password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        
        print("*"*85)
        print(f"Hello {username}, account created succesfully!Your password is: {password}")
        print("*"*85)
    elif short_code == "li":
        # print("Login! ")
        print("*"*50)
        print("Enter your User name & Password to log in:")
        print('*' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Pass Locker")  
            print('\n')
            print("what would you like to do?")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your password if already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_Password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential : {account} - UserName: {userName} Password:{password} created successfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("Here's your list of acoounts: ")

                print('*' * 30)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('_' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
            else:
                print("That Credential you want to delete does not exist in place yet")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().capitalize()
            if check_credendtials(search_name):
                search_credential = find_credential(search_name)
                print(f"{search_credential.account}")
                print("_"*30)
                Credentials.delete_credentials()
                print('\n')
                print(f"New Credential : {account} UserName: {userName}  successfully deleted!!!")
                print('\n')
            else:
                print("That Credential does not exist in place for now")

        elif short_code == 'gp':

            password = generate_Password()
            print(f" {password} generated succesfully. may proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using password manager.. !")
            break
        else:
            print("Password error... Check entry again and let it match those in the menu")
    else:
        print("Please enter a valid input 2 continue")
        
if __name__ == '__main__':
    passlocker() 