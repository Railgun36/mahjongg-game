from tkinter.ttk import Label
import mainpage
import tkinter as tk


HEIGHT = 350
WIDTH = 350
bg_color = "#ffefbf"

root = tk.Tk()
root.minsize(WIDTH,HEIGHT)
root.maxsize(WIDTH,HEIGHT)


background_label = tk.Label(root, bg=bg_color)
background_label.place(relheight=1, relwidth=1)

root.title("Mahjongg")





