from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
import os
from train import Train
from face_reco import Face_rec
from attendence import Attendence
from developer import Developer
from help import Help
from time import *
from datetime import datetime


class Face_reco_sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")

# FIRST IMAGER
        img=Image.open(r'clg\2 pr.png')
        img=img.resize((500,130))
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=500,height=130)


# SECOND IMAHGGE 
        img1=Image.open(r'clg\1 pr.png')
        img1=img1.resize((700,130))
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=500,y=0,width=600,height=130)



# THIRD IMGAE
        img2=Image.open(r'clg\2413202.png')
        img2=img2.resize((500,130))
        self.photoimage2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimage2)
        f_lbl.place(x=1100,y=0,width=500,height=130)




# background IMGAE
        img3=Image.open(r'clg\3 pr.png')
        img3=img3.resize((1530,710))
        self.photoimage3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)


# lable tittle 
        tit_labl=Label(bg_img,text="!! FACE RECOGANITION ATTENDENCE SYSTEM !!",font=("times new roman",35,'bold'),bg='white',fg="#E22B71")
        tit_labl.place(x=0,y=0,width=1530,height=45)

 

        # ===================== TIME ======================
        lbl = Label(tit_labl, font=("times new roman",20,'bold'), fg='darkred',bg='white')
        lbl.place(x=0, y=0, width=150, height=50)

        def update_time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text=string)
                lbl.after(1000, update_time)

        update_time()



#student button
        img4=Image.open(r'clg\4 pr.png')
        img4=img4.resize((220,220))
        self.photoimage4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimage4,command=self.stu_details,cursor='hand2')
        b1.place(x=200,y=100,width=220,height=220)

        b11=Button(bg_img,text="Student Details" ,command=self.stu_details,cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white")
        b11.place(x=200,y=300,width=220,height=40)


#detect afcer 
        img5=Image.open(r'clg\5 pr.png')
        img5=img5.resize((220,220))
        self.photoimage5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimage5,cursor='hand2',command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b11=Button(bg_img,text="Face Dtector",cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white",command=self.face_data)
        b11.place(x=500,y=300,width=220,height=40)


#Attendence
        img6=Image.open(r'clg\6 pr.png')
        img6=img6.resize((220,220))
        self.photoimage6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimage6,cursor='hand2',command=self.attend)
        b1.place(x=800,y=100,width=220,height=220)

        b11=Button(bg_img,text="Attendence",cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white",command=self.attend)
        b11.place(x=800,y=300,width=220,height=40)


#help deskl
        img7=Image.open(r'clg\7 pr.png')
        img7=img7.resize((220,220))
        self.photoimage7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimage7,cursor='hand2',command=self.help)
        b1.place(x=1100,y=100,width=220,height=220)

        b11=Button(bg_img,text="Help Desk",cursor='hand2',command=self.help,font=("times new roman",20,'bold'),bg='dark green',fg="white")
        b11.place(x=1100,y=300,width=220,height=40)


#train data
        img8=Image.open(r'clg\8 pr.png')
        img8=img8.resize((220,220))
        self.photoimage8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimage8,cursor='hand2',command=self.train_data)
        b1.place(x=200,y=400,width=220,height=220)

        b11=Button(bg_img,text="Train data",cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white",command=self.train_data)
        b11.place(x=200,y=600,width=220,height=40)


#photos
        img9=Image.open(r'clg\9 pr.png')
        img9=img9.resize((220,220))
        self.photoimage9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimage9,cursor='hand2',command=self.open_img)
        b1.place(x=500,y=400,width=220,height=220)

        b11=Button(bg_img,text="Photo",cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white",command=self.open_img)
        b11.place(x=500,y=600,width=220,height=40)


#developer
        img10=Image.open('clg/10 pr.png')
        img10=img10.resize((220,220))
        self.photoimage10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimage10,command=self.devp,cursor='hand2')
        b1.place(x=800,y=400,width=220,height=220)

        b11=Button(bg_img,text="Developer",command=self.devp,cursor='hand2',font=("times new roman",20,'bold'),bg='dark green',fg="white")
        b11.place(x=800,y=600,width=220,height=40)


#exit
        img11=Image.open('clg/11 pr.jpg')
        img11=img11.resize((220,220))
        self.photoimage11=ImageTk.PhotoImage(img11)
        
        b1=Button(bg_img,image=self.photoimage11,cursor='hand2',command=self.iexit)
        b1.place(x=1100,y=400,width=220,height=220)

        b11=Button(bg_img,text="Exit",cursor='hand2',command=self.iexit,font=("times new roman",20,'bold'),bg='dark green',fg="white")
        b11.place(x=1100,y=600,width=220,height=40)

    def open_img(self):
        os.startfile('data')


#================student details Function button+++++++++
    def stu_details(self):
        self.new_win=Toplevel(self.root)
        self.app=student(self.new_win)



#================tarinig data set Function button+++++++++
    def train_data(self):
        self.new_win=Toplevel(self.root)
        self.app=Train(self.new_win)



#=================== 
    def face_data(self):
        self.new_win=Toplevel(self.root)
        self.app=Face_rec(self.new_win)


#=================== 
    def attend(self):
        self.new_win=Toplevel(self.root)
        self.app=Attendence(self.new_win)


#=================== 
    def devp(self):
        self.new_win=Toplevel(self.root)
        self.app=Developer(self.new_win)

#=================== 
    def help(self):
        self.new_win=Toplevel(self.root)
        self.app=Help(self.new_win)

#=================== 
    def iexit(self):
        self.iexit=messagebox.askyesno('Face recogonistiob','Are you sure to exit !',parent=self.root)
        if self.iexit>0:
            self.root.destroy()
        else:
            return





if __name__=="__main__":
    root=Tk()
    obj=Face_reco_sys(root)
    root.mainloop()        