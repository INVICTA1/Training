# import pymysql
# from pymysql.cursors import DictCursor
# from contextlib import closing  # закрывает соединение с базой
#
# with closing(pymysql.connect(
#         host='127.0.0.1',
#         user='admin',
#         password='admin',
#         database='data',
#
# )) as connection:
#     with connection.cursor() as cursor:
#         request = "SHOW tables"
#
#         cursor.execute(request)  # Для использования команды SQL вызывается метод курсора execute().
#         for database in cursor:
#             print(database[0], end=', ')
#         cursor.execute    ("select version()")
#         version = cursor.fetchone()  # Метод fetchone() позволяет вызвать следующую строку из набора результатов запроса,
#         # показывая только одну запись. В том случае, если доступных данных нет, выводится None.
#         print('\n', cursor, "\n", version)
#         print("Database version: {}".format(version[0]))
#         data = cursor.execute("select * from students")
#         print(data)
#         rows = cursor.fetchall()  # Метод fetchall() позволяет получить все записи. Он возвращает набор результатов.
#         # Технически, это кортеж из кортежей. Каждый из внутренних кортежей представляет собой строку в таблице.
#         for row in rows:
#             print('name:{0}, age:{1} '.format(row[0], row[1]))
#         desc=cursor.description#Названия столбцов представляют собой метаданные. Они извлекаются из объекта курсора.
#
#         print(desc,'\n')
#         print("{0:5} {1:>10}".format(desc[0][0], desc[1][0]))
#         for row in rows:
#             print("{0:3} {1:>10}".format(row[0], row[1]))
table = 'employee'
fields = {'das': 'fsa', 'ger': 'uitr', 'yubgre': 'iutrt'}
key = ''
value = ''
for i, j in fields.items():
    key = key + str(i) + ','
    value = value +str(j) + ','
d='insert into {0}({1}) values({2});'.format(table,key[:-1],value[:-1])
print('\n'+d)