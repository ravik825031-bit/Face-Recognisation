from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("!! FACE RECOGNISTION SYSTEM !!")
        self.root.configure(bg='#f5f6fa')



        #===========Vraibles ================
        self.var_department=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semster=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_hobby=StringVar()

# firts image 
        img=Image.open(r'clg\1 pr.png')
        img=img.resize((500,130))
        self.photoimage=ImageTk.PhotoImage(img)
        f_lbl=Label(self.root,image=self.photoimage)
        f_lbl.place(x=0,y=0,width=500,height=130)


# SECOND IMAHGGE 
        img1=Image.open(r'clg\2 pr.png')
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
        tit_labl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,'bold'),bg='white',fg="darkgreen")
        tit_labl.place(x=0,y=0,width=1530,height=45)


# frame
        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)

# left side lablew frame 
        l_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Information',font=("times of roman",15,'bold'),fg="dark blue")
        l_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r'clg\4 pr.png')
        img_left=img_left.resize((720,130))
        self.photoimage_l=ImageTk.PhotoImage(img_left)
        f_lbl=Label(l_frame,image=self.photoimage_l)
        f_lbl.place(x=5,y=0,width=720,height=130)

# current corse 
        c_frame=LabelFrame(l_frame,bd=2,relief=RIDGE,text='Current course',font=("times of roman",14,'bold'),fg="red")
        c_frame.place(x=5,y=135,width=720,height=115)


#department
        d_lable=Label(c_frame,text="Department",font=("times of roman",12,'bold'))
        d_lable.grid(row=0,column=0,padx=10)
    # combox
        d_combo=ttk.Combobox(c_frame,textvariable=self.var_department,font=("times of roman",12,'bold'),width=17,state='read only')
        d_combo['values']=('Select Department','AIML','CSE','CIVIL','ME','ECE','BT')
        d_combo.current(0)
        d_combo.grid(row=0,column=1,padx=2,pady=10)



#course
        c_lable=Label(c_frame,text="Course",font=("times of roman",12,'bold'))
        c_lable.grid(row=0,column=2,padx=10,sticky=W)
    # combox
        C_combo=ttk.Combobox(c_frame,textvariable=self.var_course,font=("times of roman",12,'bold'),width=17,state='read only')
        C_combo['values']=('Select Course','FE','SE','TE','BE')
        C_combo.current(0)
        C_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



#Yaer
        y_lable=Label(c_frame,text="Year",font=("times of roman",12,'bold'))
        y_lable.grid(row=1,column=0,padx=10,sticky=W)
    # combox
        y_combo=ttk.Combobox(c_frame,textvariable=self.var_year,font=("times of roman",12,'bold'),width=17,state='read only')
        y_combo['values']=('Selet Year','2020-2021','2021-2022','2022-2023','2023-2024','2024-2025','2025-2026','2026-2027')
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)




#Semester
        s_lable=Label(c_frame,text="Semester",font=("times of roman",12,'bold'))
        s_lable.grid(row=1,column=2,padx=10,sticky=W)
    # combox
        s_combo=ttk.Combobox(c_frame,textvariable=self.var_semster,font=("times of roman",12,'bold'),width=17,state='read only')
        s_combo['values']=('Select Semester','','Semester-1','Semester-2')
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


 #student information
        su_frame=LabelFrame(l_frame,bd=2,relief=RIDGE,text='Class Student information',font=("times of roman",14,'bold'),fg="red")
        su_frame.place(x=5,y=250,width=720,height=300)

        self.status_lbl = Label(su_frame,
                        text="Status will show here",
                        font=("times new roman", 12, 'bold'),
                        fg="blue",
                        bg="white")
        self.status_lbl.place(x=10, y=270)

# id
        id_lable=Label(su_frame,text="Student ID:",font=("times of roman",12,'bold'))
        id_lable.grid(row=0,column=0,padx=10,sticky=W)
    # entery 
        id_entry=ttk.Entry(su_frame,textvariable=self.var_std_id,font=("times of roman",12,'bold'),width=20)
        id_entry.grid(row=0,column=1,padx=2,pady=5,sticky=W)


# name
        n_lable=Label(su_frame,text="Student Name:",font=("times of roman",12,'bold'))
        n_lable.grid(row=0,column=2,padx=10,sticky=W)
    # entery 
        n_entry=ttk.Entry(su_frame,textvariable=self.var_std_name,font=("times of roman",12,'bold'),width=20)
        n_entry.grid(row=0,column=3,padx=2,pady=5,sticky=W)


