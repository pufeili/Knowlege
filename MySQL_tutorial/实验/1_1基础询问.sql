#进阶1： 基础查询
/*
语法：
select 查询列表 from 表名称；

类似于： System.out.println(打印东西); 显示

特点： 

1、查询列表可以是：表中的字段、常量值、表达式、函数
2、查询的结果是一个虚拟的表格 
*/
#最开始选择库
USE myemployees;

#1.查询表中的单个字段 
select last_name from employees;

#2.查询表中的多个字段 
select employee_id,first_name,phone_number from employees;

#3.查询表中所有的字段  ctrl+b 快速排版

#方式一 其中``为着重号 用于区别关键字和字段
SELECT 
    `salary`, manager_id, commission_pct, salary, job_id
FROM
    employees;
#方式二 
SELECT * FROM employees;

#4、查询常量
SELECT 100;
SELECT 'john';

#5、查询表达式 
SELECT 100%98;

#6、查询函数 调用该方法得到返回值；
SELECT version();

#7、起别名 
/*
①便于理解 
②如果要查询的字段有重名的情况；使用别名可区分开来
*/
#方式一
SELECT 100%98 as 结果;
SELECT last_name as 姓,first_name as 名 from employees;

#方式二
SELECT last_name 姓,first_name 名 from employees;

#案例： 查询salary,显示结果为out put
SELECT salary as "out put" FROM employees;

#8、去重 

#案例： 查询员工表中涉及的所有部门编号 
SELECT DISTINCT department_id from employees;

#9、+号的作用 

/*

java中的+号： 
①运算符：两个操作数都是数值型 
②连接符：只要有一个操作数为字符型 就位拼接符  

mysql中的+号：
仅仅只有一个功能：运算符 

select 100+90;两个操作数都为数值型，则做加法运算 
select '123'+90;其中一个为字符型，试图将字符型数值转换为数值型， 
						如果转换成功，则继续做加法运算 
SELECT 'john'+90;       如果转换失败，则将字符型数值转换成0 

SELECT null+10; 只要其中一方为null,则结果肯定为null
*/

#案例：查询员工名和姓连接成一个字段，并显示为 姓名 

SELECT concat('a','b','c') AS 结果;

SELECT
		concat(last_name, first_name )AS 姓名
FROM
		employees;

