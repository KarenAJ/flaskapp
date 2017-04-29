from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os




#import sys
from sqlalchemy.orm import sessionmaker
from tabledef import *
import sqlite3
datab = 'datab.db'
engine = create_engine('sqlite:///datab.db', echo=True)

app = Flask(__name__)

print ("Engine is created" )

@app.route('/')
def home():
    print ("Inside home")
    return render_template('login.html', msg="")
'''
    if not session.fetch('logged_in'):
        return render_template('login.html')

    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
        '''

@app.route('/login', methods=['GET','POST'])
def login():
    print ("God Is Love: Inside login ", request.method)
    f0=0
    f1=0

    if request.method == 'POST':
        con2 = sqlite3.connect(datab)
        cur2 = con2.cursor()
        cur2.execute("SELECT username, password from users")
        data=cur2.fetchall()
        con2.close()

        for row in data:
            if request.form['username']==row[0]:
                f0=1
                if request.form['password']==row[1]:
                    f1=1
                else:
                    f1=0
            else:
                f0=0
        if f0==0:
            return redirect('/signup')
        else:
            if f1==0:
                return render_template('login.html', msg="Invalid password")
            else:
                return ("Successfully logged in!")
    else:
        return render_template('login.html', msg="")


@app.route('/signup', methods=['GET','POST'])
def signup():
    print ("God Is Love: Inside signup ", request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        con = sqlite3.connect("datab.db")
        cur = con.cursor()
        cur.execute("INSERT INTO Users (username,password) VALUES (?,?)", (username,password))
        con.commit()
        con.close()
        return redirect('/')
    else:
        return render_template('signup.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
