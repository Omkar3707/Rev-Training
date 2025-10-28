class Employee:
    def __init__(self,emp_id,e_name,bp):
       self.emp_id = emp_id
       self.e_name = e_name
       self.bp = bp

    def cal_allowance(self):
        return (self.bp*0.1) + (self.bp*0.05)

    def cal_ded(self):
        return self.bp*0.03

    def cal_grosspay(self):
        return self.bp+self.cal_allowance()

    def cal_netpay(self):
        return self.cal_grosspay() - self.cal_ded()
