#!/usr/bin/env python3.6

from user import User #Importing user class
from credentials import Credentials #Importing credentials class

def create_user(o_name,u_name,p_word): 
  '''
  Function to create a new account user
  '''
  new_user = User(o_name,u_name,p_word)
  return new_user

def create_credentials(account,account_u_name,account_p_word): 
  '''
  Function to create credentials
  '''
  new_credential = Credentials(account,account_u_name,account_p_word)
  return new_credential

def save_user_details(user): 
  '''
  Function to save user(s) official name
  '''
  user.save_user()
  
def save_credentials_details(credentials): 
  '''
  Function to save user(s) account credentials
  '''
  credentials.save_credentials()
  
def find_account(password_input):
    '''
    Function that locates a user's account and displays the user's credentials
    '''
    return User.find_by_password(password_input)
  
def find_credential(account_name_input):
    '''
    Function that locates a user's credentials by account name and displays the details
    '''
    return Credentials.find_credential(account_name_input)
  
def delete_credential(to_delete): 
  '''
  Function that locates a credentials account and deletes it
  '''
  return Credentials.delete_credential_account(to_delete)
  
def main(): 
  '''
  Main function that calls all other application functions
  '''
  
  print("Welcome to Password Locker.")
  print("\n")
  
  while True: #If all the functions called satisfy their conditions the loop continues otherwise,it stops
    print("Use these key abbreviations to create an account and/or to login to your account: ca - create a new account, sec - store existing credential details, cnew - create new account credentials, dac - display account credentials, dc - delete credentials account, ex - exit application")
    
    key_abbreviations = input().lower()
    
    if key_abbreviations == "ca": 
      print("\n")
      print("Account Creation")
      print("-" * 16)
      
      print("What is your official name?")
      o_name = input()
      
      print("Username.....")
      u_name = input()
      
      print("Password.....")
      p_word = input()
      print("Confirm password")
      test_password = input()
      
      if p_word == test_password: 
        print("\n")
        save_user_details(create_user(o_name,u_name,p_word)) # create and save new user.
        print(f"Congratulations {o_name}, you have successfully created an account.")
        print('\n')
      else: 
        print("Your password characters don't match!Try again.")
        print("\n")
     
    elif key_abbreviations == "sec": 
      try:
        print("\n")
        print(f"Welcome back, {o_name}. Go ahead and store your existing accounts credentials.") 
        
        print("Account name...")
        acc_name = input()
        
        print("Account username...")
        acc_username = input()
        
        print("Account password...")
        acc_password = input()
        
        print("\n")
        save_credentials_details(create_credentials(acc_name,acc_username,acc_password)) # create and save new users' account credentials.
        print(f"You have successfully saved details of your {acc_name} account.")
        print("\n")
      except UnboundLocalError: 
        message = print("You have to create an account first!!")
        return message
      
    elif key_abbreviations == "cnew": 
      try:
        print("\n")
        print(f"Welcome back, {o_name}....") 
        print("Create new account credentials")
        print("\n")
        
        print("Which account credential do you want to create?(e.g twitter)")
        new_account = input()
        
        print("What would you like to be your username?")
        new_username = input()
        
        print("Would you like the application to generate a password for you?(Y/N)")
        user_preference = input()
        if user_preference == "Y": 
          new_password = f"1234{new_account}"
          print("\n")
          print(f"Your {new_account} password is: {new_password}")
        else: 
          print("Input password of your choice:")
          new_password = input()
          print("\n")
          print(f"Your {new_account} password is: {new_password}")
            
        print("\n")
        save_credentials_details(create_credentials(new_account,new_username,new_password)) # create and save new users' account credentials.
        print(f"You have successfully created your new {new_account} account credentials.")
        print("\n")
      except UnboundLocalError: 
        message = print("You have to create an account first!!")
        return message
    
    elif key_abbreviations == "dac": 
      print("\n")
      print("Input your password to login to your account and view credentials.")
      password_input = input()
      if find_account(password_input): 
        print("Type in the name(i.e twitter) of account credential you want to view")
        account_to_find = input()
        if find_credential(account_to_find): 
          outcome = find_credential(account_to_find)
          print("\n")
          print("Here are the details to the account credentials you are looking for.")
          print("-"*20)
          print(f"Account name: {outcome.account}")
          print(f"Username: {outcome.username}")
          print(f"Password: {outcome.password}")
          print("\n")
        else: 
          print("Sorry,no credential account with such name exists!Please try entering the correct name or creating the credential account.")
          print("\n")
          
      else: 
        print("Unable to login.Try re-entering the password correctly or create an account if you haven't.")
        print("\n")
        
    elif key_abbreviations == "dc": 
      print("\n")
      print("Enter account name(i.e twitter) of the credentials that you want to delete.")
      account_to_delete = input()
      if delete_credential(account_to_delete): 
        print("\n")
        print(f"You have successfully deleted your {account_to_delete} account credential.")
        print("\n")
      else: 
        print("Sorry.No credentials to the account name you inputted exist.")
        print("\n")
        
    elif key_abbreviations == 'ex': 
      print("Thank you for using our application ......")
      break
    
    else: 
      print("I didn't get that. Please use the correct key abbreviations")
      
if __name__ == '__main__': 
  main()