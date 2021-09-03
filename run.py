#!/usr/bin/env python3.6

from user import User #Importing user class


def create_user(o_name,u_name,p_word): 
  '''
  Function to create a new account user
  '''
  new_user = User(o_name,u_name,p_word)
  return new_user



def save_user_details(user): 
  '''
  Function to save user(s) official name
  '''
  user.save_user()
  

  
def main(): 
  '''
  Main function that calls all other application functions
  '''
  
  print("Welcome to Password Locker.")
  print("\n")
  
  while True: #If all the functions called satisfy their conditions the loop continues otherwise,it stops
    print("Use these key abbreviations to perform different actions in the application: ca - create a new account, ex - exit the application")
    
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
 
      
    elif key_abbreviations == 'ex': 
      print("Thank you for using our application ......")
      break
    else: 
      print("I didn't get that. Please use the correct key abbreviations")
      
if __name__ == '__main__': 
  main()