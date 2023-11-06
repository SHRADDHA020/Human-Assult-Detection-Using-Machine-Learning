from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys
from PIL import ImageTk,Image

def EMO():
    call(["python", "EMO.py"])

def BT():
    call(["python", "BT.py"])

def GEN():
    call(["python", "GEN.py"])

def PROX():
  call(["python", "PROX.py"])


root = Tk()
root.geometry('1250x550')
root.title('DL Based Human assult detection')
root.resizable(0, 0)

#_fgcolor = "#000000"
_compcolor = "#ffffff"
_a1color = '#ffffff'
_a2color = '#ffffff'


font14 = "-family {Broadway} -size 23 -weight bold -slant "  \
"roman -underline 0 -overstrike 0 "

font16 = "-family {Broadway} -size 36 -weight bold "  \
"-slant roman -underline 0 -overstrike 0"

font9 = "-family {Broadway} -size 19 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"

#bg = Phot

bg = ImageTk.PhotoImage(Image.open('gui.jpg'))



my_canvas = Canvas(root, width=100, height=750)
my_canvas.pack(fill='both', expand=True)
#my_canvas.configure(background = 'red')

my_canvas.create_image(0,0,image = bg, anchor= 'nw')

my_canvas.create_text(640,50, text='DL Based Human Assult Detection', font=('Broadway',38),fill='white')
#my_canvas.configure (640,50, text='DL Based Human Assult Detection', font=('Broadway',38),fill='AliceBlue')

btn1 = Button(root, text='EMOTION DETECTION',height=5, width=500,font=('Broadway',10,BOLD))
btn2 = Button(root, text='BODY MOTION TRACKING',height=5, width=500,font=('Broadway',10,BOLD))
btn3 = Button(root, text='GENDER DETECTION',height=5, width=500,font=('Broadway',10,BOLD))
btn4 = Button(root, text='PROXIMITY ALERT',height=5, width=500,font=('Broadway',10,BOLD))

btn1_window = my_canvas.create_window(200,200,anchor=CENTER, window= btn1)
btn2_window = my_canvas.create_window(1025,200,anchor=CENTER, window= btn2)
btn3_window = my_canvas.create_window(200,440,anchor=CENTER, window= btn3)
btn4_window = my_canvas.create_window(1025,440,anchor=CENTER, window= btn4)


btn1.configure(command=EMO)
btn2.configure(command=BT)
btn3.configure(command=GEN)
btn4.configure(command=PROX)


btn1.configure(activebackground="#d2d1d0")
btn2.configure(activebackground="#d2d1d0")
btn3.configure(activebackground="#d2d1d0")
btn4.configure(activebackground="#d2d1d0")

btn1.configure(background="#646464")
btn2.configure(background="#646464")
btn3.configure(background="#646464")
btn4.configure(background="#646464")

btn1.configure(width=30)
btn2.configure(width=30)
btn3.configure(width=30)
btn4.configure(width=30)

btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)
btn4.configure(height=5)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")
btn4.configure(pady="1")


btn1.configure(foreground="white")
btn2.configure(foreground="white")
btn3.configure(foreground="white")
btn4.configure(foreground="white")

btn1.configure(highlightcolor="black")
btn2.configure(highlightcolor="black")
btn3.configure(highlightcolor="black")
btn4.configure(highlightcolor="black")

btn1.configure(highlightbackground="black")
btn2.configure(highlightbackground="black")
btn3.configure(highlightbackground="black")
btn4.configure(highlightbackground="black")

btn1.configure(activeforeground="white")
btn2.configure(activeforeground="white")
btn3.configure(activeforeground="white")
btn4.configure(activeforeground="white")

btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")
btn4.configure(disabledforeground="#bfbfbf")

my_canvas.configure(highlightbackground="grey")
root.mainloop()
