import pandas as pd
import pytest
from sqlalchemy import create_engine,text

# Create MySQL database connection
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# 1. Test extract from employees.csv
def test_dataLoading():
    def test_data_transform_Joiner():
        # Read expected data from staging table
        query_expected = """select e.eno,upper(e.ename) upper_name,e.hiredate,s.salary,s.commission,
                            s.salary+ifnull(s.commission,0) total_salary from staging_employee e
                            join staging_salary s on e.eno = s.eno"""
        df_expected = pd.read_sql(query_expected, mysql_engine)

        # Read the actual data from the database
        query_actual = """SELECT * FROM employees_details"""
        df_actual = pd.read_sql(query_actual, mysql_engine)

        # Ensure the data types and values are as expected
        # df_actual = df_actual.reset_index(drop=True)
        # df_expected = df_expected.reset_index(drop=True)

        # Verify that actual DataFrame matches the expected DataFrame
        assert df_actual.equals(df_expected), "Data Transformation for total_salary logic failed"
