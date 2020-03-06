# Write your MySQL query statement below
Select e1.Name AS Employee from Employee e1 join Employee e2 on e1.ManagerId=e2.Id AND e1.Salary>e2.Salary