import unittest
from passlock import User
from passlock import Credentials

# class UserTest(unittest.TestCase):
class TestClass(unittest.TestCase):    
    """
    A Test class that defines test cases for the User class.
    """

    # """
    # A Test class that defines test cases for the User class.
    # """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('poldiee','XyZ3thf1')


    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        
        """
        self.assertEqual(self.new_user.username,'poldiee')
        self.assertEqual(self.new_user.password,'XyZ3thf1')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.
        """
        self.new_credential = Credentials('Gmail','poldiee','yx5Gij43')
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account,'Gmail')
        self.assertEqual(self.new_credential.userName,'poldiee')
        self.assertEqual(self.new_credential.password,'yx5Gij43')

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
    unittest.main()