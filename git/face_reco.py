from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime



class Face_rec:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")
        

        tit_labl=Label(self.root,text="FACE RECOGANIZER ",font=("times new roman",35,'bold'),bg='white',fg="darkred")
        tit_labl.place(x=0,y=0,width=1530,height=45)

        # ===============top image=========
        img_top=Image.open('clg/3 pr.png')
        img_top=img_top.resize((700,700))
        self.photoimage_top=ImageTk.PhotoImage(img_top)
        f_lbl=Label(self.root,image=self.photoimage_top)
        f_lbl.place(x=0,y=55,width=700,height=700)


        #    ===================== bottom immage============
        img_bot=Image.open('clg/21 pr.png')
        img_bot=img_bot.resize((900,700))
        self.photoimage_bot=ImageTk.PhotoImage(img_bot)
        f_lbl=Label(self.root,image=self.photoimage_bot)
        f_lbl.place(x=700,y=55,width=900,height=700)

# ==========================train button================
        b11=Button(f_lbl,text="Recognition" ,cursor='hand2',font=("times new roman",25,'bold'),command=self.face_reco,bg='#10B981',fg="white")
        b11.place(x=580,y=400,width=200,height=50)


# ================== Attendence system ===============
    def mark_att(self,d,r,i,p):
        with open('lol.csv','r+',newline='\n') as f:
            mydata=f.readlines()
            name_list=[]
            for line in mydata:
                entry=line.split((','))
                name_list.append(entry[0])
            if((d not in name_list)) and ((r not in name_list)) and ((i not in name_list)) and ((p not in name_list)) :
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtstr=now.strftime('%H:%M:%S')
                f.writelines(f'\n{d},{r},{i},{p},{dtstr},{d1},present')
 








# =================== face reco==============
    def face_reco(self):
        def draw_boundary(img,classifier,scalefactor,minneigh,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            feature=classifier.detectMultiScale(gray_img,scalefactor,minneigh)

            coor=[]
            for (x,y,w,h) in feature:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
                my_cursor=conn.cursor()

                # my_cursor.execute('select name from student where std_id='+str(id))
                # i=my_cursor.fetchone()
                # i='+'.join(i)

                # my_cursor.execute('select roll from student where std_id='+str(id))
                # r=my_cursor.fetchone()
                # r='+'.join(r)

                # my_cursor.execute('select department from student where std_id='+str(id))
                # p=my_cursor.fetchone()
                # p='+'.join(p)

                # my_cursor.execute('select std_id from student where std_id='+str(id))
                # d=my_cursor.fetchone()
                # d='+'.join(d)
                my_cursor.execute('select name from student where std_id='+str(id))
                i = my_cursor.fetchone()
                i = i[0] if i else "Unknown"

                my_cursor.execute('select roll from student where std_id='+str(id))
                r = my_cursor.fetchone()
                r = r[0] if r else "Unknown"

                my_cursor.execute('select department from student where std_id='+str(id))
                p = my_cursor.fetchone()
                p = p[0] if p else "Unknown"

                my_cursor.execute('select std_id from student where std_id='+str(id))
                d = my_cursor.fetchone()
                d = d[0] if d else "Unknown"



                if confidence > 75:
                    cv2.putText(img,f'std_id:{d}',(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                    cv2.putText(img,f'Roll:{r}',(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                    cv2.putText(img,f'Name:{i}',(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                    cv2.putText(img,f'Department:{p}',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,100,0),2)
                    self.mark_att(d,r,i,p)
                    
                else: 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,'Unknown Face',(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coor=[x,y,w,h]
            return coor
        

        def recog(img,clf,facecascade):
            coor=draw_boundary(img,facecascade,1.1,10,(255,255,255),'face',clf)
            return img
        
        facecascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        
        videocap = cv2.VideoCapture(0)

        while True:
            ret, img = videocap.read()
            if not ret:
                break

            img = recog(img, clf, facecascade)
            cv2.imshow('Welcome to face reco...', img)

    #  PRESS ESC TO STOP
            if cv2.waitKey(1) & 0xFF == 27:
                    break

        videocap.release()
        cv2.destroyAllWindows()

        






if __name__=="__main__":
    root=Tk()
    obj=Face_rec(root)
    root.mainloop() 