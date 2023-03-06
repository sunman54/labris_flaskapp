from flask import Flask, render_template, request, redirect, session, jsonify
import psycopg2
import datetime
import hashlib
import re

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

from init_db import user_connect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = user_connect.dbConfig
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # primary keys are required by SQLAlchemy

    username = db.Column(db.String(50))

    firstname = db.Column(db.String(50))
    middlename = db.Column(db.String(50))
    lastname = db.Column(db.String(50))

    birthdate = db.Column(db.DateTime())

    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))


def log(text):
    x = datetime.datetime.now()
    x = (x.strftime("%c"))
    with open('logs/log.txt', 'a') as file:
        file.write(x + '\t:\t' + text + '\n')


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login', methods=['POST'])
def login():  # login function
    if not session['logged_in'] :
        username = request.form['username']
        user = Users.query.filter_by(username=username).first()
        hashed_password = hashlib.sha256()
        hashed_password.update(request.form['password'].encode('utf-8'))


        if user:
            user_connect.cur.execute(f"Select password from users where username =  '{username}' ")
            results = user_connect.cur.fetchall()
            password = results[0][0]

            if hashed_password.hexdigest().__eq__(password):  # request.form['password'] == password:
                session['logged_in'] = True
                session['users'] = user.username

                log(username + ' logged in successfully')

                x = datetime.datetime.now()
                time = (x.strftime("%X"))
                date = (x.strftime("%x"))
                user_connect.cur.execute(f"INSERT INTO loged_in_users (username, login_time, login_date) VALUES ('{username}', '{time}', '{date}')")
                user_connect.conn.commit()
                print('login successful ', session['users'])
                return jsonify({'message': 'Login successful!'})
            else:
                log(username + ' did not logged in successfully (password)')

                return jsonify({'message': 'Login failed! (password)'})
        else:
            log(username + ' tried to log in ')

            return jsonify({'message': 'Login failed! (user)'})
    else:
        return jsonify({'message': 'You can not log in again if you already logged in'})

@app.route('/logout', methods=['GET'])
def logout():  # logout function
    if session['logged_in']:
        session['logged_in'] = False
        session.pop('username', None)
        user_connect.cur.execute(f"DELETE FROM loged_in_users WHERE username = '{session['users']}'")
        user_connect.conn.commit()
        print('logged out : ', session['users'])
        return jsonify({'message': 'Logged out!'})
    else:
        return jsonify({'message': 'Did not logged in'})


@app.route('/user/list', methods=['GET'])
def user_list():  # list user function

    userlist = {}

    user_connect.cur.execute(f"Select id, username from users ")
    results = user_connect.cur.fetchall()
    for i in results: userlist[i[0]] = i[1]

    return jsonify(userlist)


@app.route('/user/create', methods=['POST'])
def user_create():  # create new user function

    username = username = request.form['username']
    email = request.form['email']
    mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    password_regex = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

    existing_user = Users.query.filter_by(username=request.form['username']).first()

    if existing_user or len(username) < 6:  # check if its an valid username
        return (f"Username '{request.form['username']}' already exists.")

    elif not re.fullmatch(mail_regex, email):  # Check if email is valid
        return f'This is not a valid email : {email}'

    elif not re.fullmatch(password_regex, request.form['password']):  # Check if password is valid
        return 'Password must be longer than 8 character \n' \
               ' at least one upper and one lower letter ([A-Za-z])\n' \
               ' at least one number and one special character(1234567890 .*?[#?!@$%^&*-) '

    else:
        hashed_password = hashlib.sha256()  # created hashing object
        hashed_password.update(request.form['password'].encode('utf-8'))
        new_user = Users(username=request.form['username'],
                         firstname=request.form['firstname'],
                         middlename=request.form['middlename'],
                         lastname=request.form['lastname'],
                         birthdate=request.form['birthdate'],
                         email=request.form['email'],
                         password=hashed_password.hexdigest())

        user_connect.session.add(new_user)
        user_connect.session.commit()
        return jsonify({'message': 'New user created!'})


@app.route('/user/delete/<int:id>', methods=['GET'])
def user_delete(id):  # delete user function

    user_connect.cur.execute(f"DELETE FROM users WHERE id = '{id}'")
    print(f"DELETE FROM users WHERE id = '{id}'")
    return f'user deleted id : {id}'


@app.route('/user/update/<int:id>', methods=['POST'])
def user_update(id):  # update user's infos function
    return f'user_update {id}'


@app.route('/onlineusers', methods=['GET'])
def online_users():  # show online users function
    return 'online_users'


if __name__ == '__main__':
    app.run(debug=True)
