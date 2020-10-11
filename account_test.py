import unittest
from account import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.new_account = Account("Migot","Sharon","0790437491","migotsharon@gmail.com","MigotSharon","12345")
    def test_init(self):
        self.assertEqual(self.new_account.first_name,"Migot")
        self.assertEqual(self.new_account.last_name,"Sharon")
        self.assertEqual(self.new_account.phone_number,"0790437491")
        self.assertEqual(self.new_account.email,"migotsharon@gmail.com")
        self.assertEqual(self.new_account.username,"MigotSharon")
        self.assertEqual(self.new_account.password,"12345")

    def test_save_account(self):
        self.new_account.save_account() 
        self.assertEqual(len(Account.account_list),1)

    def tearDown(self):
        Account.account_list = []    

    def test_save_multiple_account(self):
        '''
        Method to check if we can save multiple account objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account ("Migot","Sharon","0790437491","migotsharon@gmail.com","MigotSharon","12345") 
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)  


    def test_delete_account(self):
    
        self.new_account.save_account()
        test_account = Account("Migot","Sharon","0790437491","migotsharon@gmail.com","MigotSharon","12345") # new contact
        test_account.save_account()
        test_account.delete_account()
        self.assertEqual(len(Account.account_list),1)

    def test_find_account_by_number(self):
        '''
        To find a account by phone number and display information
        '''
        self.new_account.save_account()
        test_account = Account("Migot","Sharon","0790437491","migotsharon@gmail.com","MigotSharon","12345")
        test_account.save_account()

        found_account = Account.find_by_number("0790437491")
        
        self.assertEqual(found_account.password,test_account.password)

    def test_account_exists(self):

        self.new_account.save_account()
        test_account = Account("Migot","Sharon","0790437491","migotsharon@gmail.com","MigotSharon","12345") 
        test_account.save_account()

        account_exists = Account.account_exist("0790437491")

        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        self.assertEqual(Account.display_accounts(),Account.account_list)    
     


if __name__ == "__main__":
    unittest.main()            
