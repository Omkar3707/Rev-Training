create database RevComDb

use RevComDb;

create table department(deptno smallint, dname varchar(3) not null,
constraint pk_deptno primary key(deptno));

create table employee(empno smallint, ename varchar(30) not null,
mgr smallint,sal numeric(10,2),
comm numeric(7,2),deptno smallint,
constraint pk_empno primary key(empno),
constraint fk_deptno foreign key(deptno) references department(deptno));

insert into department values(10,'IT')
insert into department values(11,'HR')
insert into department values(12,'SAL')
insert into department values(13,'Mkt')
insert into department values(14,'OPS')

select*from department;

INSERT INTO employee(empno, ename, mgr, sal, comm, deptno) VALUES
(1001, 'Alice', NULL, 60000.00, NULL, 10),  -- HR
(1002, 'Bob', 1001, 75000.00, NULL, 11),    -- IT
(1003, 'Charlie', 1002, 50000.00, 500.00, 12), -- Sales
(1004, 'Diana', 1003, 52000.00, 300.00, 13),   -- Sales
(1005, 'Ethan', 1002, 58000.00, NULL, 14);  -- Marketing

select*from employee;


select empno as "Emp num",ename as"Name" from employee
where empno!=1002;

select empno as "EMP NO",ename as "Name" from employee
where empno not in (1002,1003,1005);

select empno as "EMP NO",ename as "Name" from employee
where sal between 40000 and 55000;

select empno as "EMP NO",ename as "Name" from employee
where ename LIKE '__a%';


select empno as "EMP NO",ename as "Name" from employee
where ename not in ('alice','fiona');

select empno as "EMP NO",ename as "Name", sal as "Salary" from employee
where sal>50000
order by sal desc;

select empno as "EMP NO",ename as "Name", sal as "Salary", comm as "Commision" from employee
where sal>50000
order by comm,sal desc;

select count(empno) as "No of Employee",
sum(sal) as "Total",avg(comm) as "Average Comm",
min(sal) as "Least Salary",max(sal) as "Top earner" from employee;


select empno as "EMP NO",ename as "Name", sal as "Salary" from employee
where sal>50000
group by deptno,empno,ename,sal;

select deptno as 'Department_no',sum(sal) as 'Total salary' from  employee
group by deptno;


select deptno as 'Department_no',sum(sal) as 'Total salary' from  employee
group by deptno
having sum(sal)>50000;

select deptno as 'Department_no',sum(sal) as 'Total salary' from  employee
where deptno in(10,11,12)
group by deptno
having sum(sal) >=60000
order by sum(sal);

insert into department values (15,'QC')
insert into department values (16,'CC')
insert into employee values (1006,'RAR',1002,65000.00,NULL,NULL),
(1007,'RER',1001,65000.00,NULL,NULL);
select*from employee;

select e.ename,d.dname
from employee e LEFT OUTER join department d
on d.deptno =e.deptno;

select e.ename,d.dname
from employee e Right OUTER join department d
on d.deptno =e.deptno;

select e.ename,d.dname
from employee e full OUTER join department d
on d.deptno =e.deptno;


