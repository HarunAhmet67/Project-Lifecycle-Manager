import json
from repositories import getUserinfo

def On_Launch():
    "Functions that will work at start of the app"
    if cfg_read("keepLoggedIn") == "True":
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
     user = getUserinfo(username)
     if password == user[3]:
          print("Password is correct")
          return True
     else:
          print("Password is incorrect")
          return False


#Register Service
def RegisterPhase():
    "When the register button is clicked, this phase is called."
    return RegisterScreen_Open()

def RegisterScreen_Open():
    from ui import RegisterScreen
    register = RegisterScreen()
    return register

#The main menu
def HubScreen_Open():
     "Opens the main menu of app"
     from ui import HubScreen
     hub = HubScreen()
     return hub

#JSON etc

def cfg_bool(key):
     "Reads the config and returns the bool of key"
     if(cfg_read(key)==True):
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

