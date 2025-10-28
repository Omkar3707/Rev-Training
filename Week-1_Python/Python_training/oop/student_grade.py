from oop.StudentDetail import StudentDetail
from student_ex_curr import StudExCurr

c_code=int(input('College Code: '))
c_name=input('College Name: ')
rollno = int(input('Enter roll no: '))
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
print(f'{stud.cal_ec()}')
