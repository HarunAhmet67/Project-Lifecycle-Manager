import sqlite3 as sq
db = 'project.db'


class REPOuseraccounts:
    def getUserinfo(username):
        "Returns the user as list, when username is given."
        conn = sq.connect(db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM useraccounts WHERE username = ?", [username])
        user = cursor.fetchone()

        conn.close()
        if user is None:
            print("User does not exists")
            return
        return user

    def insertUserinfo(user):
        username = user[0]
        email = user[1]
        password = user[2]
        conn = sq.connect(db)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO useraccounts (username, email, password) VALUES (?, ?, ?)", [username, email, password])
        conn.commit()
        conn.close()
    
    def usernameTaken(username):
        conn = sq.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM useraccounts WHERE username = ? LIMIT 1", [username])
        result = cursor.fetchone()

        conn.close()

        if result:
            return True
        else:
            return False
    
    def emailTaken(email):
        conn = sq.connect(db)
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM useraccounts WHERE email = ? LIMIT 1", [email])
        result = cursor.fetchone()
        
        conn.close()

        if result:
            return True
        else:
            return False
