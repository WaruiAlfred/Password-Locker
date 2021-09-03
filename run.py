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
  
  
  
def main(): 
  '''
  Main function that calls all other application functions
  '''
  
  print("Welcome to Password Locker.")
  print("\n")
  
  while True: #If all the functions called satisfy their conditions the loop continues otherwise,it stops
    print("Use these key abbreviations to perform different actions in the application: ca - create a new account, sec - store existing credential details, ex - exit the application")
    
    key_abbreviations = input().lower()
    
    if key_abbreviations == "ca": 
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
        print("Your password characters don't match!")
      
     
    elif key_abbreviations == "sec": 
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
      
    elif key_abbreviations == 'ex': 
      print("Thank you for using our application ......")
      break
    else: 
      print("I didn't get that. Please use the correct key abbreviations")
      
if __name__ == '__main__': 
  main()