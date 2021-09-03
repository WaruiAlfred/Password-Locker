class Credentials: 
  '''
  class that generates new instances of user passwords
  '''
  
  credentials_list = [] #Credentials list to store user(s) password(s)
  
  def save_credentials(self): 
    '''
    this function adds a user's details of account creation to credentials list
    '''
    Credentials.credentials_list.append(self)
  
  def __init__(self,account,u_name,p_word):
    #Properties for objects instantiating credentials class defined
    self.account = account
    self.username = u_name
    self.password = p_word