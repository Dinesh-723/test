import psycopg2
from psycopg2 import sql
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'dinesh27231'

def connect():
    try:
        connection=psycopg2.connect(
            host= DB_HOST,   
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except Exception as e:
        print(f"error connecting: {e}")
        return
def fetch():
    connection=connect()
    if connection is None:
        return
    cursor = connection.cursor()
    val=('7','cfwwu','236487')

    #cursor.execute("INSERT INTO students (rollno,name,address) VALUES (%s,%s,%s)",val)

    cursor.execute("update students set rollno=4 where rollno=2")

    #cursor.execute("DELETE FROM students WHERE rollno=6")

    cursor.execute("select * from students ")

    res=cursor.fetchall()
    print(res)
    connection.commit
    print(cursor.rowcount, "records found")
    cursor.close()
    connection.close()
fetch()
    

        




