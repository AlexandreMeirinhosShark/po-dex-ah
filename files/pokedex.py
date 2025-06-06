import json
import requests as rq
try:
    import vlc
except FileNotFoundError:
    print("VLC media player is not on your device. Please install it or add it to PATH.")
import tkinter as tk
from tkinter import messagebox as msg
from PIL import ImageTk, Image
from io import BytesIO
import os
from otherpage import toggle_secondary as togl


def make_sound(nomi):
    # Step 1: Fetch Ditto's form data from PokéAPI
    response = rq.get(f"https://pokeapi.co/api/v2/pokemon/{nomi}")
    response.raise_for_status()
    form_data = response.json()

    # Step 2: Extract the "latest" MP3 cry URL
    cry_url = form_data.get("cries", {}).get("latest")
    if not cry_url:
        raise ValueError("No cry found for the Pokémon.")

    # Step 3: Create VLC instance and play the sound
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(cry_url)
    player.set_media(media)

    # Step 4: Play and wait for it to finish
    player.play()


def search_pok():
    name = search.get().lower().strip()
    if not name:
        msg.showwarning("Empty Input", "Please insert the name of a Pokémon.")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = rq.get(url)

    if response.status_code == 200:
        data = response.json()
        modname = data["name"].upper()
        typem = data["types"][0]["type"]["name"].upper()
        heig = data["height"] / 10
        weig = data["weight"] / 10

        make_sound(name)


def toglee():
    togl(root, root2)

    if root2["window"] is not None:
        label3 = tk.Label(root2['window'], text="Added externally!")
        label3.pack(pady=5)


root = tk.Tk()
root.wm_resizable(width=False, height=False)
root.title("Pokédex👌")
root.config(bg="#e82b00")
root.geometry("315x420")

root2 = {"window": None}

titl = tk.Label(text="🔎The Pokédex", font="Fixedsys 18 bold", bg="#e82b00", fg="#80200a")
titl.pack()
search = tk.Entry(width=20, font="Fixedsys 12", justify="center")
search.pack(pady=5)
find = tk.Button(bg="green", fg="#FFFFFF", text="Search...", font="Fixedsys", command=search_pok)
find.pack(pady=10)
open_b = tk.Button(bg="white", text="teste", command=toglee)
open_b.pack()
imglabel = tk.Label(root, bg="#000000", width=20, height=10)
imglabel.pack(pady=5)
nlabel = tk.Label(root, )
root.mainloop()
