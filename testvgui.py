#----------------------------------------GUI_MERGE-------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys
from PIL import ImageTk,Image

def check1():
    call(["python", "check1.py"])

def check2():
    call(["python", "check2.py"])

def check3():
    call(["python", "check3.py"])

def check4():
    call(["python", "check5.py"])



root = Tk()
root.geometry('990x450')
root.title("BODY-POSE-VIDEO-DETECTION")
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



bg = ImageTk.PhotoImage(Image.open('gui.jpg'))


my_canvas = Canvas(root, width=1000, height=750)
my_canvas.pack(fill='both', expand=True)
#my_canvas.configure(background = 'red')

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(505,50, text='BODY-POSE-DETECTION-VIDEO', font=('Broadway',38),fill='white')
#PaleGreen1
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='ANALYZE 1',height=5, width=60,font=('Broadway',7,BOLD))
btn2 = Button(root, text='ANALYZE 2',height=5, width=60,font=('Broadway',7,BOLD))
btn3 = Button(root, text='ANALYZE 3',height=5, width=60,font=('Broadway',7,BOLD))
btn4 = Button(root, text='ANALYZE 4',height=5, width=60,font=('Broadway',7,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(30,132,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(550,132,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(30,300,anchor='nw', window= btn3)
btn4_window = my_canvas.create_window(550,300,anchor='nw', window= btn4)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=check1)
btn2.configure(command=check2)
btn3.configure(command=check3)
btn4.configure(command=check4)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="gold")
btn2.configure(activebackground="gold")
btn3.configure(activebackground="gold")
btn4.configure(activebackground="gold")

btn1.configure(background="gold")
btn2.configure(background="gold")
btn3.configure(background="gold")
btn4.configure(background="gold")

btn1.configure(width=56)
btn2.configure(width=56)
btn3.configure(width=56)
btn4.configure(width=56)

btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)
btn4.configure(height=5)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")
btn4.configure(pady="1")

#----------------------------------------DETAILING-------------------------------------------------------

btn1.configure(foreground="#000000")
btn2.configure(foreground="#000000")
btn3.configure(foreground="#000000")
btn4.configure(foreground="#000000")

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

my_canvas.configure(highlightbackground="red")

root.mainloop()

