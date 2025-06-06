import tkinter as tk

# Secondary window tracking flag
tracking = False


def toggle_secondary(root, root2_container):
    global tracking
    if root2_container['window'] is None or not tk.Toplevel.winfo_exists(root2_container['window']):
        # Create secondary window
        root2 = tk.Toplevel(root)
        root2.title("Secondary Window")
        root2.geometry("315x420+0+0")
        root2_container['window'] = root2
        tracking = True
        follow_root(root, root2_container)
    else:
        # Destroy secondary window and stop tracking
        root2_container['window'].destroy()
        root2_container['window'] = None
        tracking = False


def follow_root(root, root2_container):
    if tracking and root2_container['window'] is not None and tk.Toplevel.winfo_exists(root2_container['window']):
        root.update_idletasks()
        geo = root.geometry()
        size_pos = geo.split('+')
        size = size_pos[0]
        posx = int(size_pos[1])
        posy = int(size_pos[2])
        width = int(size.split('x')[0])

        new_x = posx + width
        new_y = posy
        root2_container['window'].geometry(f"315x420+{new_x}+{new_y}")

        root.after(50, lambda: follow_root(root, root2_container))


def main():
    root = tk.Tk()
    root.title("Primary Window")
    root.geometry("300x200+100+100")

    root2_container = {'window': None}  # container to hold the secondary window reference

    toggle_btn = tk.Button(root, text="Toggle Secondary Window",
                           command=lambda: toggle_secondary(root, root2_container))
    toggle_btn.pack(pady=50)

    root.mainloop()


if __name__ == '__main__':
    main()
