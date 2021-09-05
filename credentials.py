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
    
  @classmethod
  def find_credential(cls,account_name_input): 
    '''
    Method that takes in account name and displays details of the credential
    '''
    for found in cls.credentials_list:
      if found.account == account_name_input:
        return found
  
  @classmethod
  def delete_credential_account(self,to_delete): 
    '''
    Method to delete a credential account
    '''
    for indeletion in self.credentials_list:
      if indeletion.account == to_delete:
        return Credentials.credentials_list.remove(indeletion)
    
  
  def __init__(self,account,u_name,p_word):
    #Properties for objects instantiating credentials class defined
    self.account = account
    self.username = u_name
    self.password = p_word