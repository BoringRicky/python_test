import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table if not exists user (id varchar(20) primary key autoincrement, name varchar(20))')
cursor.execute('insert into user(name) values (\'Michael\')')
rowcount = cursor.rowcount
print(rowcount)

cursor.execute('select * from user where id = ?',('2',))
values = cursor.fetchall()
print(type(values))
print(values)

cursor.close()
conn.commit()
conn.close



