from cProfile import label
from email.mime import image
import tkinter as tk
from turtle import back
import PIL
import pygame
from PIL import ImageTk, Image
from replit import audio


root = tk.Tk()
root.geometry('1487x744')
#keeps track the music button is on/off
global is_on
is_on = True

#defines the function that will swap from the start menu frame to the quiz frame
def startquiz():
    start_frame.forget()
    quiz_frame.pack()

#defines the frames
start_frame = tk.Frame(root,width=1000, height=1000)
quiz_frame  = tk.Frame(root,width=1000, height=1000)

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

#define sound button images
soundbutton = ImageTk.PhotoImage(Image.open('Sound.png'))
soundbuttonoff = ImageTk.PhotoImage(Image.open('Sound.png'))

#defines the switch function, so we can toggle the music player
def switch():
    global is_on

    if is_on:  
        Music.config(image=soundbuttonoff)
        audio.play_file("Doc'sTheme.mp3")
        audio.play_file
        {
    "Paused": True,
    "Doesloop": True,
    "Loopcount":0
        }
    else:
      Music.config(image=soundbutton)
    audio.play_file("Doc'sTheme.mp3")
    audio.play_file
    {
    "Paused": False,
        }

#this is the button to toggle the switch
canvas3 = tk.Canvas(start_frame, width = 100, height = 100)
Music = tk.Button(start_frame, text = "oihfdoahfawbhuivwaboi", image = soundbutton, command = switch)
Music.configure(width=100, bg='black')
Music_menu = canvas3.create_window(50,50)
Music.pack()

Music.place(x=50, y=0)
start_frame.pack()

bg1 = tk.PhotoImage(file = "Fallout.png")

#creates a label, making the background.
LABEL = tk.Label(quiz_frame, image = bg1,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

#makes the canvas for the background
canvas = tk.Canvas(quiz_frame, width=1920, height=1080)
canvas.pack(fill='both', expand=True,)

canvas.create_image(0,-80, image=bg1, anchor="nw")

def goback():
    quiz_frame.forget()
    start_frame.pack()

def switch():
    global is_on

    if is_on:  
        Music.config(image=soundbuttonoff)
        pygame.mixer.music.load("Doc'sTheme.mp3")
        pygame.mixer.music.play(loops=0)
        is_on = False
    else:
       Music.config(image=soundbutton)
       pygame.mixer.music.stop()
       is_on = True

#this is the button to toggle the switch
canvas3 = tk.Canvas(quiz_frame, width = 100, height = 100)
Music = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = soundbutton, command = switch)
Music.configure(width=100, bg='black')
Music_menu = canvas1.create_window(50,50)
Music.pack()

Music.place(x=50, y=0)

quitbutton1 = ImageTk.PhotoImage(Image.open('Quit.png'))

quiz_frame.pack()

root.mainloop()