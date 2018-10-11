import mysql.connector

conn = mysql.connector.connect(user='root', password='root123456', database='test')
cursor = conn.cursor()
cursor.execute('create table if not exists user ( id varchar(20) primary key, name varchar(20) )')
cursor.execute('insert into user (id, name) values (%s,%s)',['2','Jack'])
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)

cursor.execute('select * from user where id = %s',('2',))
values = cursor.fetchall()
print(values)
conn.commit()
conn.close()

