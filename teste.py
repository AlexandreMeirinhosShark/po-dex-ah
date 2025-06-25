import tkinter as tk
from tkinter import font
root = tk.Tk()

# Compact font for labels
compact_font = "TkDefaultFont"

# Compact, centered labels
vers = tk.Label(root, text=f"This is Tcl/Tk version {root.tk.eval('info tclversion')}",
                font=compact_font, padx=0, pady=0, borderwidth=0)
veri = tk.Label(root, text=" This should be a cedilla: ç ",
                font=compact_font, padx=0, pady=0, borderwidth=0)

vers.grid(row=0, column=0, padx=0, pady=0)
veri.grid(row=1, column=0, padx=0, pady=0)

# Center the grid column
root.grid_columnconfigure(0, weight=1)

# Buttons with normal width, but height matching previous label style
btn1 = tk.Button(root, text="Click me!", command=lambda: btn1.config(text=f"[{btn1.cget('text')}]"))
btn2 = tk.Button(root, text="QUIT", command=root.quit)

# Adjust vertical padding to increase button height only
btn1.grid(row=2, column=0, pady=0)
btn2.grid(row=3, column=0, pady=0)

root.mainloop()