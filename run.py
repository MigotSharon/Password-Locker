#!/usr/bin/env python3.6
from account import Account

def create_account(fname,lname,phone,email,username,password):
    '''
    Function to create a new account
    '''
    new_account = Account(fname,lname,phone,email,username,password)
    return new_account

def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()   

def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()     

def find_account(number):
    '''
    Function that finds a account by number and returns the account
    '''
    return Account.find_by_number(number) 

def check_existing_account(number):
    '''
    Function that check if a account exists with that number and return a Boolean
    '''
    return Account.account_exist(number) 

def display_account():
    '''
    Function that returns all the saved account
    '''
    return Account.display_accounts()  

def main():
    print("Hello Welcome to your account list. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
            print("Use these short codes : cc - create a new account, dc - display accounts, fc -find a account, ex -exit the account list ")
            short_code = input().lower()
            if short_code == 'cc':
                print("New Account")
                print("-"*10)

                print ("First name ....")
                f_name = input()

                print("Last name ...")
                l_name = input()

                print("Phone number ...")
                p_number = input()

                print("Email address ...")
                e_address = input()

                print("Username ...")
                u_name = input()

                print("Password ...")
                p_password = input()


                save_accounts(create_account(f_name,l_name,p_number,e_address,u_name,p_password))
                print ('\n')
                print(f"New Account {f_name} {l_name} created")
                print ('\n')

            elif short_code == 'dc':

                if display_account():
                    print("Here is a list of all your account")
                    print('\n')

                    for account in display_account():
                        print(f"{account.first_name} {account.last_name} .....{account.phone_number}")

                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any accounts saved yet")
                    print('\n')

            elif short_code == 'fc':
                print("Enter the number you want to search for")

                search_number = input()
                if check_existing_account(search_number):
                        search_account = find_account(search_number)
                        print(f"{search_account.first_name} {search_account.last_name}")
                        print('-' * 20)

                        print(f"Phone number.......{search_account.phone_number}")
                        print(f"Email address.......{search_account.email}")
                        print(f"Username.......{search_account.username}")
                        print(f"Password.......{search_account.password}")
                else:
                        print("That account does not exist")

            elif short_code == "ex":
                print("Bye .......")
                break
            else:
                print("I really didn't get that. Please use the short codes") 

if __name__ == '__main__':
    main() 

