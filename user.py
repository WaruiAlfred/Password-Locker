class User: 
  '''
  class that generates new instances of username
  '''
  
  users_list = [] #Empty username_list for storing usernames
  
  def save_user(self): 
    '''
    save_user function adds new user(s) official name(S) to users list
    '''
    User.users_list.append(self)
  
  @classmethod
  def find_by_password(cls,password_input): 
    '''
    Method that takes in a password and returns true if the password matches the user's account password
    '''
    for found in cls.users_list:
      if found.password == password_input:
        return found
  
  def __init__(self,o_name,u_name,p_word):
    #Properties for objects instantiating user class defined
    self.official_name = o_name
    self.username = u_name
    self.password = p_word