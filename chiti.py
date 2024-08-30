from flask import Flask,render_template
import random
app=Flask(__name__)

words=["M.Sujatha", "M.Dinesh", "N.Swathi","N.Naveen", "N.Kishore", "SK.Kayyum", "SK.Ibbu", "SK.Rabbnai", "J.Anusha","J.Sreelatha"]

@app.route('/')
def member():
       return render_template('chiti.html')


@app.route('/chiti', methods=['GET'])
def members():
        genword=random.choice(words)
        return render_template('chiti.html',name=genword)

if __name__=="__main__":
       app.run()