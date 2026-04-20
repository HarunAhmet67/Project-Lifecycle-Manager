import tkinter as tk
from ui_tokens import SizeTokens as sz, SpacingTokens as sp
from services import LoginPhase, RegisterPhase, cfg_keepLoggedIn


class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Account")
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
        self.ent_password = tk.Entry(self, width=sz.l)
        self.cbx_keeplogin = tk.Checkbutton(self, text="Keep logged in", variable=self.var, command=lambda:cfg_keepLoggedIn(self.var))
        self.btn_login = tk.Button(self, text="Login", command=lambda: self.login_Account(), width=sz.m)
        self.btn_create_acc = tk.Button(self, text="Create Account", command=lambda: self.create_Account(), width=sz.m)

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
        print("Log-in succesful!")
        self.destroy()
    
    def create_Account(self):
        self.destroy()
        RegisterPhase()



class RegisterScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Create Account")
        self.geometry("300x300")
        self.minsize(width=300, height=300)

        self.create_Widgets()
        self.setup_Layout()

    def create_Widgets(self):
        "Creates the widgets of UI"
        self.btn_register = tk.Button(self, text="Register", command=lambda: self.register_Account())

    def setup_Layout(self):
        "Places the widgets to UI"
        self.btn_register.pack(pady=20)

    def register_Account(self):
        print("Register succesful!")
        self.destroy()
        LoginPhase()
