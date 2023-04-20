import sqlite3,os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

con = sqlite3.connect(os.getenv('File'), check_same_thread=False)
cur = con.cursor()

#Client
def Sel_Client(id):
    if id==0:
        return cur.execute('''SELECT * FROM Client''').fetchall()
    else:
        return cur.execute('''SELECT * FROM Client where ID_Client = '''+str(id)).fetchall()

def Ins_Client(Lasstname,Name,Middle_Name,Login,Password,Passport_ID):
    cur.execute('''INSERT INTO Client(Lasstname,Name,Middle_Name,Login,Password,Passport_ID) VALUES(?,?,?,?,?,?)''', (Lasstname,Name,Middle_Name,Login,Password,Passport_ID))
    con.commit()

#Post
def Sel_Post(id):
    if id==0:
        return cur.execute('''SELECT * FROM Post''').fetchall()
    else:
        return cur.execute('''SELECT * FROM Post where ID_Post = '''+str(id)).fetchall()

def Ins_Post(title):
    cur.execute('INSERT INTO Post(Title) VALUES(?)', (title,))
    con.commit()
    return cur.execute('SELECT * FROM Post').fetchall()
