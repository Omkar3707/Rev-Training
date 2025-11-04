use RevStudDb

begin transaction;

insert into student values (101,'AAA','qwiuui','hyd',123456);
insert into student values (102,'ACC','shuish','wgl',565342);

select * from student;

save transaction level1;

insert into student (rollno,sname,pin) values
(103,'RRR',876567);
insert into student (sname,pin,rollno)
values ('TrT',564563,104);

save transaction level2;

update student set addr='uppal'
where rollno=103;
rollback transaction level2;
commit transaction;

update student set city='Hyd'
where rollno=103;

delete from student where rollno=104;

truncate table student;

