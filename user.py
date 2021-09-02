class User: 
  '''
  class that generates new instances of username
  '''
  
  username_list = [] #Empty username_list for storing usernames
  
  def __init__(self,u_name):
    #Properties for objects instantiating user class defined
    self.username = u_name