# Division
        d_lable=Label(su_frame,text="Class Division :",font=("times of roman",12,'bold'))
        d_lable.grid(row=1,column=0,padx=10,sticky=W)
    # entery 
        # d_entry=ttk.Entry(su_frame,textvariable=self.var_div,font=("times of roman",12,'bold'),width=20)
        # d_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        d_combo=ttk.Combobox(su_frame,textvariable=self.var_div,font=("times of roman",12,'bold'),width=18,state='read only')
        d_combo['values']=('Select Division','A','B','C')
        d_combo.current(0)
        d_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)


# Rollnno
        rn_lable=Label(su_frame,text="Roll no :",font=("times of roman",12,'bold'))
        rn_lable.grid(row=1,column=2,padx=10,sticky=W)
    # entery 
        rn_entry=ttk.Entry(su_frame,textvariable=self.var_roll,font=("times of roman",12,'bold'),width=20)
        rn_entry.grid(row=1,column=3,padx=2,pady=5,sticky=W)



# gender
        g_lable=Label(su_frame,text="Gender :",font=("times of roman",12,'bold'))
        g_lable.grid(row=2,column=0,padx=10,sticky=W)
    # entery 
        g_entry=ttk.Combobox(su_frame,textvariable=self.var_gender,font=("times of roman",12,'bold'),width=18)
        g_entry['values']=("Select","Male","Female",'chkka','chhki')
        g_entry.current(0)
        g_entry.grid(row=2,column=1,padx=2,pady=5,sticky=W)



# DOB
        dob_lable=Label(su_frame,text="DOB :",font=("times of roman",12,'bold'))
        dob_lable.grid(row=2,column=2,padx=10,sticky=W)
    # entery 
        dob_entry=ttk.Entry(su_frame,textvariable=self.var_dob,font=("times of roman",12,'bold'),width=20)
        dob_entry.grid(row=2,column=3,padx=2,pady=5,sticky=W)



# EMAIL
        em_lable=Label(su_frame,text="Email id :",font=("times of roman",12,'bold'))
        em_lable.grid(row=3,column=0,padx=10,sticky=W)
    # entery 
        em_entry=ttk.Entry(su_frame,textvariable=self.var_email,font=("times of roman",12,'bold'),width=20)
        em_entry.grid(row=3,column=1,padx=2,pady=5,sticky=W)



# phone number
        pn_lable=Label(su_frame,text="Phone no :",font=("times of roman",12,'bold'))
        pn_lable.grid(row=3,column=2,padx=5,sticky=W)
    # entery 
        pn_entry=ttk.Entry(su_frame,textvariable=self.var_phone,font=("times of roman",12,'bold'),width=20)
        pn_entry.grid(row=3,column=3,padx=2,pady=5,sticky=W)



# addresss
        ad_lable=Label(su_frame,text="Address :",font=("times of roman",12,'bold'))
        ad_lable.grid(row=4,column=0,padx=10,sticky=W)
    # entery 
        ad_entry=ttk.Entry(su_frame,textvariable=self.var_address,font=("times of roman",12,'bold'),width=20)
        ad_entry.grid(row=4,column=1,padx=2,pady=5,sticky=W)



# hobby
        te_lable=Label(su_frame,text="hobby :",font=("times of roman",12,'bold'))
        te_lable.grid(row=4,column=2,padx=10,sticky=W)
    # entery 
        te_entry=ttk.Entry(su_frame,textvariable=self.var_hobby,font=("times of roman",12,'bold'),width=20)
        te_entry.grid(row=4,column=3,padx=2,pady=5,sticky=W)

# radio button 1

        self.var_radio1=StringVar()
        radio_1=ttk.Radiobutton(su_frame,text="Take photo smaple",variable=self.var_radio1,value='Yes')
        radio_1.grid(row=6,column=0)


        # radio 2
        # self.var_radio2=StringVar()
        radio_2=ttk.Radiobutton(su_frame,text="No photo smaple",variable=self.var_radio1,value='No')
        radio_2.grid(row=6,column=1)
  
  
  #@buttons frame 
        bt_frame=Frame(su_frame,bd=2,relief=RIDGE)
        bt_frame.place(x=0,y=200,width=715,height=35)

    # data add & save button
        s_bu=Button(bt_frame,width=17,text='Save',command=self.add_data,font=("times of roman",12,'bold'),bg='green',fg='white')
        s_bu.grid(row=0,column=0)

    # update button
        u_bu=Button(bt_frame,width=17,text='Update',command=self.update_data,font=("times of roman",12,'bold'),bg='green',fg='white')
        u_bu.grid(row=0,column=1)

    # delete button
        d_bu=Button(bt_frame,width=17,text='Delete',command=self.delete_data,font=("times of roman",12,'bold'),bg='green',fg='white')
        d_bu.grid(row=0,column=2)

    # restet
        re_bu=Button(bt_frame,width=16,text='Reset',command=self.reset_data,font=("times of roman",12,'bold'),bg='green',fg='white')
        re_bu.grid(row=0,column=3)


