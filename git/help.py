from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")
        self.root.configure(bg='#f5f6fa')

        tit_labl=Label(self.root,text="HELP DESK",font=("times new roman",35,'bold'),bg='white',fg="darkblue")
        tit_labl.place(x=0,y=0,width=1530,height=45)

# ===============top image=========
        img_top=Image.open(r'clg\3 pr.png')
        img_top=img_top.resize((1530,720))
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)


        d_lable=Label(f_lbl,text="Email: ravik825031@gmail.com",font=("roboto",20,'bold'),bg='#3B82F6',fg='white')
        d_lable.place(x=600,y=150)











if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()