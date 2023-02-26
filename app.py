import mainpage
import tkinter as tk

#configure db



HEIGHT = 350
WIDTH = 350
BG_COLOR = "#ffefbf"

root = tk.Tk()
root.minsize(WIDTH, HEIGHT)
root.maxsize(WIDTH, HEIGHT)

background_label = tk.Label(root, bg=BG_COLOR)
background_label.place(relheight=1, relwidth=1)

root.title("Mahjongg")
