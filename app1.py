#----------------------------------------GUI_MERGE-------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys

def system():
    call(["python", "system_check.py"])

def pre():
    call(["python", "pre-process.py"])

def Live():
    call(["python", "main.py"])


root = Tk()
root.geometry('790x700')
root.title("EMOTION DETECTOR")
#root.overrideredirect(1)
root.resizable(0, 0)


'''This class configures and populates the toplevel window.
top is the toplevel containing window.'''

#_bgcolor = 'greenyellow'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#ffffff' # X11 color: 'white'
_ana1color = '#ffffff' # X11 color: 'white'
_ana2color = '#ffffff' # X11 color: 'white'
        
font14 = "-family {Broadway} -size 23 -weight bold -slant "  \
"roman -underline 0 -overstrike 0 -"

font16 = "-family {Bahnschrift Light} -size 36 -weight bold "  \
"-slant roman -underline 0 -overstrike 0"

font9 = "-family {Broadway} -size 19 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"

bg = PhotoImage(file= 'back.png')

my_canvas = Canvas(root, width=1000, height=750)
my_canvas.pack(fill='both', expand=True)

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(400,50, text='EMOTION DETECTION', font=('Bahnschrift Light',38),fill='white')
#dark violet
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='SYSTEM CHECK',height=5, width=60,font=('Broadway',12,BOLD))
btn2 = Button(root, text='PRE-PROCESSING',height=5, width=60,font=('Broadway',12,BOLD))
btn3 = Button(root, text='FACE EXPRESSION DETECTION',height=5, width=60,font=('Broadway',12,BOLD))
btn4 = Button(root, text='EXIT',height=5, width=60,font=('Broadway',12,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(70,130,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(70,250,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(70,370,anchor='nw', window= btn3)
btn4_window = my_canvas.create_window(70,493,anchor='nw', window= btn4)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=system)
btn2.configure(command=pre)
btn3.configure(command=Live)
btn4.configure(command=quit)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="dark violet")
btn2.configure(activebackground="dark violet")
btn3.configure(activebackground="dark violet")
btn4.configure(activebackground="dark violet")

btn1.configure(background="dark violet")
btn2.configure(background="dark violet")
btn3.configure(background="dark violet")
btn4.configure(background="dark violet")

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

