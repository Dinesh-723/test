from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)

@app.route('/')
def myfun():
    return "hello this is flask"
@app.route('/Home/<int:id>')
def Home(id):
    a=id+id
    print(a)
    return "the value is %s" %a
@app.route('/temp')
def temp():
    return render_template('hi.html')
@app.route('/url')
def url():
    return redirect(url_for('myfun'))


if __name__=="__main__":
    app.run()