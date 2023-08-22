import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="animal"
)
cursor=mydb.cursor()
query="""
create table pets(
id int auto_increment primary key,
age int not null,
gender varchar(100)not null,
breed varchar(200)not null,
location varchar(200)not null,
price int not null
)
"""
cursor.execute(query)