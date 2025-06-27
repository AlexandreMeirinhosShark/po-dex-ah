import requests as rq
try:
    import vlc
except FileNotFoundError:
    print("VLC media player is not on your device. Please install it or add it to PATH.")
import tkinter as tk
from PIL import ImageTk, Image
from io import BytesIO
from otherwin import toggle_secondary as togl

labelnt_helper=""
labelentd={}
letvar = 0
infolist = []
infoidx = 0
keybtns = []
loflet = [["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
          ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
          ["u", "v", "w", "x", "y", "z", "-", ".", ",", "'"],
          ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]]

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
    global labelnt_helper, infolist, infoidx
    name = labelnt_helper
    screen.itemconfig(gremger, fill="black")
    screen.itemconfig(imager, image="")
    if not name:
        infolbl.config(text="ERROR")
        return

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = rq.get(url)

    if response.status_code == 200:
        data = response.json()
        modname = data["name"].upper()
        typem = data["types"][0]["type"]["name"].upper()
        heig = data["height"] / 10 #meters
        weig = data["weight"] / 10 #kilograms
        image = data["sprites"]["other"]["official-artwork"]["front_default"]

        infolist = [modname, typem, f"{heig}M", f"{weig}KG"]
        print(infolist)
        infolbl.config(text=infolist[infoidx])

        make_sound(name)

        resimg = rq.get(image)
        img = Image.open(BytesIO(resimg.content))
        img = img.resize((130, 130), Image.LANCZOS)
        tkimge = ImageTk.PhotoImage(img)
        screen.image=tkimge
        screen.itemconfig(imager, image=tkimge)
        screen.itemconfig(gremger, fill="#4dbff0", width=1)
    elif response.status_code == 404:
        infolbl.config(text="ERROR")


