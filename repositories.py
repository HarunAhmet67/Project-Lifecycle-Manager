import sqlite3 as sq
db = 'project.db'

def getUserinfo(username):
    "Returns the user as list, when username is given."
    conn = sq.connect(db)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM useraccounts WHERE username = ?", [username])
    user = cursor.fetchone()
    return user
