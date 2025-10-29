from StudentDetail import StudentDetail

class StudExCurr(StudentDetail):
    def __init__(self,c_code,c_name,rollno,sname,m1,m2,m3,ec1,ec2):
        StudentDetail.__init__(self,c_code,c_name,rollno,sname,m1,m2,m3)
        self.ec1=ec1
        self.ec2=ec2

    def cal_ec(self):
        return self.ec1+self.ec2