#@buttons frame 2 
        bt_frame2=Frame(su_frame,bd=2,relief=RIDGE)
        bt_frame2.place(x=0,y=235,width=715,height=35)

    #takr photo sample
        tk_bu=Button(bt_frame2,width=35,command=self.genrate_data,text='Take photo sample',font=("times of roman",12,'bold'),bg='green',fg='white')
        tk_bu.grid(row=0,column=0)

    #update photo sample
        u_bu=Button(bt_frame2,width=34,text='Update photo sample',command=self.update_photo,font=("times of roman",12,'bold'),bg='green',fg='white')
        u_bu.grid(row=0,column=1)






# right franme
        r_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text='Student Details',font=("times of roman",15,'bold'),fg='dark blue')
        r_frame.place(x=750,y=10,width=730,height=580)

        img_right=Image.open(r'clg\5 pr.png')
        img_right=img_right.resize((720,130))
        self.photoimage_r=ImageTk.PhotoImage(img_right)
        f_lbl=Label(r_frame,image=self.photoimage_r)
        f_lbl.place(x=5,y=0,width=720,height=130)


# ----------- search system ------------
        sea_frame=LabelFrame(r_frame,bd=2,relief=RIDGE,text='Search System',font=("times of roman",14,'bold'),fg="red")
        sea_frame.place(x=5,y=135,width=720,height=70)

        

# search bar
        se_lable=Label(sea_frame,text="Search by :",font=("times of roman",15,'bold'),bg='white')
        se_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)
#combobox
        s_combo=ttk.Combobox(sea_frame,font=("times of roman",12,'bold'),width=15,state='read only')
        s_combo['values']=('Select ','Roll_no','Phone_No')
        s_combo.current(0)
        s_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(sea_frame,font=("times of roman",12,'bold'),width=15)
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        se_bu=Button(sea_frame,width=10,text='Search',font=("times of roman",12,'bold'),bg='blue')
        se_bu.grid(row=0,column=3,padx=4)

        sl_bu=Button(sea_frame,width=10,text='Show All',font=("times of roman",12,'bold'),bg='blue')
        sl_bu.grid(row=0,column=4,padx=4)



# -----------table frame-----------

        table_frame=Frame(r_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=720,height=340)

# scroll bar
        scro_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scro_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        
        self.stu_tab=ttk.Treeview(table_frame,column=('department','course','year','sem','id','name','division','roll','gender','dob','email','phone','address','hobby','photo'),xscrollcommand=scro_x.set,yscrollcommand=scro_y.set)
        scro_x.pack(side=BOTTOM,fill=X)
        scro_y.pack(side=RIGHT,fill=Y)
        scro_x.config(command=self.stu_tab.xview)
        scro_y.config(command=self.stu_tab.yview)


        self.stu_tab.heading('department',text="Department")
        self.stu_tab.heading('course',text="Course")
        self.stu_tab.heading('year',text="Year")
        self.stu_tab.heading('sem',text="Semester")
        self.stu_tab.heading('id',text="Student ID")
        self.stu_tab.heading('name',text="Name")
        self.stu_tab.heading('division',text="Division")
        self.stu_tab.heading('roll',text="Roll_no")
        self.stu_tab.heading('gender',text="Gender")
        self.stu_tab.heading('dob',text="DOB")
        self.stu_tab.heading('email',text="Email ID")
        self.stu_tab.heading('phone',text="Phone_NO")
        self.stu_tab.heading('address',text="Address")
        self.stu_tab.heading('hobby',text="Hobby")
        self.stu_tab.heading('photo',text="Photo")
        self.stu_tab['show']='headings'


        self.stu_tab.column('department',width=100)
        self.stu_tab.column('course',width=100)
        self.stu_tab.column('year',width=100)
        self.stu_tab.column('sem',width=100)
        self.stu_tab.column('id',width=100)
        self.stu_tab.column('name',width=100)
        self.stu_tab.column('division',width=100)
        self.stu_tab.column('roll',width=100)
        self.stu_tab.column('gender',width=100)
        self.stu_tab.column('dob',width=100)
        self.stu_tab.column('email',width=130)
        self.stu_tab.column('phone',width=130)
        self.stu_tab.column('address',width=100)
        self.stu_tab.column('hobby',width=100)
        self.stu_tab.column('photo',width=100)
    

        self.stu_tab.pack(fill=BOTH,expand=1)
        self.stu_tab.bind('<ButtonRelease>',self.get_cursor)
        self.fetch()




