import pandas as pd
import pytest
from sqlalchemy import create_engine,text

# Create MySQL database connection
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# 1. Test extract from employees.csv
def test_dataExtractionFromEmployeesFile():
    # Read Expected data from source
    df_expected = pd.read_csv("data/employees.csv")

    query = """SELECT * FROM staging_employee"""

    # read the actual data from the database
    df_actual = pd.read_sql(query, mysql_engine)

    # Verify that actual DataFrame matches the expected DataFrame
    assert df_actual.equals(df_expected), "Data Extraction from employees.csv failed"



 # 2. Test extract from salary.json
def test_dataExtractionFromSalaryFile():
    # Read Expected data from source
    df_expected = pd.read_json("data/salary.json")

    query = """SELECT * FROM staging_salary"""

    # read the actual data from the database
    df_actual = pd.read_sql(query, mysql_engine)

    # Verify that actual DataFrame matches the expected DataFrame
    assert df_actual.equals(df_expected), "Data Extraction from salary.json failed"




