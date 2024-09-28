import pandas as pd
import pytest
from sqlalchemy import create_engine,text

# Create MySQL database connection
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')
def test_data_transform_ename_to_upperCase():
    # Read expected data from staging table
    query_expected = """SELECT upper(ename) AS upper_name FROM staging_employee"""
    df_expected = pd.read_sql(query_expected, mysql_engine).astype('str')
    #df_expected = pd.read_sql(query_expected, mysql_engine).astype('str').apply(lambda x: x.str.strip())
    # Read the actual data from the database
    query_actual = """SELECT upper_name FROM employees_details"""
    df_actual = pd.read_sql(query_actual, mysql_engine).astype('str')
    #df_actual = pd.read_sql(query_actual, mysql_engine).astype('str').apply(lambda x: x.str.strip())

    # Ensure the data types and values are as expected
    #df_actual = df_actual.reset_index(drop=True)
    #df_expected = df_expected.reset_index(drop=True)

    # Verify that actual DataFrame matches the expected DataFrame
    assert df_actual.equals(df_expected), "Data Transformation of ename to upper case failed"

def test_data_transform_Joiner():
    # Read expected data from staging table
    query_expected = """SELECT salary + IFNULL(commission, 0) AS total_salary FROM staging_salary"""
    df_expected = pd.read_sql(query_expected, mysql_engine).astype('Int64')

    # Read the actual data from the database
    query_actual = """SELECT total_salary FROM employees_details"""
    df_actual = pd.read_sql(query_actual, mysql_engine).astype('Int64')

    # Ensure the data types and values are as expected
    #df_actual = df_actual.reset_index(drop=True)
    #df_expected = df_expected.reset_index(drop=True)

    # Verify that actual DataFrame matches the expected DataFrame
    assert df_actual.equals(df_expected), "Data Transformation for total_salary logic failed"
