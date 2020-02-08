import pymysql
from pymysql.cursors import DictCursor
from contextlib import closing  # закрывает соединение с базой
import warnings
warnings.filterwarnings('error')

host = '127.0.0.1'
user = 'admin'
password = 'admin'
database = 'data'
show_databases_sql = "SHOW tables"
insert_data_sql = 'insert into employee (FIRST_NAME,last_name,age,sex,income) values(%s,%s,%s,%s,%s)'
update_base_sql = "update employee set income=%s"
create_table_sql = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
            FIRST_NAME  CHAR(20) NOT NULL,
            LAST_NAME  CHAR(20),
            AGE INT,  
            SEX CHAR(1),
            INCOME FLOAT )"""
with closing(pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,

)) as connection:
    with connection.cursor() as cursor:
        def create_table():
            try:
                cursor.execute(create_table_sql)
            except BaseException:
                print("Table  already exists")
                cursor.execute(show_databases_sql)
                for base in cursor:
                    print(base[0])


        def insert_into_table(data):
            cursor.executemany(insert_data_sql, data)


        def update_table(income):

            cursor.executemany(update_base_sql, str(income))


        # data = [('alan', 'woker', 30, 'm', 20054), ('ala', 'poker', 54, 'w', 2054)]
        # insert_into_table(data)
        # update_table(20400)
        if __name__ == "__main__":
            create_table()
