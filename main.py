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
final_frame = tk.Frame(root,width=1000, height=1000)
end_frame = tk.Frame(root,width=1000, height=1000)
end_frame1 = tk.Frame(root,width=1000, height=1000)
end_frame2 = tk.Frame(root,width=1000, height=1000)
end_frame3 = tk.Frame(root,width=1000, height=1000)
end_frame4 = tk.Frame(root,width=1000, height=1000)
end_frame5 = tk.Frame(root,width=1000, height=1000)
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
playbutton.configure(width=500, bg='black')
playbutton_menu = canvas1.create_window(10,10)
playbutton.pack()

playbutton.place(x=485, y=425)

#defines the quit button image
quitbutton = ImageTk.PhotoImage(Image.open('Quit.png'))

#this is the code to quit the GUI
canvas2 = tk.Canvas(start_frame, width = 100, height = 100)
playbutton1 = tk.Button(start_frame, text = "oihfdoahfawbhuivwaboi", image = quitbutton, command = root.destroy)
playbutton1.configure(width=500, bg='black')
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

#-----------------------------------Question 1---------------------------------------------
#score value
score = 0

def nextpage():
  quiz_frame.forget()
  quiz_frame2.pack()


  #when restarting the test, it will set the score to zero
def restart():
  global score
  if score <= 1:
    score = 0
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
  quiz_frame4.forget()
  final_frame.forget()
  end_frame.forget()
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
playbutton3.configure(width=480, bg='black')
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

#---------------------------------Question 2-----------------------------------------------

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

#this is also a restart function, it will check if the score is greater than or equal to 1 it will subtract the score by itself, going to zero
def goback():
  global score
  if score >=1:
    score -= score
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
  quiz_frame4.forget()
  end_frame.forget()
  final_frame.forget()

canvas6 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton5 = tk.Button(quiz_frame2, text = "oihfdoah", image = BACK2, command = goback)
playbutton5.configure(width=300, bg='black')
playbutton_menu5 = canvas2.create_window(50,50)
playbutton5.pack()

playbutton5.place(x=0, y=650)

#the score system is quite simple and primitive, but it works well.
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
playbutton6.configure(width=480,height=100, bg='black')
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

#--------------------------------Question 3------------------------------------------------

bg3 = tk.PhotoImage(file = "Cliffshot.png")

