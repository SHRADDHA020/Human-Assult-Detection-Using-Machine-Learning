from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
import os
from subprocess import call
import sys
from PIL import ImageTk,Image

def SDD ():
    call(["python",'SDD.py'])

def SD ():
    call(["python",'SD.py'])

def PROXY():
    call(["python",'proxi_video.py'])


root =Tk()
root.geometry ('1250x550')
root.title('Proximity alert')
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

bg = ImageTk.PhotoImage(Image.open('4.jpg'))

my_canvas = Canvas(root, width=100, height=750)
my_canvas.pack(fill='both', expand=True)
#my_canvas.configure(background = 'red')

my_canvas.create_image(0,0,image = bg, anchor='nw')

my_canvas.create_text(640,50, text='PROXIMITY-ALERT', font=('Broadway',38),fill='yellow')

btn1 = Button(root, text='SOCIAL DISTANCE DETECTOR',height=5, width=60,font=('Broadway',10,BOLD))
btn2 = Button(root, text='SOCIAL DISTANCE ALERT',height=5, width=60,font=('Broadway',10,BOLD))
btn3 = Button(root, text='PROXIMITY VIDEO',height=5, width=60,font=('Broadway',10,BOLD))


btn1_window = my_canvas.create_window(30,132,anchor='nw', window= btn1)
btn2_window = my_canvas.create_window(840,132,anchor='nw', window= btn2)
btn3_window = my_canvas.create_window(440,300,anchor='nw', window= btn3)



btn1.configure(command=SDD)
btn2.configure(command=SD)
btn3.configure(command=PROXY)


btn1.configure(activebackground="grey")
btn2.configure(activebackground="grey")
btn3.configure(activebackground="grey")


btn1.configure(background="#EAECEE")
btn2.configure(background="#EAECEE")
btn3.configure(background="#EAECEE")


btn1.configure(width=36)
btn2.configure(width=36)
btn3.configure(width=36)


btn1.configure(height=5)
btn2.configure(height=5)
btn3.configure(height=5)


btn1.configure(pady="1")
btn2.configure(pady="1")
btn3.configure(pady="1")



btn1.configure(foreground="black")
btn2.configure(foreground="black")
btn3.configure(foreground="black")


btn1.configure(highlightcolor="white")
btn2.configure(highlightcolor="white")
btn3.configure(highlightcolor="white")


btn1.configure(highlightbackground="greenyellow")
btn2.configure(highlightbackground="greenyellow")
btn3.configure(highlightbackground="greenyellow")


btn1.configure(activeforeground="white")
btn2.configure(activeforeground="white")
btn3.configure(activeforeground="white")


btn1.configure(disabledforeground="#bfbfbf")
btn2.configure(disabledforeground="#bfbfbf")
btn3.configure(disabledforeground="#bfbfbf")


my_canvas.configure(highlightbackground="grey")
root.mainloop()
