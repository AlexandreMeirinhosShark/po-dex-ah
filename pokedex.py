import json
import requests as rq
# import vlc
import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image
from io import BytesIO
import os

root = tk.Tk()
root.wm_resizable(width=False, height=False)
root.title("Pokédex👌")
root.config(bg="#e82b00")

titl = tk.Label(text="🔎The Pokédex", font="Fixedsys 18 bold", bg="#e82b00", fg="#80200a")
titl.pack()
search = tk.Entry(width=20, font="Fixedsys 12", justify="center")
search.pack(pady=5)
find = tk.Button(bg="green", fg="#FFFFFF", text="Search...", font="Fixedsys")
find.pack(pady=10)
imglabel = tk.Label(root, bg="#e82b00", width=20, height=10)
imglabel.pack(pady=5)
root.mainloop()
