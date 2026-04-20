import json

def On_Launch():
    "Functions that will work at start of the app"
    
    if cfg_read("keepLoggedIn") == "True":
        print("Hızlı giriş yeovvv")
        #will open the main menu
        return
    else:
         LoginPhase()

#Login Service
def LoginPhase():
        LoginScreen_Open().mainloop()

def LoginScreen_Open():
    from ui import LoginScreen
    login = LoginScreen()
    return login

#Register Service
def RegisterPhase():
    "When the register button is clicked, this phase is called."
    RegisterScreen_Open().mainloop()

def RegisterScreen_Open():
    from ui import RegisterScreen
    register = RegisterScreen()
    return register

#JSON etc

def cfg_read(key):
     "Reads and returns the value of key"
     with open("config.json", "r", encoding="utf-8") as file:
          variable = json.load(file)
          return variable[key]

def cfg_write(key, change):
     "Changes the value on key"
     with open("config.json", "r", encoding="utf-8") as file:
          data = json.load(file)
          data[key] = change
     with open("config.json", "w", encoding="utf-8") as file:
          json.dump(data, file, ensure_ascii=False, indent=4)

def cfg_keepLoggedIn(checkbox_var):
    "Changes the config according to the checkbox variable."
    if checkbox_var.get():
        cfg_write("keepLoggedIn", "True")
    else:
        cfg_write("keepLoggedIn", "False")
