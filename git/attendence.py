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
import csv
from tkinter import filedialog


mydata=[]

class Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")


# ====================text variable ==============
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendence=StringVar()

        # firts image 
        img=Image.open(r'clg\1 pr.png')
        img=img.resize((800,200))
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=800,height=200)


# SECOND IMAHGGE 
        img1=Image.open(r'clg\2 pr.png')
        img1=img1.resize((800,200))
        self.photoimage1=ImageTk.PhotoImage(img1)
        f_lbl=Label(self.root,image=self.photoimage1)
        f_lbl.place(x=800,y=0,width=800,height=200)


# ============== bg imagew ==========
        img3=Image.open(r'clg\3 pr.png')
        img3=img3.resize((1530,600))
        self.photoimage3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimage3)
        bg_img.place(x=0,y=200,width=1530,height=600)



# lable tittle 
        tit_labl=Label(bg_img,text="--ATTENDENCE--",font=("times new roman",35,'bold'),bg='white',fg="darkgreen")
        tit_labl.place(x=0,y=0,width=1530,height=45)

# frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)


# left side lablew frame 
        l_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Attendence Information',font=("times of roman",15,'bold'),fg="dark blue")
        l_frame.place(x=10,y=10,width=730,height=580)
        img_left=Image.open(r'clg\4 pr.png')
        img_left=img_left.resize((720,130))
        self.photoimage_l=ImageTk.PhotoImage(img_left)
        f_lbl=Label(l_frame,image=self.photoimage_l)
        f_lbl.place(x=5,y=0,width=720,height=130)

        leftin_frame=Frame(l_frame,bd=2,relief=RIDGE)
        leftin_frame.place(x=0,y=135,width=720,height=350)


        # ============lable aND ENTRY==========

        id_lable=Label(leftin_frame,text="Attendence ID:",font=("times of roman",12,'bold'))
        id_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
    # entery 
        id_entry=ttk.Entry(leftin_frame,textvariable=self.var_id,font=("times of roman",12,'bold'),width=20)
        id_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        # roll
        n_lable=Label(leftin_frame,text="Student Rollno :",font=("times of roman",12,'bold'))
        n_lable.grid(row=0,column=2,padx=10,sticky=W)
    # entery 
        n_entry=ttk.Entry(leftin_frame,textvariable=self.var_roll,font=("times of roman",12,'bold'),width=20)
        n_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

    # name
        d_lable=Label(leftin_frame,text="Name :",font=("times of roman",12,'bold'))
        d_lable.grid(row=1,column=0,padx=10,sticky=W)
    # entery 
        d_entry=ttk.Entry(leftin_frame,textvariable=self.var_name,font=("times of roman",12,'bold'),width=20)
        d_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)


    # department
        rn_lable=Label(leftin_frame,text="Department :",font=("times of roman",12,'bold'))
        rn_lable.grid(row=1,column=2,padx=10,sticky=W)
    # entery 
        rn_entry=ttk.Entry(leftin_frame,textvariable=self.var_dep,font=("times of roman",12,'bold'),width=20)
        rn_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)


    # time
        t_lable=Label(leftin_frame,text="Time :",font=("times of roman",12,'bold'))
        t_lable.grid(row=2,column=0,padx=10,sticky=W)
    # entery 
        t_entry=ttk.Entry(leftin_frame,textvariable=self.var_time,font=("times of roman",12,'bold'),width=20)
        t_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)
    
    # DATE
        da_lable=Label(leftin_frame,text="Date :",font=("times of roman",12,'bold'))
        da_lable.grid(row=2,column=2,padx=10,sticky=W)
    # entery 
        da_entry=ttk.Entry(leftin_frame,textvariable=self.var_date,font=("times of roman",12,'bold'),width=20)
        da_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)
    
    
    # attendence status
       
        g_lable=Label(leftin_frame,text="Attendence status :",font=("times of roman",12,'bold'))
        g_lable.grid(row=3,column=1,padx=10,sticky=W)
    # entery 
        g_entry=ttk.Combobox(leftin_frame,textvariable=self.var_attendence,font=("times of roman",12,'bold'),width=18)
        g_entry['values']=("Status","Present","Absent")
        g_entry.current(0)
        g_entry.grid(row=3,column=2,padx=2,pady=10,sticky=W)