def toglee(event=None):
    global keybtns, loflet, letvar, labelnt_helper
    togl(root, root2)
    root2c = root2["window"]

    if root2c is None:
        top_part.coords(open_a, 290, 5, 290, 20, 310, 12.5)
    elif root2c is not None:
        top_part.coords(open_a, 310, 5, 310, 20, 290, 12.5)

    if root2c is not None:
        root2c.wm_resizable(width=False, height=False)
        root2c.title("Pokédex👌")
        root2c.config(bg="#c91a1a")
        top_part2 = tk.Canvas(root2c, width=315, height=60, bg="#c91a1a", highlightthickness=0, bd=0)
        top_part2.pack()
        top_part2.create_polygon(0, 0, 315, 0, 315, 60, 171, 60, 139, 25, 0, 25, fill="white", width=0)
        top_part2.create_line(171, 60, 139, 25, fill="#540b0b", width=5)
        top_part2.create_line(140, 25, 0, 25, fill="#540b0b", width=5)
        top_part2.create_line(169.2, 60, 315, 60, fill="#540b0b", width=10)
        label3 = tk.Label(root2c, text="Type Pokémon Name", font="Fixedsys 18 bold", bg="#c91a1a", fg="#ab1616")
        label3.pack()
        labelentd["label"] = tk.Label(root2c, font="Fixedsys 10", bg="black", fg="white", width=31, height=4, text="")
        labelentd["label"].pack(pady=10)
        keybtns=[]
        for i in range(10):
            button_test = tk.Button(root2c, width=5, height=1, bg="#0683c2", font="Fixedsys", command=lambda i=i: typerid(i))
            labelnt_helper=""
            button_test.place(x=32+((i%5)*50), y=200+((i//5)*27))
            keybtns.append(button_test)
        lettering()
        leftbtn = tk.Button(root2c, width=4, height=1, bg="#cfcfcf", text="<", font="Fixedsys 8 bold", fg="red", command=go_left)
        leftbtn.place(x=32, y=290)
        rightbtn = tk.Button(root2c, width=4, height=1, bg="#cfcfcf", text=">", font="Fixedsys 8 bold", fg="red", command=go_right)
        rightbtn.place(x=80, y=290)
        sender = tk.Button(root2c, width=10, height=1, bg="#171717", text="Send", font="Fixedsys 8 bold", fg="white", command=search_pok)
        sender.place(x=32, y=350)
        erasir = tk.Button(root2c, width=10, height=1, bg="#171717", text="Erase", font="Fixedsys 8 bold", fg="white", command=erase)
        erasir.place(x=182, y=350)

        decor2 = tk.Canvas(root2c, width=100, height=60, highlightthickness=0, bd=0, bg="#c91a1a")
        decor2.place(x=182, y=256)
        decor2.create_rectangle(0, 0, 45, 5, fill="#202020", width=2)
        decor2.create_rectangle(55, 0, 100, 5, fill="#202020", width=2)
        decor2.create_oval(99, 59, 74, 34, fill="#ba9609", width=2)
        # test (182, 256) (282, 261)
        # test


def go_right():
    global letvar
    if letvar == 3:
        letvar = 0
    else:
        letvar += 1
    lettering()


def go_left():
    global letvar
    if letvar == 0:
        letvar = 3
    else:
        letvar -= 1
    lettering()


def lettering():
    global keybtns, loflet, letvar
    for j in range(10):
        keybtns[j].config(text=loflet[letvar][j], font="Fixedsys")


def typerid(a):
    global labelnt_helper, loflet, letvar
    labelnt = labelentd["label"]
    labelnt_helper=f"{labelnt_helper}{loflet[letvar][a]}"
    labelnt.config(text=labelnt_helper)


def erase():
    global labelnt_helper
    labelnt=labelentd["label"]
    labelnt_helper=""
    labelnt.config(text="")



def infords(event=None):
    global infoidx, infolist
    try:
        if infoidx == 3:
            infoidx = 0
        else:
            infoidx += 1
        infolbl.config(text=infolist[infoidx])
    except IndexError:
        infolbl.config(text="ERROR")


def blackout(event=None):
    screen.itemconfig(gremger, fill="black")
    screen.itemconfig(imager, image="")
    infolbl.config(text="")


root = tk.Tk()
root.wm_resizable(width=False, height=False)
root.title("Pokédex👌")
root.config(bg="#c91a1a")
root.geometry("315x420")

root2 = {"window": None}

top_part = tk.Canvas(root, width=315, height=60, bg="#c91a1a", highlightthickness=0, bd=0)
top_part.pack()
# Canvas parts start
top_part.create_line(144, 60, 176, 25, fill="#540b0b", width=5)
top_part.create_line(175, 25, 315, 25, fill="#540b0b", width=5)
top_part.create_line(145.8, 60, 0, 60, fill="#540b0b", width=10)
light = top_part.create_oval(9.5, 7.5, 49.5, 47.5, fill="#013e94", outline="white", width=3)
top_part.create_oval(60.5, 7.5, 68.5, 15.5, fill="red", outline="black")
top_part.create_oval(80.5, 7.5, 88.5, 15.5, fill="yellow", outline="black")
top_part.create_oval(100.5, 7.5, 108.5, 15.5, fill="green", outline="black")
# open button
open_a = top_part.create_polygon(290, 5, 290, 20, 310, 12.5, fill="#f2bb07", width=1, outline="black", tags="openeer")
top_part.tag_bind("openeer", "<Button-1>", toglee)
# Canvas parts end
titl = tk.Label(root, text="🔎The Pokédex", font="Fixedsys 18 bold", bg="#c91a1a", fg="#ab1616")
titl.pack()
screen = tk.Canvas(root, width=200, height=170,  bg="#cfcfcf", highlightthickness=0, bd=0)
screen.pack(pady=10)
# screen parts
screen.create_polygon(0, 170, 20, 170, 0, 150, fill="#c91a1a", width=0)
screen.create_oval(80, 10, 85, 15, fill="red")
screen.create_oval(107, 10, 112, 15, fill="red")
screen.create_oval(25, 151.5, 36, 162.5, fill="red")
gremger=screen.create_rectangle(25, 25, 175, 145, fill="black", width=0)
imager=screen.create_image(100, 85)
screen.create_line(175, 150, 150, 150, width=2)
screen.create_line(175, 155, 150, 155, width=2)
screen.create_line(175, 160, 150, 160, width=2)
screen.create_line(175, 165, 150, 165, width=2)
# screen parts end
infolbl = tk.Label(root, width=10, height=3, bg="#08a346", borderwidth=1, relief="solid", font="Fixedsys 9")
infolbl.place(x=85, y=323)
buttonc = tk.Canvas(root, width=80, height=80, highlightthickness=0, bd=0, bg="#c91a1a")
buttonc.place(x=200, y=300)
switchinfo = buttonc.create_polygon(26.667, 0, 53.333, 0, 53.333, 26.667, 80, 26.667, 80, 53.333, 53.333, 53.333, 53.333, 80, 26.667, 80, 26.667, 53.333, 0, 53.333, 0, 26.667, 26.667, 26.667, fill="#202020", tags="informer", width=2, outline="black")
buttonc.create_oval(35, 32, 45, 48, outline="black", width=1)
buttonc.tag_bind("informer", "<Button-1>", infords)
buttonc2 = tk.Canvas(root, width=35, height=35, highlightthickness=0, bd=0, bg="#c91a1a")
buttonc2.place(x=30, y=295)
ternof = buttonc2.create_oval(0, 0, 35, 35, fill="#202020", width=2, tags="turn_off")
buttonc2.tag_bind("turn_off", "<Button-1>", blackout)
decor1 = tk.Canvas(root, width=100, height=5, highlightthickness=0, bd=0, bg="#c91a1a")
decor1.place(x=80, y=293)
decor1.create_rectangle(0, 0, 35, 5, fill="red", width=2)
decor1.create_rectangle(65, 0, 100, 5, fill="royalblue", width=2)

root.mainloop()
