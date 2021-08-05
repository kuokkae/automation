# the script will be part of a daily triggered activity, relies on scraping to be performed that day
#
import pyodbc
import pandas as pd

conn = pyodbc.connect('''DSN=dsn_name;UID=userid;PWD=password''')
table = '''table_name'''

# reads in csv
df = pd.read_csv (r'csv file name')

# prefill any empty value
df["colname"].fillna(0, inplace= True)

# insert table function
def insert_table(table_ref, dbc):
    sql ='''INSERT INTO TABLE_NAME (col_1, col_2, col_3) VALUES(?,?,?)'''
    try:
        with dbc.cursor() as cursor:
            for i, row in df.iterrows():
                cursor.execute(sql, (col_1, col_2, col_3))
                conn.commit()
                print(cursor.rowcount, f"record(s) added, current count {i}")
            # cursor.close()
    except Exception as err:
        dbc.rollback()
        raise err
    conn.close()

# execute function
insert_table(table,conn)
