class Account:
    '''
Create account that generate new instance of accounts
'''

    account_list = []# Empty account list 

    def __init__(self,first_name,last_name,phone_number,email,username,password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.username = username
        self.password = password

    account_list = []

    def save_account(self):
        Account.account_list.append(self) 

    def delete_account(self):
        Account.account_list.remove(self)       

    @classmethod
    def find_by_number(cls,number):
        
        for account in cls.account_list:
            if account.phone_number == number:
                return account  

    @classmethod
    def account_exist(cls,number):
        
        for account in cls.account_list:
            if account.phone_number == number:
                    return True

        return False  

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list                
