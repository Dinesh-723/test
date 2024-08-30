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
def create():
    connection=connect()
    if connection is None:
       return
    cursor=connection.cursor()
    cursor.execute("CREATE TABLE chiti (id SERIAL not null PRIMARY KEY,Members VARCHAR(250))")
    cursor.execute('''INSERT INTO chiti (Members)VALUES 
             ('M.Sujatha'),
             ('M.Dinesh'),
             ('N.Swathi'),
             ('N.Naveen'),
             ('N.Kishore'),
             ('SK.Kayyum'),
             ('SK.Ibbu'),
             ('SK.Rabbani'),
             ('J.Anusha'),
             ('J.Sreelatha')
     ''')  
    print("table is created successfully..")
    connection.commit()
    cursor.close()
    connection.close()
create()


# def insert():
#     connection=connect()
#     if connection is None:
#         return
#     cursor=connection.cursor()
#     cursor.execute("insert into carsales (company,product,units)values (%s,%s,%s) ('hundai','creta','30')")
#     print("value inserted successfully")
#     connection.commit()
#     cursor.close()
#     connection.close()
# insert()


# def update():
#     connection=connect()
#     cursor=connection.cursor()
#     cursor.execute("update carsales set units='25' where company='hundai'")
#     connection.commit()
#     cursor.close()
#     connection.close()
# update()

# def delet():
#     connection =connect()
#     if connection is None:
#         return
#     cursor=connection.cursor()
# ##     cursor.execute("delete from carsales where company='hundai'")
#     cursor.execute("delete from set units ='25' where company='hundai'")
#     print("row(s) deleted successfully..")
#     connection.commit()
#     cursor.close()
#     connection.close()
# delet()
    
def fetch():
    connection=connect()
    if connection is None:
        return
    cursor=connection.cursor()
    cursor.execute("select * from chiti")
    a=cursor.fetchall()
    print(a)
    cursor.close()
    connection.close()
fetch()


    