LABEL = tk.Label(quiz_frame3, image=bg3,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(quiz_frame3, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg3, anchor="nw")

def addscore():
  global score
  score += 10
  print(score)
  quiz_frame3.forget()
  quiz_frame4.pack()

def nextpage3():
  quiz_frame3.forget()
  quiz_frame4.pack()

def goback():
  global score
  if score >=1:
    score -= score
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
  quiz_frame4.forget()
  end_frame.forget()
  final_frame.forget()
  
B1 = ImageTk.PhotoImage(Image.open('B1.png'))

canvas10 = tk.Canvas(quiz_frame3, width = 100, height = 100)
playbutton9 = tk.Button(quiz_frame3, text = "oihfdoahfawbhuivwaboi", image = B1, command = addscore)
playbutton9.configure(width=500,height=100,bg='black')
playbutton_menu9 = canvas10.create_window(50,50)
playbutton9.pack()
playbutton9.place(x=0, y=550)

B2 = ImageTk.PhotoImage(Image.open('B2.png'))

canvas11 = tk.Canvas(quiz_frame3, width = 100, height = 100)
playbutton10 = tk.Button(quiz_frame3, text = "oihfdoahfawbhuivwaboi", image = B2, command = nextpage3)
playbutton10.configure(width=500,height=100,bg='black')
playbutton_menu10 = canvas11.create_window(50,50)
playbutton10.pack()
playbutton10.place(x=500, y=550)

B3 = ImageTk.PhotoImage(Image.open('B3.png'))

canvas12 = tk.Canvas(quiz_frame3, width = 100, height = 100)
playbutton11 = tk.Button(quiz_frame3, text = "oihfdoahfawbhuivwaboi", image = B3, command = nextpage3)
playbutton11.configure(width=480,height=100,bg='black')
playbutton_menu11 = canvas12.create_window(50,50)
playbutton11.pack()
playbutton11.place(x=1000, y=550)

canvas6 = tk.Canvas(quiz_frame2, width = 100, height = 100)
playbutton5 = tk.Button(quiz_frame2, text = "oihfdoah", image = BACK2, command = goback)
playbutton5.configure(width=300, bg='black')
playbutton_menu5 = canvas2.create_window(50,50)
playbutton5.pack()

BACK3 = ImageTk.PhotoImage(Image.open('restart.png'))

canvas13 = tk.Canvas(quiz_frame3, width = 100, height = 100)
playbutton12 = tk.Button(quiz_frame3, text = "oihfdoah", image = BACK3, command = goback)
playbutton12.configure(width=300, bg='black')
playbutton_menu12 = canvas13.create_window(50,50)
playbutton12.pack()

playbutton12.place(x=0, y=650)

quiz_frame3.pack()

#-----------------------------------Question 4-------------------------------------------------

bg4 = tk.PhotoImage(file = "76.png")

LABEL = tk.Label(quiz_frame4, image=bg4,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(quiz_frame4, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg4, anchor="nw")

def addscore():
  global score
  score += 10
  print(score)
  quiz_frame4.forget()
  final_frame.pack()

def nextpage4():
  quiz_frame4.forget()
  final_frame.pack()

def goback():
  global score
  if score >=1:
    score -= score
  print(score)
  quiz_frame.forget()
  start_frame.pack()
  quiz_frame2.forget()
  quiz_frame3.forget()
  quiz_frame4.forget()
  end_frame.forget()
  final_frame.forget()
TRUE = ImageTk.PhotoImage(Image.open('True.png'))

canvas14 = tk.Canvas(quiz_frame4, width = 100, height = 100)
playbutton13 = tk.Button(quiz_frame4, text = "oihfdoah", image = TRUE, command = addscore)
playbutton13.configure(width=500, bg='black')
playbutton_menu13 = canvas14.create_window(50,50)
playbutton13.pack()

playbutton13.place(x=250, y=550)

FALSE = ImageTk.PhotoImage(Image.open('False.png'))

canvas15 = tk.Canvas(quiz_frame4, width = 100, height = 100)
playbutton14 = tk.Button(quiz_frame4, text = "oihfdoah", image = FALSE, command = nextpage4)
playbutton14.configure(width=500, bg='black')
playbutton_menu14 = canvas15.create_window(50,50)
playbutton14.pack()
playbutton14.place(x=750, y=550)

canvas16 = tk.Canvas(quiz_frame4, width = 100, height = 100)
playbutton15 = tk.Button(quiz_frame4, text = "oihfdoah", image = BACK3, command = goback)
playbutton15.configure(width=300, bg='black')
playbutton_menu15 = canvas16.create_window(50,50)
playbutton15.pack()
playbutton15.place(x=0, y=650)

quiz_frame4.pack()

#-----------------------Question 5----------------------------------------

bg5 = tk.PhotoImage(file = "end.png")

LABEL = tk.Label(final_frame, image=bg5,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(final_frame, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bg5, anchor="nw")

#this is to switch between which ending frame depending on how well you have done on the quiz
def addscore5():
  global score
  score += 10
  print(score)
  if score == 50:
    final_frame.forget()
    end_frame.pack()
  if score == 40:
    final_frame.forget()
    end_frame1.pack()
    
  if score == 30:
    final_frame.forget()
    end_frame2.pack()
    
  if score == 20:
    final_frame.forget()
    end_frame3.pack()
    
  if score == 10:
    final_frame.forget()
    end_frame4.pack()

  if score == 0:
    final_frame.forget()
    end_frame5.pack()

    
def nextpage5():
  final_frame.forget()
  end_frame.pack()
  
yes = ImageTk.PhotoImage(Image.open('Yuppers.png'))

canvas17 = tk.Canvas(final_frame, width = 100, height = 100)
playbutton15 = tk.Button(final_frame, text = "oihfdoah", image = yes, command = nextpage5)
playbutton15.configure(width=500, bg='black')
playbutton_menu15 = canvas16.create_window(50,50)
playbutton15.pack()
playbutton15.place(x=750, y=550)

no = ImageTk.PhotoImage(Image.open('Noing.png'))

canvas16 = tk.Canvas(final_frame, width = 100, height = 100)
playbutton15 = tk.Button(final_frame, text = "oihfdoah", image = no, command = addscore5)
playbutton15.configure(width=500, bg='black')
playbutton_menu15 = canvas16.create_window(50,50)
playbutton15.pack()
playbutton15.place(x=250, y=550)

final_frame.pack()
#--------------------------Final score--------------------------------------

#all of these are frames that hold images pertaining to how much you got correct. if you got 4 out of 5, the if statement will send you to the frame that will show you that you have gotten 4 correct.

#this first frame is if you got 5 out 5 correct
bga = tk.PhotoImage(file = "endingimage1.png")

LABEL = tk.Label(end_frame, image=bga,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bga, anchor="nw")

#the second is if you got 4 out 5
bgb = tk.PhotoImage(file = "endingimage2.png")

LABEL = tk.Label(end_frame1, image=bgb,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame1, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bgb, anchor="nw")
  
#this is if you got 3 out of 5
bgc = tk.PhotoImage(file = "endingimage3.png")

LABEL = tk.Label(end_frame2, image=bgc,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame2, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bgc, anchor="nw")
  
#this is if you got 2 out of 5
bgd = tk.PhotoImage(file = "endingimage4.png")

LABEL = tk.Label(end_frame3, image=bgd,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame3, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bgd, anchor="nw")
  
#this is if you got 1 out 5
bge = tk.PhotoImage(file = "endingimage5.png")

LABEL = tk.Label(end_frame4, image=bge,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame4, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bge, anchor="nw")
  
#this is if you got none of them correct
bgf = tk.PhotoImage(file = "endingimage6.png")

LABEL = tk.Label(end_frame5, image=bgf,width=100,)
LABEL.place(x=0,y=0,relwidth=1, relheight=1)

canvas = tk.Canvas(end_frame5, width=1920, height=1080)
canvas.pack(fill='both',)

canvas.create_image(0,0, image=bgf, anchor="nw")