from astroid.objects import Property

from oop.College import College

class TeacherDetail(College):
    def __init__(self,c_code,c_name,empid,tname,dept):
        College.__init__(self,c_code,c_name)
        self.empid=empid
        self.tname=tname
        self.dept=dept

    def tea_display(self):
        print(f'{self._c_code }\t{self._c_name}'
              f'{self.empid}\n{self.tname}\n{self.dept}')
