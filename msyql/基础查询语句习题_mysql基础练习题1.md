##### 1.
create database wangyu

##### 2.
##### use wangyu

##### 创建雇员表

CREATE TABLE employee (
  empid int(11) NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  sex varchar(255) DEFAULT NULL,
  title varchar(255) DEFAULT NULL,
  birthday date DEFAULT NULL,
  depid int(11) DEFAULT NULL,
  PRIMARY KEY (empid))

##### 创建部门表

  CREATE TABLE department (
  depid int(11) NOT NULL AUTO_INCREMENT,
  depname varchar(255) DEFAULT NULL,
  PRIMARY KEY (depid))

##### 创建工资表

 CREATE TABLE salary (
  empid int(11) NOT NULL AUTO_INCREMENT,
  basesalary int DEFAULT NULL,
  titlesalary int DEFAULT NULL,
  deduction int DEFAULT NULL,
  PRIMARY KEY (empid))



##### 3. 修改表结构
ALTER table department add dptinfo VARCHAR(255)

##### 4. 表中添加记录
insert into employee(empid,name,sex,title,depid,birthday) values(1001,"张三","男","高级工程师",111,"1975-1-1");
insert into employee(empid,name,sex,title,depid,birthday) values(1002,"李四","女","助工",111,"1985-1-1");
insert into employee(empid,name,sex,title,depid,birthday) values(1003,"王五","男","工程师",222,"1978-1-1");
insert into employee(empid,name,sex,title,depid,birthday) values(1004,"赵六","男","工程师",222,"1979-1-1");
insert into department(depid,depname) values(111,"生产部");
insert into department(depid,depname) values(222,"销售部");
insert into department(depid,depname) values(333,"人事部");
insert into salary(empid,basesalary,titlesalary,deduction) values(1001,2200,1100,200);
insert into salary(empid,basesalary,titlesalary,deduction) values(1002,1200,200,100);
insert into salary(empid,basesalary,titlesalary,deduction) values(1003,1900,700,200);
insert into salary(empid,basesalary,titlesalary,deduction) values(1004,1950,700,150);

##### 5. 修改表中的值
update employee set title="工程师" where name="李四"
update salary set basesalary=1700,titlesalary=600 where empid=(select empid from employee where name="李四")

##### 6.删除表中记录
update salary set basesalary=1700,titlesalary=600 where empid=(select empid from employee where name="李四")

##### 7.
SELECT e.name,s.empid,(s.basesalary+s.titlesalary) as "实发工资",(s.basesalary+s.titlesalary-s.deduction) as "应发工资" from employee as e LEFT JOIN salary as s on e.empid=s.empid

##### 8.
select * from employee where year(NOW())-year(birthday) > 40 and name like "张%"

##### 9.
select e.empid,e.name,e.title,d.depname,s.basesalary+s.titlesalary-s.deduction as "实发工资" from employee as e LEFT JOIN salary as s on e.empid=s.empid LEFT JOIN department as d on e.depid=d.depid

##### 10.


