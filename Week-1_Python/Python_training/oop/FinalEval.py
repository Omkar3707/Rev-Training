from student_ex_curr import StudExCurr
from TeacherDetail import TeacherDetail

class FinalEval(StudExCurr,TeacherDetail):
     def __init__(self,c_code,c_name,rollno,sname,m1,m2,m3,ec1,ec2,empid,tname,dept,feed_from_teacher):
         StudExCurr.__init__(self,c_code,c_name,rollno,sname, m1, m2, m3, ec1, ec2)
         TeacherDetail.__init__(self,c_code,c_name,empid,tname,dept)
         self.feed_from_teacher = feed_from_teacher