#--------------------function declartion-----------------
    def add_data(self):
        if self.var_department.get()=="Select Depatment" or self.var_std_name.get()=='' or self.var_std_id.get=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute(
    "INSERT INTO student (department, course,year, semester,std_id, name, division, roll, gender, dob, email, phone, address, hobby, photosample) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
    (
        
        self.var_department.get(),
        
        self.var_course.get(),
        self.var_year.get(),
        self.var_semster.get(),
        self.var_std_id.get(),
        self.var_std_name.get(),
        self.var_div.get(),
        self.var_roll.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_email.get(),
        self.var_phone.get(),
        self.var_address.get(),
        self.var_hobby.get(),
        self.var_radio1.get()
    )
)
                conn.commit()
                self.fetch()
                conn.close()
                messagebox.showinfo('success','student details added successfully',parent=self.root)
        
            except Exception as es:
                messagebox.showerror("Error",f'due to : {str(es)}',parent=self.root)

#=========================fetech data +++++++++++=

    def fetch(self): 
        conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.stu_tab.delete(*self.stu_tab.get_children())
            for i in data :
                self.stu_tab.insert('',END,values=i)
            conn.commit()
        conn.close()


     #==============get cursor=================
    def get_cursor(self,event=''):
        cursor=self.stu_tab.focus()
        content=self.stu_tab.item(cursor)
        dataa=content['values']

        
        self.var_department.set(dataa[0]),
        self.var_course.set(dataa[1]),
        self.var_year.set(dataa[2]),
        self.var_semster.set(dataa[3]),
        self.var_std_id.set(dataa[4]),
        self.var_std_name.set(dataa[5]),
        self.var_div.set(dataa[6]),
        self.var_roll.set(dataa[7]),
        self.var_gender.set(dataa[8]),
        self.var_dob.set(dataa[9]),
        self.var_email.set(dataa[10]),
        self.var_phone.set(dataa[11]),
        self.var_address.set(dataa[12]),
        self.var_hobby.set(dataa[13]),
        self.var_radio1.set(dataa[14])

#========= update function ===========
#     def update_data(self):
#         if self.var_department.get()=="Select Depatment" or self.var_std_name.get()=='' or self.var_std_id.get=='':
#             messagebox.showerror('Error','All fields are required',parent=self.root)
#         else:
#             try:
#                 update=messagebox.askquestion('Update','Do you want to update student deltails',parent=self.root)
#                 if update >0:
#                     conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
#                     my_cursor=conn.cursor()
#                     my_cursor.execute('update student set departemnt=%s,course=%s,year=%s,semester=%s,std_id=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,hobby=%s,photosample=%s where std_id=%s',(
#                         self.var_department.get(),
        
