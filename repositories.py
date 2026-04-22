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

class REPOservers:
    "Allows reaching the servers, their owners and owner id's."
    def sv_createServer(servername, owner):
        "Creates server"
        conn = sq.connect(db)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO servers (server_name, server_owner) VALUES (?, ?)", [servername, owner])
        conn.commit()
        conn.close()

    def sv_deleteServer():
        "Deletes server"
    
    def sv_getServer():
        "Get server data"
    
class REPOserver_members:
    "Allows reaching the database of members, and their ranks in all servers"
    def svm_addMember():
        "Adds member to a server"

    def svm_removeMember():
        "Removes a member from server"

    def svm_setRank():
        "Sets the rank of member in a server."
    
    def svm_rankCheck():
        "Checks the rank of user, mainly used for controlling the permits."