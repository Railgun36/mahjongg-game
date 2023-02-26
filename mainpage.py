from game import Mahjongg
from tkinter import ttk, Label, Entry, IntVar, Button
import app
import yaml
import flask
from flask import request, json, jsonify, render_template
from flask_mysqldb import MySQL

db_app = flask.Flask(__name__)
db = yaml.safe_load(open("db.yaml"))
db_app.config["MYSQL_HOST"] = db["mysql_host"]
db_app.config["MYSQL_USER"] = db["mysql_user"]
db_app.config["MYSQL_PASSWORD"] = db["mysql_password"]
db_app.config["MYSQL_DB"] = db["mysql_db"]
mysql = MySQL(db_app)

class MainWindow():

    def __init__(self, master, title, size):
        self.master = master
        self.title = title
        self.size = size
        self.master.title(self.title)
        self.master.geometry(self.size)
mainpage_frame = ttk.Frame(app.root)
mainpage_frame.pack()
fontsize = 20
radioValue = IntVar() 

def new_game():
    mainpage_frame.destroy()
    from new_game import start_new_game
    start_new_game()

def main_screen():    
    background_label = Label(mainpage_frame, bg=app.BG_COLOR)
    background_label.place(relheight=1, relwidth=1)

    title_label = Label(
        mainpage_frame,
        text="Mahjongg",
        font=("Segoe Script", 35),
        bg=app.BG_COLOR,
        fg="#a83232",
    )
    title_label.grid()

    names_label = Label(
        mainpage_frame, 
        text="Please select..", 
        font=("Cambria italic", 30), 
        bg=app.BG_COLOR
    )
    names_label.grid()

    new_button = Button(
        mainpage_frame, 
        text="New Game", 
        font=("Arial bold", 10), 
        command=new_game
    )
    new_button.grid()

    load_button = Button(
        mainpage_frame, 
        text="Load Game", 
        font=("Arial bold", 10), 
        command=new_game
    )
    load_button.grid()


    empty_label = Label(
        mainpage_frame, 
        text="  ", 
        bg=app.BG_COLOR
    )
    empty_label.grid()



    app.root.mainloop()

def main_screen2():   
    background_label = Label(mainpage_frame, bg=app.BG_COLOR)
    background_label.place(relheight=1, relwidth=1)

    title_label = Label(
        mainpage_frame,
        text="Mahjongg",
        font=("Segoe Script", 35),
        bg=app.BG_COLOR,
        fg="#a83232",
    )
    title_label.grid()

    names_label = Label(
        mainpage_frame, 
        text="Please select..", 
        font=("Cambria italic", 30), 
        bg=app.BG_COLOR
    )
    names_label.grid()

    new_button = Button(
        mainpage_frame, 
        text="New Game", 
        font=("Arial bold", 10), 
        command=new_game
    )
    new_button.grid()

    load_button = Button(
        mainpage_frame, 
        text="Load Game", 
        font=("Arial bold", 10), 
        command=new_game
    )
    load_button.grid()

    empty_label = Label(
        mainpage_frame, 
        text="  ", 
        bg=app.BG_COLOR
    )
    empty_label.grid()

    app.root.mainloop()


main_screen2()