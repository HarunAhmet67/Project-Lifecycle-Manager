import tkinter as tk
from ui_tokens import SizeTokens as sz, SpacingTokens as sp, ColorTokens as c
from services import LoginPhase, RegisterPhase, HubScreen_Open, cbx_changeboolconfig, Check_userAccount


class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Account")
        self.btn_color = c.blue
        self.bg_color = c.silver
        self.config(background=self.bg_color)
        self.geometry("300x300")
        self.minsize(width=300, height=300)
        self.var = tk.IntVar()
        
        self.create_Widgets()
        self.setup_Layout()

    def create_Widgets(self):
        "Creates the widgets of UI"
        self.lbl_username = tk.Label(self, text="Username:")
        self.ent_username = tk.Entry(self, width=sz.l)
        self.lbl_password = tk.Label(self, text="Password")
        self.ent_password = tk.Entry(self, width=sz.l, show="*")
        self.cbx_keeplogin = tk.Checkbutton(self, text="Keep logged in", variable=self.var, command=lambda:cbx_changeboolconfig("keepLoggedIn", self.var), background=self.bg_color)
        self.btn_login = tk.Button(self, text="Login", command=lambda: self.login_Account(), width=sz.m, background=self.btn_color)
        self.btn_create_acc = tk.Button(self, text="Create Account", command=lambda: self.create_Account(), width=sz.m, background=self.btn_color)

    def setup_Layout(self):
        "Places the widgets to UI"
        self.lbl_username.pack(pady=sp.l)
        self.ent_username.pack(pady=sp.sm)
        self.lbl_password.pack(pady=sp.l)
        self.ent_password.pack(pady=sp.sm)
        self.cbx_keeplogin.pack(pady=sp.sm)
        self.btn_login.pack(pady=sp.l)
        self.btn_create_acc.pack(pady=sp.xs)

    def login_Account(self):
        if(Check_userAccount(self.ent_username.get(), self.ent_password.get())) == True:
            HubScreen_Open()
            self.destroy()
    
    def create_Account(self):
        self.destroy()
        RegisterPhase()



class RegisterScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Account")
        self.bg_color = c.silver
        self.btn_color = c.blue
        self.config(background=self.bg_color)
        self.geometry("300x300")
        self.minsize(width=300, height=300)

        self.create_Widgets()
        self.setup_Layout()

    def create_Widgets(self):
        "Creates the widgets of UI"
        self.lbl_username = tk.Label(self, text="Username")
        self.ent_username = tk.Entry(self, width=sz.l)
        self.lbl_email = tk.Label(self, text="E-mail")
        self.ent_email = tk.Entry(self, width=sz.l)
        self.lbl_password = tk.Label(self, text="Password")
        self.ent_password = tk.Entry(self, width=sz.l)
        self.lbl_confpassword = tk.Label(self, text="Confirm Password")
        self.ent_confpassword = tk.Entry(self, width=sz.l)
        self.btn_register = tk.Button(self, text="Register", command=lambda: self.register_Account(), background=self.btn_color)

    def setup_Layout(self):
        "Places the widgets to UI"
        self.lbl_username.pack(pady=sp.sm)
        self.ent_username.pack(pady=sp.xs)
        self.lbl_email.pack(pady=sp.sm)
        self.ent_email.pack(pady=sp.xs)
        self.lbl_password.pack(pady=sp.sm)
        self.ent_password.pack(pady=sp.xs)
        self.lbl_confpassword.pack(pady=sp.sm)
        self.ent_confpassword.pack(pady=sp.xs)
        self.btn_register.pack(pady=sp.l)

    def register_Account(self):
        print("Register succesful!")
        self.destroy()
        LoginPhase()

class HubScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Project Life-cycle Manager")
        self.bg_color = c.silver
        self.btn_color = c.blue
        self.config(background=self.bg_color)
        self.geometry("500x300")
        self.resizable(width=False, height=False)

        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.btn_joinworkplace = tk.Button(self, text="Join Workplace", width=sz.m, height=3, background=self.btn_color)
        self.btn_createworkplace = tk.Button(self, text="Create Workplace", width=sz.m, height=3, background=self.btn_color)

    def setup_layout(self):
        self.btn_joinworkplace.grid(column=0, row=0, pady=sp.m, padx=sp.m)
        self.btn_createworkplace.grid(column=0, row=1, padx=sp.m, pady=sp.m)