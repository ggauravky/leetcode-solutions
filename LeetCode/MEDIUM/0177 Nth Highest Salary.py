# 177. Nth Highest Salary
# Medium
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table: Employee

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
 

# Write a solution to find the nth highest distinct salary from the Employee table. If there are less than n distinct salaries, return null.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# | 2  | 200    |
# | 3  | 300    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | 200                    |
# +------------------------+
# Example 2:

# Input: 
# Employee table:
# +----+--------+
# | id | salary |
# +----+--------+
# | 1  | 100    |
# +----+--------+
# n = 2
# Output: 
# +------------------------+
# | getNthHighestSalary(2) |
# +------------------------+
# | null                   |
# +------------------------+

# sql solution:

'''

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      with cte as
      (
          select distinct salary,
          DENSE_RANK() over (order by salary desc) as rnk
          from Employee
      )
      select distinct IFNULL(salary, null) 
      from cte 
      where rnk = N

  );
END

'''




# pandas solution:

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Invalid N → return NULL
    if N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    distinct_salaries = (
        employee['salary']
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )
    
    if N <= len(distinct_salaries):
        nth_salary = distinct_salaries.iloc[N - 1]
    else:
        nth_salary = None
    
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})
