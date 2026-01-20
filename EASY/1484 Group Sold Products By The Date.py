# 1484. Group Sold Products By The Date
# Easy
# Topics
# premium lock icon
# Companies
# SQL Schema
# Pandas Schema
# Table Activities:

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | sell_date   | date    |
# | product     | varchar |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may contain duplicates.
# Each row of this table contains the product name and the date it was sold in a market.
 

# Write a solution to find for each date the number of different products sold and their names.

# The sold products names for each date should be sorted lexicographically.

# Return the result table ordered by sell_date.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Activities table:
# +------------+------------+
# | sell_date  | product     |
# +------------+------------+
# | 2020-05-30 | Headphone  |
# | 2020-06-01 | Pencil     |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | Basketball |
# | 2020-06-01 | Bible      |
# | 2020-06-02 | Mask       |
# | 2020-05-30 | T-Shirt    |
# +------------+------------+
# Output: 
# +------------+----------+------------------------------+
# | sell_date  | num_sold | products                     |
# +------------+----------+------------------------------+
# | 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
# | 2020-06-01 | 2        | Bible,Pencil                 |
# | 2020-06-02 | 1        | Mask                         |
# +------------+----------+------------------------------+
# Explanation: 
# For 2020-05-30, Sold items were (Headphone, Basketball, T-shirt), we sort them lexicographically and separate them by a comma.
# For 2020-06-01, Sold items were (Pencil, Bible), we sort them lexicographically and separate them by a comma.
# For 2020-06-02, the Sold item is (Mask), we just return it.

# Sql sol:

"""

select
    sell_date,
    count(distinct product) as num_sold,
    group_concat(distinct product order by product) as products
from Activities
group by sell_date
order by sell_date;

"""



# pandas sol:
import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()

    grouped = activities.groupby('sell_date')['product'].apply(lambda x: ','.join(sorted(x))).reset_index()

    grouped['num_sold'] = activities.groupby('sell_date')['product'].nunique().values

    result = grouped[['sell_date', 'num_sold', 'product']]
    result = result.rename(columns={'product': 'products'})

    result = result.sort_values(by='sell_date').reset_index(drop=True)

    return result