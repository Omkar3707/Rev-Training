from oop.College import College


class StudentDetail(College):
    def __init__(self, c_code, c_name, rollno, sname, m1, m2, m3):
        super().__init__(c_code, c_name)
        self.__rollno = rollno
        self.__sname = sname
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def get_rollno(self):
        return self.__rollno

    def set_rollno(self, rollno):
        self.__rollno = rollno

    def get_sname(self):
        return self.__sname

    def set_sname(self, sname):
        self.__sname = sname

    def get_m1(self):
        return self.__m1

    def set_m1(self, m1):
        self.__m1 = m1

    def set_m2(self, m2):
        self.__m2 = m2

    def get_m3(self):
        return self.__m3

    def set_m3(self, m3):
        self.__m3 = m3

    def cal_total(self):
        return self.__m1 + self.__m2+self.__m3

    def cal_avg(self):
        return self.cal_total()/ 3