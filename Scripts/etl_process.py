import pandas as pd
import pytest
from sqlalchemy import create_engine
# database connection string

mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# 1. Extract data from source and load in staging table
df_emp = pd.read_csv("data/employees.csv")
df_emp.to_sql("staging_employee",mysql_engine,if_exists='replace',index=False)

df_sal = pd.read_json("data/salary.json")
df_sal.to_sql("staging_salary",mysql_engine,if_exists='replace',index=False)


# 2.  Transform
# a) convert Employees name to upper case
# b) Replace any null values in commission with 0
# c) Join both the tables based on eno

query = """select e.eno,upper(e.ename) upper_name,e.hiredate,s.salary,s.commission,
s.salary+ifnull(s.commission,0) total_salary from staging_employee e
join staging_salary s on e.eno = s.eno"""

df = pd.read_sql(query,mysql_engine)

# 3. Load
df.to_sql('employees_details',mysql_engine,if_exists='replace',index=False)
