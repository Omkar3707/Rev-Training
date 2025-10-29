from oop.FinalEval import FinalEval
from oop.StudentDetail import StudentDetail
from student_ex_curr import StudExCurr
from oop.TeacherDetail import TeacherDetail

c_code=int(input('College Code: '))
c_name=input('Enter College Name: ')
rollno = int(input('Enter roll no: '))
name= input('Enter name: ')
m1=int(input('Enter m1: '))
m2=int(input('Enter m2: '))
m3=int(input('Enter m3: '))
ec1=int(input('Enter ec1: '))
ec2=int(input('Enter ec2: '))
empid=int(input('Enter empid: '))
tname=input('Enter tname: ')
dept=input('Enter dept: ')

feed_from_teacher=input('Enter Feedback: ')

finaleval=FinalEval(c_code,c_name,rollno,name,m1,m2,m3,ec1,ec2,empid, tname, dept, feed_from_teacher)

finaleval.col_display()
print(f'{finaleval.col_display()[0]}\t{finaleval.col_display()[1]}'
      f'{finaleval.get_rollno()}\n {finaleval.get_sname()}\n'
      f'{finaleval.cal_total()}\n {finaleval.cal_avg()}\n'
      f'{finaleval.cal_ec()}\n')
finaleval.tea_display()
print(f'{finaleval.feed_from_teacher}')




'''empid=int(input('Enter empid: '))
tname=input('Enter tname: ')
dept=input('Enter dept: ')
c_code=int(input('College Code: '))
c_name=input('College Name: ')

teacher=TeacherDetail(c_code,c_name,empid,tname,dept)

print(f'{teacher.display()}')'''
'''rollno = int(input('Enter roll no: '))
name= input('Enter name: ')
m1=int(input('Enter m1: '))
m2=int(input('Enter m2: '))
m3=int(input('Enter m3: '))
ec1=int(input('Enter ec1: '))
ec2=int(input('Enter ec2: '))

stud = StudExCurr(c_code,c_name,rollno,name,m1,m2,m3,ec1,ec2)

#stud = StudentDetail(c_code,c_name,rollno,name,m1,m2,m3)
print(f'{stud.display()[0]}\t{stud.display()[1]}')
print(f'{stud.get_rollno()}\n{stud.get_sname()}\n{stud.cal_total()}\n{stud.cal_avg()}')
print(f'{stud.cal_ec()}')'''
