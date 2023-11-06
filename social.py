#----------------------------------------GUI_MERGE-------------------------------------------------------

from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys

def system():
    call(["python", "Menu.py"])

def withmask():
    call(["python", "Social-Distancing.py"])

def bird():
    call(["python", "SocialDistanceDetector.py"])


root = Tk()
root.geometry('750x450')
root.title("CO_LIEUTANENT-87")


'''This class configures and populates the toplevel window.
top is the toplevel containing window.'''

_bgcolor = 'greenyellow'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#ffffff' # X11 color: 'white'
_ana1color = '#ffffff' # X11 color: 'white'
_ana2color = '#ffffff' # X11 color: 'white'
        
font14 = "-family {Fixedsys} -size 23 -weight bold -slant "  \
"roman -underline 0 -overstrike 0"

font16 = "-family {Fixedsys} -size 36 -weight bold "  \
"-slant roman -underline 0 -overstrike 0"

font9 = "-family {Fixedsys} -size 19 -weight normal -slant "  \
"roman -underline 0 -overstrike 0"

bg = PhotoImage(file='E:\Deeraj\PROJECT\CO-L-87\\1151.png')
#E:\Deeraj\PROJECT\CO-L-87

my_canvas = Canvas(root, width=1000, height=750)
my_canvas.pack(fill='both', expand=True)

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(350,50, text='SOCIAL DISTANCING', font=('Fixedsys',26),fill='black')
#PaleGreen1
#CadetBlue3

#-------------------------------------BUTTONS------------------------------------------------------

btn1 = Button(root, text='SOCIAL-DISTANCING-VIDEO',height=5, width=60,font=('Fixedsys',16,BOLD))
btn2 = Button(root, text='SOCIAL-DISTANCING-LIVE ',height=5, width=60,font=('Fixedsys',16,BOLD))
btn3 = Button(root, text='SOCIAL-DISTANCING-BIRD-VIEW ',height=5, width=60,font=('Fixedsys',16,BOLD))

#-------------------------------------POSITION-------------------------------------------------------

btn1_window = my_canvas.create_window(130,100,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(130,200,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(130,300,anchor='nw', window= btn3)

#----------------------------------------WORKING-------------------------------------------------------

btn1.configure(command=system)
btn2.configure(command=withmask)
btn3.configure(command=bird)

#----------------------------------------STYLING-------------------------------------------------------

btn1.configure(activebackground="hot pink")
btn2.configure(activebackground="hot pink")
btn3.configure(activebackground="hot pink")

btn1.configure(background="hot pink")
btn2.configure(background="hot pink")
btn3.configure(background="hot pink")

btn1.configure(width=56)
btn2.configure(width=56)
btn3.configure(width=56)

btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)

btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")

#----------------------------------------DETAILING-------------------------------------------------------

btn1.configure(foreground="#000000")
btn2.configure(foreground="#000000")
btn3.configure(foreground="#000000")

btn1.configure(highlightcolor="black")
btn2.configure(highlightcolor="black")
btn3.configure(highlightcolor="black")

btn1.configure(highlightbackground="greenyellow")
btn2.configure(highlightbackground="greenyellow")
btn3.configure(highlightbackground="greenyellow")

btn1.configure(activeforeground="#000000")
btn2.configure(activeforeground="#000000")
btn3.configure(activeforeground="#000000")

btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")

my_canvas.configure(highlightbackground="red")

root.mainloop()

