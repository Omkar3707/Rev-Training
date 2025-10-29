class BankDetails:
    def __init__(self,cus_id,c_name,balance):
        self.cus_id=cus_id
        self.c_name=c_name
        self.balance=balance

    def wel_msg(self):
        print("Welcome to SBI")

    def dis_details(self):
        print(f'{self.cus_id} - {self.c_name} - {self.balance}')