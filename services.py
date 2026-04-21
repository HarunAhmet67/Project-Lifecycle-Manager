import json
from repositories import REPOuseraccounts as R_acc

def On_Launch():
    "Functions that will work at start of the app"
    if FastLogin():
        print("Fast login kachoww")
        HubScreen_Open().mainloop()
    else:
        LoginPhase().mainloop()

#Login Service
def LoginPhase():
    return LoginScreen_Open()

def LoginScreen_Open():
    from ui import LoginScreen
    login = LoginScreen()
    return login

def Check_userAccount(username, password):
     user = R_acc.getUserinfo(username)
     if user != None:
        if password == user[3]:
             return True
        else:
             print("wrong password")
             return False

def FastLogin():
    "Logins instantly if keepLoggedIn is True on config"
    if cfg_read("keepLoggedIn") == "True":
        user = al_GetLastAccountUsed()
        username = user[0]
        password = user[1] 
        if Check_userAccount(username, password):
            return True
        else:
            return False



#Register Service
def RegisterPhase():
    "When the register button is clicked, this phase is called."
    return RegisterScreen_Open()

def RegisterScreen_Open():
    from ui import RegisterScreen
    register = RegisterScreen()
    return register

def sv_RegisterAccount(username, email, password, confirm_password):
    ""
    if RegisterCheck(username, email, password, confirm_password):
        user = []
        user.append(username)
        user.append(email)
        user.append(password)
        print("Register succesful!")
        R_acc.insertUserinfo(user)
        return True
    else:
        print("Register has failed!")
        return False


def RegisterCheck(username, email, password, confirm_password):
    "Checks the conditions of register service"
    if R_acc.usernameTaken(username):
        print("Username has taken!")
        return False
    if "@" not in email:
        print("E-mail is not proper.")
        return False
    if R_acc.emailTaken(email):
        print("E-mail has taken!")
        return False
    if len(password) < 4:
        print("Passwords should have at least 5 characters!")
        return False
    if password != confirm_password:
        print("Passwords do not match!")
        return False
    return True
#The main menu
def HubScreen_Open():
     "Opens the main menu of app"
     from ui import HubScreen
     hub = HubScreen()
     return hub

#JSON etc

def cfg_bool(key):
     "Reads the config and returns the bool of key"
     if cfg_read(key):
          return True
     else:
          return False 
     
def cfg_read(key):
     "Reads the config and returns the value of key"
     with open("config.json", "r", encoding="utf-8") as file:
          variable = json.load(file)
          return variable[key]

def cfg_write(key, change):
     "Changes the value of key on config"
     with open("config.json", "r", encoding="utf-8") as file:
          data = json.load(file)
          data[key] = change
     with open("config.json", "w", encoding="utf-8") as file:
          json.dump(data, file, ensure_ascii=False, indent=4)

def cbx_changeboolconfig(key, cbx_var):
    "Changes the bool variable in config according to the checkbox variable."
    if cbx_var.get():
        cfg_write(key, "True")
    else:
        cfg_write(key, "False")

# "al" stands for accountslogged.
def al_loadData():
    with open("accountslogged.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def al_dumpData(data):
    with open("accountslogged.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def al_AccountExists(username):
     "Searches for the account with username given, and decides if it exists."
     search = username
     data = al_loadData()
     
     for u in data:
          if u["username"] == search:
            return True
     return False
               

def al_SaveAcount(username, password):
     "Saves the accounts logged on this device to json file."
     data = al_loadData()
     if al_AccountExists(username):
        al_UpdateAccountDetails(username, password)
     else:
        new_id = len(data)
        new_user = {"id": new_id, "username": username, "password": password}
        data.append(new_user)
        al_dumpData(data)

def al_GetAccountDetails(username):
    "Searches the accounts logged from username and returns the password"

    if al_AccountExists(username):
        search = username
        data = al_loadData()
        for user in data:
            if user["username"] == search:
                return user
    else:
        print("Account did not found.")

def al_GetLastAccountUsed(data = al_loadData()):
    account = data[0]
    username = account["last_username"]
    password = account["last_password"]
    user = []
    user.append(username)
    user.append(password)
    return user

def al_SaveLastAccountUsed(username):
    data = al_loadData()
    user = al_GetAccountDetails(username)
    id = user["id"]
    name = user["username"]
    password = user["password"]
    data[0]["last_id"] = id
    data[0]["last_username"] = name
    data[0]["last_password"] = password
    al_dumpData(data)

def al_UpdateAccountDetails(username, password):
    data = al_loadData()
    user = al_GetAccountDetails(username, data)
    name = user["username"]
    pw = user["password"]
    index = user["id"]
    if Check_userAccount(name, pw):
        return
    else:
        data[index]["password"] = password
        al_dumpData(data)
