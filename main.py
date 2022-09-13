from cProfile import label
from email.mime import image
import tkinter as tk
from turtle import back
import PIL

from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('1487x744')

#defines the function that will swap from the start menu frame to the quiz frame
def startquiz():
    start_frame.forget()
    quiz_frame.pack()

#defines the frames
start_frame = tk.Frame(root,width=1000, height=1000)
quiz_frame  = tk.Frame(root,width=1000, height=1000)
quiz_frame2 = tk.Frame(root,width=1000, height=1000)

#defines the background image
bg = tk.PhotoImage(file = "Fallout.png")

#creates a label, making the background.
LABEL = tk.Label(start_frame, image=bg,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

#makes the canvas for the background
canvas = tk.Canvas(start_frame, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg, anchor="nw")

#defines the start button image
startbutton = ImageTk.PhotoImage(Image.open('Start.png'))

#this is the code for the button to start the quiz.
canvas1 = tk.Canvas(start_frame, width = 100, height = 100)
playbutton = tk.Button(start_frame, text = "oihfdoahfawbhuivwaboi", image = startbutton, command = startquiz)
playbutton.configure(width=520, bg='black')
playbutton_menu = canvas1.create_window(10,10)
playbutton.pack()

playbutton.place(x=485, y=425)

#defines the quit button image
quitbutton = ImageTk.PhotoImage(Image.open('Quit.png'))

#this is the code to quit the GUI
canvas2 = tk.Canvas(start_frame, width = 100, height = 100)
playbutton1 = tk.Button(start_frame, text = "oihfdoahfawbhuivwaboi", image = quitbutton, command = root.destroy)
playbutton1.configure(width=520, bg='black')
playbutton_menu1 = canvas2.create_window(50,50)
playbutton1.pack()

playbutton1.place(x=485, y=550)
start_frame.pack()

bg1 = tk.PhotoImage(file = "TheBall.png")

#creates a label, making the background.
LABEL = tk.Label(quiz_frame, image = bg1,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

#makes the canvas for the background
canvas = tk.Canvas(quiz_frame, width=1920, height=1080)
canvas.pack(fill='both', expand=True,)

canvas.create_image(0,0, image=bg1, anchor="nw")

def goback():
    start_frame.pack()
    quiz_frame.forget()

def nextpage():
  quiz_frame.forget()
  quiz_frame2.pack()

quitbutton1 = ImageTk.PhotoImage(Image.open('A1.png'))

canvas2 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton1 = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = quitbutton1, command = nextpage)
playbutton1.configure(width=500, bg='black')
playbutton_menu1 = canvas2.create_window(50,50)
playbutton1.pack()



playbutton1.place(x=0, y=550)

ans2 = ImageTk.PhotoImage(Image.open('Untitled.png'))

canvas3 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton2 = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = ans2, command = nextpage)
playbutton2.configure(width=500, bg='black')
playbutton_menu2 = canvas2.create_window(50,50)
playbutton2.pack()

ans3 = ImageTk.PhotoImage(Image.open('A2.png'))

playbutton2.place(x=500, y=550)

canvas4 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton3 = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = ans3, command = nextpage)
playbutton3.configure(width=500, bg='black')
playbutton_menu3 = canvas2.create_window(50,50)
playbutton3.pack()

playbutton3.place(x=1000, y=550)

BACK = ImageTk.PhotoImage(Image.open('back.png'))

canvas5 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton4 = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = BACK, command = goback)
playbutton4.configure(width=300, bg='black')
playbutton_menu4 = canvas2.create_window(50,50)
playbutton4.pack()

playbutton4.place(x=0, y=650)

quiz_frame.pack()


root.mainloop()