import unittest
from passwords import user
class TestUser(unittest.TestCase):
    '''
    Test class that defines tests for user class behaviours
    Args:
         unittest.Testcase:Testcase class that helps create test cases
    '''
    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User("a.s.s.matic","Instagram","maurinesinami")#create contact object
    def test_init(self):
            '''
            test_init test test case to test if te object is initialized properly
            '''
        self.assertEqual(self.new_user.username,"a.s.s.matic")
        self.assertEqual(self.new_user.account, "Instagram")
        self.assertEqual(self.new_user.password,"maurinesinami")
if __name__ == '__main__':
    unittest.main()
