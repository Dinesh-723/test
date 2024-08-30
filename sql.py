import psycopg2
from psycopg2 import sql
DB_HOST='localhost'
DB_PORT='5432'
DB_NAME='postgres'
DB_USER='postgres'
DB_PASSWORD='dinesh27231'

def connect():
    try:
        connection=psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection 
    except Exception as e:
        print(f"error connection: {e}")
        return
    
# def fetch():
#     connection=connect()
#     if connection is None:
#         return
#     cursor=connection.cursor()
#     cursor.execute("select * from emp")
#     res=cursor.fetchone()
#     print(res)
#     cursor.close()
#     connection.close()
# fetch()

# connection=connect()
# #if connection is None:
#     #return
# cursor=connection.cursor()
#cursor.execute("CREATE TABLE People (name VARCHAR(250),age int,address VARCHAR(300))")
#     # sep=cursor.fetchall()
#     # print(sep)
# cursor.close()
# connection.close()

def fetch():
    connection=connect()
    if connection is None:
        return
    try:
        connection=connect()
        cursor=connection.cursor()

    # sql=''' CREATE TABLE People(People_id SERIAL PRIMARY KEY,People_name VARCHAR(250) NOT NULL,People_location VARCHAR(250)
    # )'''
        sql=""" INSERT INTO people(people_id,people_name,people_location)VALUES (%s,%s,%s)"""
        val=[(4,'vignesh','guntur'),
             (5,'navven','vijaywada')]
        for i in val:
            cursor.execute(sql,i)
            connection.commit()
            count=cursor.rowcount
            print(count, "record inserted successfully into people table")
    except (Exception, psycopg2.Error) as error:
        print("error while fetching data",error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("connection is closed")

    # cursor.execute(sql)
    # print("Table created successfully")
    # connection.commit()
    # connection.close()
fetch()

