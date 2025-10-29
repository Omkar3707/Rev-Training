from BankDetails import BankDetails

class CreditCard(BankDetails):
    def __init__(self,cus_id,c_name,balance,creditscore,status):
        super().__init__(cus_id,c_name,balance)
        self.creditscore=creditscore
        self.status=status

    def wel_msg(self):
        print(f'Welcome to SBI, {self.c_name}')

    def dis_cc_details(self):
        print(f'{self.creditscore} - {self.status}')