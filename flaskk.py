from flask import Flask,render_template,url_for,redirect,request
import psycopg2 
from psycopg2 import sql
app=Flask(__name__)

def connection():
    conn=psycopg2.connect(
        host='localhost',
        database='postgres',
        user='postgres',
        password='dinesh27231'
        )
    return conn



@app.route('/')
def myfun():
    return "form is submited"

@app.route('/Home/<int:id>')
def Home(id):
    x=id+id
    print(x)
    return "the value is %s"%x

@app.route('/temp/<core>')
def temp(core):
    return render_template('hi.html',name=core)

@app.route('/url/<var>')
def url(var):
    if var=='name':
        return redirect(url_for('myfun'))
    else:
        return redirect(url_for('temp'))

@app.route('/register',methods=['GET','POST'])
def user():
    if request.method=='POST':
        phone=request.form['phone']
        email=request.form['email']
        password=request.form['password']
        conn=connection()
        cur=conn.cursor()
        cur.execute("insert into users (phone,email,password) values (%s,%s,%s)", (phone,email,password))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('myfun'))
    return render_template('user.html')

@app.route('/update', methods= ['GET','POST'])
def updateuser():
    if request.method=='POST':
        phone=request.form['phone']
        email=request.form['email']
        password=request.form['password']
        id=request.form['id']
        conn=connection()
        cur=conn.cursor()
        cur.execute("update users set phone=%s, email=%s, password=%s where id=%s", (phone,email,password,id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('fetchuser'))
    return render_template('user.html')

@app.route('/delete', methods=['POST'])
def delete():
    conn=connection()
    cur=conn.cursor()
    id=request.form['id']
    cur.execute('''delete from users where id=%s''',(id))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('fetchuser'))
    
  
@app.route('/fetch')
def fetchuser():
        conn=connection()
        cur=conn.cursor()
        cur.execute("select * from users order by id")
        rows=cur.fetchall()
        cur.close()
        conn.close()
        return render_template('fetch.html',rows=rows)



if __name__=="__main__":
    app.run()