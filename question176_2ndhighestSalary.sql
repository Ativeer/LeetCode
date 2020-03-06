# Write your MySQL query statement below
Select (Select distinct Salary from Employee order by Salary Desc Limit 1 Offset 1) As SecondHighestSalary