import json
import requests as rq
# import vlc
import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.wm_resizable(width=False, height=False)
root.title("Pokédex👌")

titl = tk.Label(text="🔎The Pokédex", font="Fixedsys 18 bold")
titl.pack()
search = tk.Entry(width=20, font="Fixedsys 12", justify="center")
search.pack(pady=5)
fins = tk.Button(bg="green", fg="#FFFFFF", text="Search...", font="Fixedsys")
fins.pack(pady=10)
root.mainloop()