#         self.var_course.get(),
#         self.var_year.get(),
#         self.var_semster.get(),
#         self.var_std_name.get(),
#         self.var_div.get(),
#         self.var_roll.get(),
#         self.var_gender.get(),
#         self.var_dob.get(),
#         self.var_email.get(),
#         self.var_phone.get(),
#         self.var_address.get(),
#         self.var_hobby.get(),
#         self.var_radio1.get(),
#         self.var_std_id.get()
#                     )
#         )
#                 else:
#                     if  not update:
#                         return
#                 messagebox.showinfo('Sucess ','Student details update sucessfully !',parent=self.root)
#                 conn.commit()
#                 self.fetch()
#                 conn.close()
#             except Exception as es:
#                 messagebox.showerror("Error",f'Due to : {str(es)}',parent=self.root)

    def update_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=='' or self.var_std_id.get()=='':
                messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                update=messagebox.askyesno('Update','Do you want to update student details?',parent=self.root)
                if update:
                        conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
                        my_cursor=conn.cursor()

                        my_cursor.execute("""
                        UPDATE student SET
                        department=%s,
                        course=%s,
                        year=%s,
                        semester=%s,
                        name=%s,
                        division=%s,
                        roll=%s,
                        gender=%s,
                        dob=%s,
                        email=%s,
                        phone=%s,
                        address=%s,
                        hobby=%s,
                        photosample=%s
                        WHERE std_id=%s
                        """,(
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semster.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_hobby.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                        ))

                        conn.commit()
                        self.fetch()
                        conn.close()

                        messagebox.showinfo('Success','Student updated successfully!',parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)
    
    # ==============delte==============
    
    
    def delete_data(self):
        if self.var_std_id.get()=='':
            messagebox.showerror('Error','Student id must be required',parent=self.root)
        else:
            try:
                delete=messagebox.askyesno('Student deltet page','Do you want delete this information ',parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
                    my_cursor=conn.cursor()
                    sql='delete from student where std_id=%s'
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete :
                        return
                    
                conn.commit()
                self.fetch()
                conn.close()

                messagebox.showinfo("Delete","successfully deleted student detials",parent=self.root)


            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)
        

        # ====================reset================

    def reset_data(self):  
        self.var_department.set('Select Departmanet')
        self.var_course.set('Select course')
        self.var_year.set('Select year')
        self.var_semster.set('Select smester')
        self.var_std_id.set('')
        self.var_std_name.set('')
        self.var_div.set('Select Division')
        self.var_roll.set('')
        self.var_gender.set('Select gender')
        self.var_dob.set('')
        self.var_email.set('')
        self.var_phone.set('')
        self.var_address.set('')
        self.var_hobby.set('')
        self.var_radio1.set('')

#==================genrate data set and take photo samlple=======
    def genrate_data(self):
        if self.var_department.get()=="Select Department" or self.var_std_name.get()=='' or self.var_std_id.get()=='':
                messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
               
                conn=mysql.connector.connect(host="localhost",username='root',password='3242',database='face_recognizer')
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("""
                        UPDATE student SET
                        department=%s,
                        course=%s,
                        year=%s,
                        semester=%s,
                        name=%s,
                        division=%s,
                        roll=%s,
                        gender=%s,
                        dob=%s,
                        email=%s,
                        phone=%s,
                        address=%s,
                        hobby=%s,
                        photosample=%s
                        WHERE std_id=%s
                        """,(
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semster.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_hobby.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                        ))

                conn.commit()
                self.fetch()
                self.reset_data()
                conn.close()

            # ================Load predefined data on face frontal fron opencv====
                fac_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                def face_crp(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=fac_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor =1.3
                    # min Neighbpour=5

                    for (x,y,w,h) in faces:
                        face_crp=img[y:y+h,x:x+w]
                        return face_crp

                
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,myframe=cap.read()
                    if face_crp(myframe) is not None:
                        img_id+=1
                        face=cv2.resize(face_crp(myframe),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_namepath="data/users."+str(id)+'.'+str(img_id)+".jpg"
                        cv2.imwrite(file_namepath,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow('Cropped face',face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Result','Genrating data set completed suseecfully!!')
            
            
            except Exception as es:
                messagebox.showerror("Error",f'Due to: {str(es)}',parent=self.root)


    def update_photo(self):
        if self.var_std_id.get()=='':
            messagebox.showerror("Error","Please select student first",parent=self.root)
            return

        try:
            import os

            student_id = str(self.var_std_id.get()).strip()
            folder_path = "data"

            deleted_count = 0

            # 🔥 delete only that student's photos
            for file in os.listdir(folder_path):
                parts = file.split(".")
                if len(parts) >= 3:
                    if parts[0] == "user" and parts[1] == student_id:
                        os.remove(os.path.join(folder_path, file))
                        deleted_count += 1

            # ✅ show delete status
            self.status_lbl.config(text=f"Deleted {deleted_count} old photos ✅", fg="green")
            self.root.update()

            # 🔥 camera start
            face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            def face_crop(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)
                for (x,y,w,h) in faces:
                    return img[y:y+h,x:x+w]

            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, frame = cap.read()
                if face_crop(frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_crop(frame),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                    file_name = f"data/user.{student_id}.{img_id}.jpg"
                    cv2.imwrite(file_name, face)

                    cv2.putText(face,str(img_id),(50,50),
                                cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Updating Face",face)

                if cv2.waitKey(1)==13 or img_id==100:
                    break

            cap.release()
            cv2.destroyAllWindows()

            # ✅ final status
            self.status_lbl.config(text="New photos updated successfully ✅", fg="blue")

            messagebox.showinfo("Success","Photo updated successfully!",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)








if __name__=="__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()        