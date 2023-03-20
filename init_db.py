import psycopg2

class user_connect:
    name = "sunman"
    password = "labris"
    project_name = "labris"
    dbConfig = (f"postgresql://{name}:{password}@localhost/{project_name}")
    # dbConfig = (f"postgresql://{name}:{password}@localhost:{port}/{project_name}")

    conn = psycopg2.connect(
        host="localhost",
        database="labris",
        user='sunman',
        password='labris')

    cur = conn.cursor()
    #conn.commit()


conn = psycopg2.connect(
    host="localhost",
    database="labris",
    user='sunman',
    password='labris')

curr = conn.cursor()

conn.commit()
