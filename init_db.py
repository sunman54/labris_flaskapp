import os
import psycopg2


class user_connect:
    name= "sunman"
    password= "labris"
    project_name= "labris"
    dbConfig = (f"postgresql://{name}:{password}@localhost/{project_name}")
    # dbConfig = (f"postgresql://{name}:{password}@localhost:{port}/{project_name}")

    conn = psycopg2.connect(
        host="localhost",
        database="labris",
        user='sunman',
        password='labris')

    cur = conn.cursor()
    conn.commit()

conn =  psycopg2.connect(
        host="localhost",
        database="labris",
        user= 'sunman',
        password='labris')

curr = conn.cursor()

"""
cur.execute('DROP TABLE IF EXISTS users;')


cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            
                                 'username varchar (50) NOT NULL,'
            
                                 'firstname varchar (50) NOT NULL,'
                                 'middlename varchar (50),'
                                 'lastname varchar (50) NOT NULL,'
                                 'birthdate date,'
            
                                 'email varchar (150) NOT NULL,'
                                 'password varchar (50) NOT NULL,'
                                 )"""
# INSERT INTO users (username, firstname, middlename, lastname, birthdate, email, password) VALUES ('sunman', 'melih', 'cabir', 'sunman', '1999-09-30', 'm.sunman@yandex.com', 'qwerasdfzxcv');
# INSERT INTO users (username, firstname, lastname, email, password) VALUES ('admin', 'admin', 'admin', 'admin@admin.com', 'passworddd123512');


conn.commit()

