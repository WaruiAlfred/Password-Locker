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
    
if __name__ == '__main__':
    unittest.main()   
    