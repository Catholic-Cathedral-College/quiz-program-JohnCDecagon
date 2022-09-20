from cProfile import label
from email.mime import image
import tkinter as tk
from turtle import back
import PIL

from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('1487x744')
root.title("FalloutQuiz")

#defines the function that will swap from the start menu frame to the quiz frame
def startquiz():
    start_frame.forget()
    quiz_frame.pack()

#defines the frames
start_frame = tk.Frame(root,width=1000, height=1000)
quiz_frame  = tk.Frame(root,width=1000, height=1000)
quiz_frame2 = tk.Frame(root,width=1000, height=1000)
quiz_frame3 = tk.Frame(root,width=1000, height=1000)
quiz_frame4 = tk.Frame(root,width=1000, height=1000)
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

#------------------------------------------------------------------------------
#score value
score = 0

def nextpage():
  quiz_frame.forget()
  quiz_frame2.pack()
  
def restart():
  global score
  if score <= 1:
    score = 0
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
#this is for the correct answer, it adds ten to the score when the correct answer is clicked
def addscore():
  global score
  score += 10
  print(score)
  quiz_frame.forget()
  quiz_frame2.pack()

correctanswer = ImageTk.PhotoImage(Image.open('A1.png'))

canvas2 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton1 = tk.Button(quiz_frame, text = "oihfdoahfawbhuivwaboi", image = correctanswer, command = addscore)
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

BACK = ImageTk.PhotoImage(Image.open('restart.png'))

canvas5 = tk.Canvas(quiz_frame, width = 100, height = 100)
playbutton4 = tk.Button(quiz_frame, text = "oihfdoah", image = BACK, command = restart)
playbutton4.configure(width=300, bg='black')
playbutton_menu4 = canvas2.create_window(50,50)
playbutton4.pack()

playbutton4.place(x=0, y=650)

quiz_frame.pack()

#------------------------------------------------------------------------------

#defines the background image
bg2 = tk.PhotoImage(file = "nextquest.png")

#creates a label, making the background.
LABEL = tk.Label(quiz_frame2, image=bg2,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

#makes the canvas for the background
canvas = tk.Canvas(quiz_frame2, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg2, anchor="nw")

BACK2 = ImageTk.PhotoImage(Image.open('restart.png'))

def goback2():
  global score
  score -= 10
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
  
canvas6 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton5 = tk.Button(quiz_frame2, text = "oihfdoah", image = BACK2, command = goback2)
playbutton5.configure(width=300, bg='black')
playbutton_menu5 = canvas2.create_window(50,50)
playbutton5.pack()

playbutton5.place(x=0, y=650)

def addscore():
  global score
  score += 10
  print(score)
  quiz_frame2.forget()
  quiz_frame3.pack()

def nextpage2():
  quiz_frame2.forget()
  quiz_frame3.pack()

Joshua = ImageTk.PhotoImage(Image.open('Joshua.png'))

canvas7 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton6 = tk.Button(quiz_frame2, text = "oihfdoahfawbhuivwaboi", image = Joshua, command = addscore)
playbutton6.configure(width=500,height=100, bg='black')
playbutton_menu6 = canvas2.create_window(50,50)
playbutton6.pack()

playbutton6.place(x=1000, y=550)

Lanius = ImageTk.PhotoImage(Image.open('Lanius.png'))

canvas8 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton7 = tk.Button(quiz_frame2, text = "oihfdoahfawbhuivwaboi", image = Lanius, command = nextpage2)
playbutton7.configure(width=500,height=100, bg='black')
playbutton_menu7 = canvas2.create_window(50,50)
playbutton7.pack()

playbutton7.place(x=500, y=550)

Vulpes = ImageTk.PhotoImage(Image.open('Vulpes.png'))

canvas9 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton8 = tk.Button(quiz_frame2, text = "oihfdoahfawbhuivwaboi", image = Vulpes, command = nextpage2)
playbutton8.configure(width=500,height=100,bg='black')
playbutton_menu8 = canvas2.create_window(50,50)
playbutton8.pack()

playbutton8.place(x=0, y=550)

quiz_frame2.pack()

#------------------------------------------------------------------------------

bg3 = tk.PhotoImage(file = "Cliffshot.png")

LABEL = tk.Label(quiz_frame3, image=bg3,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(quiz_frame3, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg3, anchor="nw")

B1 = ImageTk.PhotoImage(Image.open('B1.png'))

canvas10 = tk.Canvas(quiz_fram3, width = 100, height = 100)
playbutton9 = tk.Button(quiz_frame3, text = "oihfdoahfawbhuivwaboi", image = Vulpes,)
playbutton9.configure(width=500,height=100,bg='black')
playbutton_menu9 = canvas2.create_window(50,50)
playbutton9.pack()

quiz_frame3.pack()