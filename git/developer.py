from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")
        self.root.configure(bg='#f5f6fa')

        tit_labl=Label(self.root,text="DEVELOPER ",font=("times new roman",35,'bold'),bg='white',fg="darkblue")
        tit_labl.place(x=0,y=0,width=1530,height=45)

# ===============top image=========
        img_top=Image.open(r'clg\3 pr.png')
        img_top=img_top.resize((1530,720))
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)




#  frame
        main_frame=Frame(f_lbl,bd=2,bg='white')
        main_frame.place(x=1000,y=0,width=500,height=600)

# ===============top image=========
        img_top1=Image.open(r'clg\31 pr.png')
        img_top1=img_top1.resize((200,280))
        self.photoimage_top1=ImageTk.PhotoImage(img_top1)
        f_lbl=Label(main_frame,image=self.photoimage_top1)
        f_lbl.place(x=300,y=0,width=200,height=280)



        Label(main_frame, text="Name: Ravi Kumar",
              font=("times new roman", 15, 'bold'),
              bg="white").place(x=50, y=240)

        Label(main_frame, text="App: Face Recognition Attendence System",
              font=("times new roman", 15, 'bold'),
              bg="white").place(x=50, y=280)

        Label(main_frame, text="Course: B-tech (AIML)",
              font=("times new roman", 15, 'bold'),
              bg="white").place(x=50, y=320)

        Label(main_frame, text="Year: 2024-2028",
              font=("times new roman", 15, 'bold'),
              bg="white").place(x=50, y=360)

        Label(main_frame, text="Description:",
              font=("times new roman", 15, 'bold'),
              bg="white").place(x=50, y=400)

        Label(main_frame,
              text="This app is used for student attendance\nusing face recognition technology.",
              font=("times new roman", 15,'bold'),
              bg="white", justify=LEFT).place(x=160, y=400)







if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()