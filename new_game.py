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

mainpage_frame = ttk.Frame(app.root)
mainpage_frame.pack()

fontsize = 20

radioValue = IntVar()


def start_game():
    Mahjongg.players[0]["player1"]["name"] = field_player1.get()
    Mahjongg.players[1]["player2"]["name"] = field_player2.get()
    Mahjongg.players[2]["player3"]["name"] = field_player3.get()
    Mahjongg.players[3]["player4"]["name"] = field_player4.get()
    mainpage_frame.destroy()
    from countpage import Points_screen
    Points_screen()

def go_back():
    from mainpage import main_screen2
    main_screen2()

def start_new_game():
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
        mainpage_frame, text="Insert Names", font=("Cambria italic", 30), bg=app.BG_COLOR
    )
    names_label.grid()

    field_player1 = Entry(
        mainpage_frame,
        font=fontsize,
        justify="center",
        borderwidth=4,
        relief="groove",
        highlightbackground=app.BG_COLOR,
    )
    field_player1.insert(0, "Player 1 (EAST)")
    field_player1.grid()

    field_player2 = Entry(
        mainpage_frame, 
        font=fontsize, 
        justify="center", 
        borderwidth=4, 
        relief="groove"
    )
    field_player2.insert(0, "Player 2 (SOUTH)")
    field_player2.grid()

    field_player3 = Entry(
        mainpage_frame, 
        font=fontsize, 
        justify="center", 
        borderwidth=4, 
        relief="groove"
    )
    field_player3.insert(0, "Player 3 (WEST)")
    field_player3.grid()

    field_player4 = Entry(
        mainpage_frame, 
        font=20, 
        justify="center", 
        borderwidth=4, 
        relief="groove"
    )
    field_player4.insert(0, "Player 4 (NORTH)")
    field_player4.grid()

    empty_label = Label(mainpage_frame, text="  ", bg=app.BG_COLOR)
    empty_label.grid()

    start_button = Button(
        mainpage_frame, text="Play Mahjongg", font=("Arial bold", 10), command=start_game
    )
    start_button.grid()


    back_button = Button(
        mainpage_frame, text="Go back", font=("Arial bold", 10), command=go_back
    )
    back_button.grid()
    app.root.mainloop()