# ==================butnframe=======?
        bt_frame=Frame(leftin_frame,bd=2,relief=RIDGE)
        bt_frame.place(x=0,y=300,width=715,height=35)

    # import csv
        s_bu=Button(bt_frame,width=17,text='Import Csv',font=("times of roman",12,'bold'),bg='green',fg='white',command=self.impcsv)
        s_bu.grid(row=0,column=0)

    # export csv
        u_bu=Button(bt_frame,width=17,text='Export Csv',font=("times of roman",12,'bold'),bg='green',fg='white',command=self.expcsv)
        u_bu.grid(row=0,column=1)

    # delete button
        d_bu=Button(bt_frame,width=17,text='Update',font=("times of roman",12,'bold'),bg='green',fg='white')
        d_bu.grid(row=0,column=2)

    # restet
        re_bu=Button(bt_frame,width=16,command=self.reset_data,text='Reset',font=("times of roman",12,'bold'),bg='green',fg='white')
        re_bu.grid(row=0,column=3)



        # right franme
        r_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Attendence Details',font=("times of roman",15,'bold'),fg='dark blue')
        r_frame.place(x=750,y=10,width=730,height=510)

        table_frame=Frame(r_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=715,height=460)



        # ============= scrool bar===========?
        # scroll bar
        scro_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scro_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.stu_tab=ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendence'),xscrollcommand=scro_x.set,yscrollcommand=scro_y.set)
        scro_x.pack(side=BOTTOM,fill=X)
        scro_y.pack(side=RIGHT,fill=Y)
        scro_x.config(command=self.stu_tab.xview)
        scro_y.config(command=self.stu_tab.yview)


        self.stu_tab.heading('id',text="Attendence ID")
        self.stu_tab.heading('roll',text="Roll no")
        self.stu_tab.heading('name',text="Name")
        self.stu_tab.heading('department',text="Department")
        self.stu_tab.heading('time',text="Time")
        self.stu_tab.heading('date',text="Date")
        self.stu_tab.heading('attendence',text="Attendence Status")

        self.stu_tab['show']='headings'

        self.stu_tab.column('id',width=100)
        self.stu_tab.column('roll',width=100)
        self.stu_tab.column('name',width=100)
        self.stu_tab.column('department',width=100)
        self.stu_tab.column('time',width=100)
        self.stu_tab.column('date',width=100)
        self.stu_tab.column('attendence',width=120)

        self.stu_tab.pack(fill=BOTH,expand=1)
        self.stu_tab.bind("<ButtonRelease>",self.getcur)
    
    # ================= Face Data=============?
    def fetchdata(self,rows):
        self.stu_tab.delete(*self.stu_tab.get_children())
        for i in rows:
            self.stu_tab.insert('',END,values=i)
# ================import csv================
    # def impcsv(self):
    #     global mydata
    #     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title='Open csv',filetypes=(('CSV File','*.csv'),('All File','*.*')),parent=self.root)
    #     with open(fln) as myfile:
    #         csvread=csv.reader(myfile,delimiter=',')
    #         for i in csvread:
    #             mydata.append(i)
    #         self.fetchdata(mydata)

    def impcsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title='Open csv',
            filetypes=(('CSV File','*.csv'),('All File','*.*')),
            parent=self.root
        )

        # FIX: check if file selected
        if fln == "":
            messagebox.showerror("Error", "No file selected")
            return

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=',')
            mydata.clear()   # optional (avoid duplicate data)
            for i in csvread:
                mydata.append(i)

        self.fetchdata(mydata)

# =============export csv =================?
    def expcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror('Error','No data found for export',parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title='Open csv',
            filetypes=(('CSV File','*.csv'),('All File','*.*')),
            parent=self.root
        )
            with open(fln,mode='w',newline='') as myfile:
                exp=csv.writer(myfile,delimiter=',')
                for i in mydata:
                    exp.writerow(i)
                messagebox.showinfo('export',"Your data is exported "+os.path.basename(fln)+' successfully')
        except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)

    
    
    def getcur(self,event=''):
        cur=self.stu_tab.focus()
        cont=self.stu_tab.item(cur) 
        rows=cont['values']
        self.var_id.set(rows[0]),
        self.var_roll.set(rows[1]),
        self.var_name.set(rows[2]),
        self.var_dep.set(rows[3]),
        self.var_time.set(rows[4]),
        self.var_date.set(rows[5]),
        self.var_attendence.set(rows[6])



    def reset_data(self):
        self.var_id.set(''),
        self.var_roll.set(''),
        self.var_name.set(''),
        self.var_dep.set(''),
        self.var_time.set(''),
        self.var_date.set(''),
        self.var_attendence.set('')
        



















if __name__=="__main__":
    root=Tk()
    obj=Attendence(root)   
    root.mainloop() 
