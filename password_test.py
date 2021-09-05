from user import User #Importing the user class
from credentials import Credentials #Importing the credentials class
import unittest #Importing python unittest module for testing

class TestPassword(unittest.TestCase): 
  '''
  Test class to test user and credentials classes behaviours.
  TestCase class helps in creating test cases.
  '''
  
  def setUp(self):
    '''
    setUp method to run before every test case.
    '''
    self.new_user = User("John Mac","Miley","1234")
    self.new_credentials = Credentials("twitter","Aldis","1234")
    
  def tearDown(self):
    '''
    tearDown method to clean up after each test case has run.
    '''
    User.users_list = []
    Credentials.credentials_list = []
    
  def test_init(self):
    '''
    test_init to test proper initialization of objects' properties
    '''

    self.assertEqual(self.new_user.official_name,"John Mac")
    self.assertEqual(self.new_user.username,"Miley")
    self.assertEqual(self.new_user.password,"1234")
    self.assertEqual(self.new_credentials.account,"twitter")
    self.assertEqual(self.new_credentials.username,"Aldis")
    self.assertEqual(self.new_credentials.password,"1234")
    
  def test_save_user(self): 
    '''
    test_save_user to test if username in added to username list and credentials to credentials list
    '''
    self.new_user.save_user() #save user(s) official name(s)
    self.new_credentials.save_credentials() #save new credentials for user(s)
    self.assertEqual(len(User.users_list),1) #checking if users list length has increased
    self.assertEqual(len(Credentials.credentials_list),1) #checking if credentials list length has increased
    
  def test_save_multiple_credentials(self): 
    '''
    Test to confirm if multiple credentials can be saved in the credentials list
    '''
    self.new_credentials.save_credentials()
    test_credential = Credentials("facebook","bale","meforyou") # new credential details
    test_credential.save_credentials()
    
    #error message in case test case fails
    message = "Unable to add multiple credentials to credentials list"
    
    self.assertGreater(len(Credentials.credentials_list),1,message) #Checking if length of credentials list has increased
    
  def test_save_multiple_users(self): 
    '''
    Test to confirm if multiple users can create accounts
    '''
    self.new_user.save_user()
    test_user = User("Mercy Mumbi","Alice","9876") #new user account
    test_user.save_user()
    
    self.assertEqual(len(User.users_list),2)
    
  def test_find_account_by_password(self): 
    '''
    Test to confirm if a user(s) account can be accessed by the inputted password and credentials information displayed
    '''
    self.new_user.save_user()
    test_user = User("Mercy Mumbi","Alice","9876") #new user account
    test_user.save_user()
    
    found_user = User.find_by_password("9876")
    
    self.assertEqual(found_user.password,test_user.password)
    
  def test_find_credential(self): 
    '''
    Test to confirm whether the credential located is the correct one
    '''
    self.new_credentials.save_credentials()
    test_credential = Credentials("facebook","bale","meforyou") # new credential details
    test_credential.save_credentials()
    
    found_credential = Credentials.find_credential("facebook")
    
    self.assertEqual(found_credential.account,test_credential.account)
    
  def test_delete_credentials_account(self): 
    '''
    Test to confirm whether a credentials account has been deleted
    '''
    self.new_credentials.save_credentials()
    test_credential = Credentials("facebook","bale","meforyou") # new credential details
    test_credential.save_credentials()
    
    test_credential.delete_credential_account("facebook") #Deleting a credential account
    
    self.assertEqual(len(Credentials.credentials_list),1)
    
if __name__ == '__main__':
    unittest.main()   
    