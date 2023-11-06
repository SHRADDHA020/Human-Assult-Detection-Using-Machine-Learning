from tkinter import*
import random
import os

def verify():
       filename = 'system_check.py'
       os.system(filename)
       os.system('notepad'+filename)

def pre():
       filename = 'pre-proces.py'
       os.system(filename)
       os.system('notepad'+filename)

def main():
       filename = 'main.py'
       os.system(filename)
       os.system('notepad'+filename)

       
       
def menu():
       root = Tk()
       root.title('Menu')
       root.geometry('1300x570')
       root.config(bg = 'grey')
       
       title_Frame = LabelFrame(root, font = ('Algerian',50,'bold'), width = 1000, height = 100, bg = 'red', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'MENU', font = ('Algerian',30,'bold'), bg = 'red')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #========================================================FRAMES===================================================================
       Frame_1 = LabelFrame(root, font = ('Algerian',17,'bold'), width = 1000, height = 100, bg = 'firebrick1', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 280)
       Frame_2 = LabelFrame(root, font = ('Algerian',17,'bold'), width = 1000, height = 100, bg = 'firebrick1', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 130, pady = 7)
       Frame_3 = LabelFrame(root, font = ('Algerian',17,'bold'), width = 1000, height = 100, bg = 'firebrick1', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, pady = 7)
       Frame_4 = LabelFrame(root, font = ('Algerian',17,'bold'), width = 1000, height = 100, bg = 'yellow', relief = 'ridge', bd = 0)
       Frame_4.grid(row = 4, column = 0, pady = 0)
       


       #========================================================LABELS===================================================================
       Label_1 = Label(Frame_1, text = 'VERIFY SYSTEM', font = ('Algerian',25,'bold'), bg = 'firebrick1')
       Label_1.grid(row = 0, column = 0, padx = 144, pady = 5)
       Label_2 = Label(Frame_2, text = 'PRE-PROCESSING', font = ('Algerian',25,'bold'), bg = 'firebrick1')
       Label_2.grid(row = 0, column = 0, padx = 135, pady = 5)
       Label_3 = Label(Frame_3, text = 'LIVE EXPRESSION DETECTOR', font = ('Algerian',25,'bold'), bg = 'firebrick1')
       Label_3.grid(row = 0, column = 0, padx = 40, pady = 5)
       Label_4 = Label(Frame_4, text = '', font = ('Algerian',25,'bold'), bg = 'yellow')
       Label_4.grid(row = 0, column = 0, padx = 0, pady = 0)
       


       #========================================================BUTTONS===================================================================
       Button_1 = Button(Frame_1, text = 'VERIFY', font = ('Algerian',16,'bold'), width = 8, command = verify)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'PROCESS', font = ('Algerian',16,'bold'), width = 8, command = pre)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'LIVE', font = ('Algerian',16,'bold'), width = 8, command = main)
       Button_3.grid(row = 0, column = 3, padx = 50)
       Button_4 = Button(Frame_4, text = 'EXIT', font = ('Algerian',20,'bold'), width = 8, command = quit)
       Button_4.grid(row = 0, column = 3, padx = 0)
       
       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
