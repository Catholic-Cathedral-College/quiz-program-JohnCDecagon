import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

openfile = tk.Button(root, text="commence forth", fg="white",bg="#263D42")
openfile.pack()

img = ImageTk.PhotoImage(Image.open("FalloutGarage.jpg"))
label = tk.Label(root, image=img)

canvas = tk.Canvas

openfile.place(x=10, y=10)

label.pack()
