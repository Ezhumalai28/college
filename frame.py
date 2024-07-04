import sqlite3
import os
from flask import *
app = Flask(__name__)

@app.route('/')
def register():
    return render_template('register.html')

@app.route('/sendlog',methods=['POST'])
def sendlog():
    # database connection the sqlite3
    con = sqlite3.connect('OnlineAttendance.db')
    c = con.cursor()
    uname = request.form['Fname']
    mail = request.form['email']
    psw = request.form['password']
    c.execute("INSERT INTO register (Fname,email,password) VALUES(?,?,?)",(uname,mail,psw))
    con.commit()
    con.close()
    return render_template('home.html')

    # if request.form['Fname'] =='sam' and request.form['password']=='123':
    #     return redirect(url_for("home"))
    # else:
    #     abort(401)

    # if uname == 'Fname' and mail== 'email' and psw == 'password':
    #     return render_template('sendlog.html')
    # else:
    #  return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/ug')
def ug():
    return render_template('UG.html')

@app.route('/pg')
def pg():
    return render_template('PG.html')

@app.route('/research')
def research():
    return render_template('Research.html')

@app.route('/cs')
def openexe():
    os.startfile('D:\\attendance\\Attendence Master Sheet.xlsm')
    return render_template('CS.html')


@app.route('/log')
def log():
    return render_template('Log.html')
    # conn = sqlite3.connect('OnlineAttendance.db')
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM register')
    # if request.form['Fname'] =='ezhuwebtech2812@gmail.com' and request.form['password']=='25354':
    #     return redirect(url_for("/home"))
    # else:
    #     return render_template('Log.html')
    # cursor.close()
    # conn.close()
   
  



# @app.route('/cs',methods=['POST'])
# def cs():
#     # database connection the sqlite3
#     con = sqlite3.connect('OnlineAttendance.db')
#     c = con.cursor()
#
#     sname = request.form['name1']
#     smsg = request.form['samsg']
#
#     c.execute("INSERT INTO csattend (name1,samsg) VALUES(?,?)", (sname, smsg))
#     con.commit()
#     con.close()
#     return render_template('home.html')
#     return render_template('CS.html')




# @app.route('/display')
# def display():
#     return render_template('CS.html')




@app.route('/contact',methods=['POST'])
def contact():
    # database connection the sqlite3
    con = sqlite3.connect('OnlineAttendance.db')
    c = con.cursor()

    Cuname = request.form['Cfname']
    Cmail = request.form['Cemail']
    msg = request.form['message']

    c.execute("INSERT INTO contactas (Cfname,Cemail,message) VALUES(?,?,?)", (Cuname, Cmail, msg))
    con.commit()
    con.close()
    return render_template('home.html')



if __name__=='__main__':
    app.run(debug=True)




