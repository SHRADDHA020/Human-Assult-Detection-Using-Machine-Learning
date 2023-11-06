#----------------------------------------GUI_MERGE-------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys
from PIL import ImageTk,Image

def DETECT():
    call(["python", "DETECT.py"])

def V_GUI():
    call(["python", "V_GUI.py"])

def ANGLE():
    call(["python", "ANGLE.py"])

def CURLS():
    call(["python", "CURLS.py"])



root = Tk()
root.geometry('1250x550')
root.title("BODY-POSE-DETECTION")
root.resizable(0, 0)
#root.overrideredirect(1)


'''This class configures and populates the toplevel window.
top is the toplevel containing window.'''

#_bgcolor = 'greenyellow'  # X11 color: 'gray85'
#_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#ffffff' # X11 color: 'white'
_ana1color = '#ffffff' # X11 color: 'white'
_ana2color = '#ffffff' # X11 color: 'white'
        
font14 = "-family {Broadway} -size 23 -weight bold -slant "  \
"roman -underline 0 -overstrike 0"

font16 = "-family {Broadway} -size 36 -weight bold "  \
"-slant roman -underline 0 -overstrike 0"

font9 = "-family {Broadway} -size 19 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"

bg = ImageTk.PhotoImage(Image.open('3.jpg'))


my_canvas = Canvas(root, width=1000, height=750)
my_canvas.pack(fill='both', expand=True)
#my_canvas.configure(background = 'red')

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(640,50, text='BODY-POSE-DETECTION', font=('Broadway',38),fill='yellow')
#PaleGreen1
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='DETECT BODY ACTION',height=5, width=60,font=('Broadway',10,BOLD))
btn2 = Button(root, text='VIDEO ANALYSIS',height=5, width=60,font=('Broadway',10,BOLD))
btn3 = Button(root, text='DETECT ANGLE',height=5, width=60,font=('Broadway',10,BOLD))
btn4 = Button(root, text='CURLS COUNTING',height=5, width=60,font=('Broadway',10,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(30,150,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(810,150,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(30,350,anchor='nw', window= btn3)
btn4_window = my_canvas.create_window(810,350,anchor='nw', window= btn4)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=DETECT)
btn2.configure(command=V_GUI)
btn3.configure(command=ANGLE)
btn4.configure(command=CURLS)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="#840000")
btn2.configure(activebackground="#840000")
btn3.configure(activebackground="#840000")
btn4.configure(activebackground="#840000")

btn1.configure(background="#840000")
btn2.configure(background="#840000")
btn3.configure(background="#840000")
btn4.configure(background="#840000")

btn1.configure(width=40)
btn2.configure(width=40)
btn3.configure(width=40)
btn4.configure(width=40)

btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)
btn4.configure(height=5)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")
btn4.configure(pady="1")

#----------------------------------------DETAILING-------------------------------------------------------

btn1.configure(foreground="White")
btn2.configure(foreground="White")
btn3.configure(foreground="White")
btn4.configure(foreground="White")

btn1.configure(highlightcolor="black")
btn2.configure(highlightcolor="black")
btn3.configure(highlightcolor="black")
btn4.configure(highlightcolor="black")

btn1.configure(highlightbackground="greenyellow")
btn2.configure(highlightbackground="greenyellow")
btn3.configure(highlightbackground="greenyellow")
btn4.configure(highlightbackground="greenyellow")

btn1.configure(activeforeground="#000000")
btn2.configure(activeforeground="#000000")
btn3.configure(activeforeground="#000000")
btn4.configure(activeforeground="#000000")

btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")
btn4.configure(disabledforeground="#bfbfbf")

my_canvas.configure(highlightbackground="#840000")

root.mainloop()

