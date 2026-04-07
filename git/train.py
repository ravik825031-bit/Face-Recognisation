from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")




        tit_labl=Label(self.root,text="TRAIN DATA ",font=("times new roman",35,'bold'),bg='white',fg="darkblue")
        tit_labl.place(x=0,y=0,width=1530,height=45)

# ===============top image=========
        img_top=Image.open(r'clg\2 pr.png')
        img_top=img_top.resize((1530,325))
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)


# ==========================train button================
        b11=Button(self.root,text="Train Data" ,command=self.train_cla,cursor='hand2',font=("times new roman",30,'bold'),bg='dark green',fg="white")
        b11.place(x=0,y=380,width=1530,height=60)


    #    ===================== bottom immage============
        img_bot=Image.open(r'clg\3 pr.png')
        img_bot=img_bot.resize((1530,325))
        self.photoimage_bot=ImageTk.PhotoImage(img_bot)
        f_lbl=Label(self.root,image=self.photoimage_bot)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_cla(self):
        data_dir=('data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # convert grey scale image
            imagenp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imagenp)
            ids.append(id)
            cv2.imshow('Progress',imagenp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        # ========== tarin tha c;ssifier+++++++++++=?

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Result','Tranining data completed !!')


















if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()        