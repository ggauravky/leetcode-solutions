# 1907. Count Salary Categories

# Table: Accounts

# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | account_id  | int  |
# | income      | int  |
# +-------------+------+
# account_id is the primary key (column with unique values) for this table.
# Each row contains information about the monthly income for one bank account.
 

# Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

# "Low Salary": All the salaries strictly less than $20000.
# "Average Salary": All the salaries in the inclusive range [$20000, $50000].
# "High Salary": All the salaries strictly greater than $50000.
# The result table must contain all three categories. If there are no accounts in a category, return 0.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Accounts table:
# +------------+--------+
# | account_id | income |
# +------------+--------+
# | 3          | 108939 |
# | 2          | 12747  |
# | 8          | 87709  |
# | 6          | 91796  |
# +------------+--------+
# Output: 
# +----------------+----------------+
# | category       | accounts_count |
# +----------------+----------------+
# | Low Salary     | 1              |
# | Average Salary | 0              |
# | High Salary    | 3              |
# +----------------+----------------+
# Explanation: 
# Low Salary: Account 2.
# Average Salary: No accounts.
# High Salary: Accounts 3, 6, and 8.

# sql solution:

"""

SELECT
  'Low Salary' AS Category,
  SUM(income < 20000) AS accounts_count
FROM Accounts
UNION ALL
SELECT
  'Average Salary' Category,
  SUM(income >= 20000 AND income <= 50000) AS accounts_count
FROM Accounts
UNION ALL
SELECT
  'High Salary' category,
  SUM(income > 50000) AS accounts_count
FROM Accounts;

"""

# pandas solution:
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salary_count = (accounts['income'] < 20000).sum()
    average_salary_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_salary_count = (accounts['income'] > 50000).sum()

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_salary_count, average_salary_count, high_salary_count]
    })

    return result