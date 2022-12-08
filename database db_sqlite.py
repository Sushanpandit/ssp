"""
import sqlite3
connection = sqlite3.connect('database.db')

connection.execute('drop table if exists staff')
print("Table staff Exists/Drop")
#creating Table

connection.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")
#insert Values
connection.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name 1",21,"M")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name 2",28,"F")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name 3",26,"M")')

connection.commit()
print("Rows are inserted in Table staff Created")

cursor = connection.cursor()

print("Displaying staff Created")
#cursor.execute('select * from staff')
#result = cursor.fetchall()
#result= cursor.fetchone()

result = connection.execute('select * from staff where gender == "M"')
result = connection.execute('select Name,Age from staff')
                            
for rows in result:
    print(rows)
"""
import sqlite3
connection = sqlite3.connect('database.db')

#connection.execute('drop table if exists staff')
#print("Table of the Student")
#creating Table

connection.execute('create table Student(Roll int,Subject text,city text,phone int)')

print("Table Student Created")
#insert Values
conn.execute('insert into Student(Roll,Subject,city,phone) values(0001,"sub 1",21,1234666767)')
conn.execute(' insert into Student(Roll,Subject,city,phone) values(0001,"sub 2",71,1034666767)')
conn.execute('insert into Student(Roll,Subject,city,phone) values(0001,"sub 3",61,1234666767)')

connection.commit()
print("Rows are inserted in Table Student Created")

cursor = connection.cursor()

print("Student info Created")
 
result = connection.execute('select*from Student')
                            
for rows in results:
    print(rows)
