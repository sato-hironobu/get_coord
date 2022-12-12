import pyautogui as pag
import tkinter as tk

def _get_coord():
    pos = pag.position()
    return f"x-coord:{pos.x}\ny-coord:{pos.y}"

class Cursor:
    def __init__(self, parent):
        self.label = tk.Label(parent, text=str(_get_coord()))
        self.label.pack()
        self.label.after(20, self.show)

    def show(self):
        self.label.configure(text=str(_get_coord()))
        self.label.after(20, self.show)

root = tk.Tk()
root.title("Cursor Coordinate")
root.geometry("450x60")
root.attributes("-topmost", True)
cursor = Cursor(root)
root.mainloop()
