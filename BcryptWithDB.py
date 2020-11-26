import bcrypt
import sqlite3

conn = sqlite3.connect('TEST_DB.db')
c = conn.cursor()

login_email = "test@test.com"
login_password = "test"


with sqlite3.connect('TEST_DB.db') as db:
    c = db.cursor()
    
    
#Encrypt+Salt PWs
hashable_pw = bytes(login_password, 'utf-8')
hashed_pw = bcrypt.hashpw(hashable_pw, bcrypt.gensalt())

insert = 'INSERT INTO Accounts(email_address,password) VALUES(?,?)'
c.execute(insert,[(login_email),(hashed_pw)])

#Send password to DB
    
find_user = ('SELECT * FROM Accounts WHERE email_address = ?')
c.execute(find_user,[(login_email)])

if c.fetchall():
    print('yikes!')
else:
    print("account created")
    insert = 'INSERT INTO Accounts(email_address,password) VALUES(?,?)'
    c.execute(insert,[(login_email),(hashed_pw)])
    conn.commit()


pass_hash = ('SELECT password FROM Accounts WHERE email_address = ?', (login_email),)
pass_hash_fetch = c.fetchall()
pass_hash_result = pass_hash_fetch[0][0]

if bcrypt.checkpw(login_password, pass_hash_result):
    ms.showinfo('Success', 'Successfully Logged in!')
    #redirect to MainApplication
else:
    ms.showerror('Error','Account not found')

