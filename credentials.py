class Credentials: 
  '''
  class that generates new instances of user passwords
  '''
  
  credentials_list = [] #Credentials list to store user(s) password(s)
  
  def __init__(self,p_word):
    #Properties for objects instantiating credentials class defined
    self.password = p_word