from game import Mahjongg
from tkinter import ttk, Label, Entry, IntVar, Button, Radiobutton
import app


class Points_screen(Mahjongg):
    def __init__(self):
        self.points_frame = ttk.Frame(app.root)
        self.points_frame.grid()

        self.background_label = Label(self.points_frame, bg=app.BG_COLOR)
        self.background_label.place(relheight=1, relwidth=1)
        self.radioValue = IntVar()

        self.title_label = Label(
            self.points_frame,
            text="Mahjongg",
            font=("Segoe Script", 35),
            bg=app.BG_COLOR,
            fg="#a83232",
        )
        self.title_label.grid(row=0, column=1)

        self.player1_label = Label(
            self.points_frame,
            font=40,
            text=Mahjongg.players[0]["player1"]["name"]
            + " ("
            + Mahjongg.players[0]["player1"]["direction"]
            + "): "
            + str(Mahjongg.players[0]["player1"]["score"]),
            bg=app.BG_COLOR,
        )
        self.player1_label.grid(row=2, column=1)
        self.player1_points = Entry(self.points_frame, font=30, justify="center")
        self.player1_points.insert(0, "0")
        self.player1_points.grid(row=3, column=1)
        self.rdioOne = Radiobutton(
            self.points_frame,
            variable=self.radioValue,
            value=1,
            command=self.activate_calculate,
            bg=app.BG_COLOR,
        )
        self.rdioOne.grid(column=0, row=2)

        self.player2_label = Label(
            self.points_frame,
            font=40,
            text=Mahjongg.players[1]["player2"]["name"]
            + " ("
            + Mahjongg.players[1]["player2"]["direction"]
            + "): "
            + str(Mahjongg.players[1]["player2"]["score"]),
            bg=app.BG_COLOR,
        )
        self.player2_label.grid(row=4, column=1)
        self.player2_points = Entry(self.points_frame, font=30, justify="center")
        self.player2_points.insert(0, "0")
        self.player2_points.grid(row=5, column=1)
        self.rdioTwo = Radiobutton(
            self.points_frame,
            variable=self.radioValue,
            value=2,
            command=self.activate_calculate,
            bg=app.BG_COLOR,
        )
        self.rdioTwo.grid(column=0, row=4)

        self.player3_label = Label(
            self.points_frame,
            font=40,
            text=Mahjongg.players[2]["player3"]["name"]
            + " ("
            + Mahjongg.players[2]["player3"]["direction"]
            + "): "
            + str(Mahjongg.players[2]["player3"]["score"]),
            bg=app.BG_COLOR,
        )
        self.player3_label.grid(row=6, column=1)
        self.player3_points = Entry(self.points_frame, font=30, justify="center")
        self.player3_points.insert(0, "0")
        self.player3_points.grid(row=7, column=1)
        self.rdioThree = Radiobutton(
            self.points_frame,
            variable=self.radioValue,
            value=3,
            command=self.activate_calculate,
            bg=app.BG_COLOR,
        )
        self.rdioThree.grid(column=0, row=6)

        self.player4_label = Label(
            self.points_frame,
            font=40,
            text=Mahjongg.players[3]["player4"]["name"]
            + " ("
            + Mahjongg.players[3]["player4"]["direction"]
            + "): "
            + str(Mahjongg.players[3]["player4"]["score"]),
            bg=app.BG_COLOR,
        )
        self.player4_label.grid(row=8, column=1)
        self.player4_points = Entry(self.points_frame, font=30, justify="center")
        self.player4_points.insert(0, "0")
        self.player4_points.grid(row=9, column=1)
        self.rdioFour = Radiobutton(
            self.points_frame,
            variable=self.radioValue,
            value=4,
            command=self.activate_calculate,
            bg=app.BG_COLOR,
        )
        self.rdioFour.grid(column=0, row=8)

        self.calc_button = Button(
            self.points_frame,
            text="Calculate",
            command=self.calculate,
            state="disabled",
            bg=app.BG_COLOR,
        )
        self.calc_button.grid(column=0, row=10)

        self.rounds_label = Label(
            self.points_frame,
            font=("italic", 12),
            text="Rounds played: " + str(int(str(self.radioValue)[6:]) - 1),
            bg=app.BG_COLOR,
        )
        self.rounds_label.grid(column=1, row=10)

    def new_page(self):  # Goes to new page to insert points
        self.points_frame.destroy()
        Points_screen().calculate

    def activate_calculate(self):  # Activates calculations button
        self.calc_button["state"] = "active"

    def calculate(self):
        points_player1 = int(self.player1_points.get())
        points_player2 = int(self.player2_points.get())
        points_player3 = int(self.player3_points.get())
        points_player4 = int(self.player4_points.get())
        winner_value = self.radioValue.get()
        Mahjongg().get_roundPointsPlayer(
            points_player1, points_player2, points_player3, points_player4, winner_value
        )
        self.new_page()
