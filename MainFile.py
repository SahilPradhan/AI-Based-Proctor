from tkinter import*
from tkinter import ttk,messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from PIL import ImageDraw # pip install pillow
import PIL.Image
import pymysql #pip install pymysql
from datetime import*
#import datetime
import time
import sys
from math import*
import webbrowser
from functools import partial

from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import random
from io import StringIO
from user_activity import userActivityTracking
#import tkFont
import re
import tkinter as tk


#from head_pose_estimation import start
#from main import start

from audio_part import start_audio
from person_and_phone import start_multiplepersons

from threading import Thread
from threading import Event

from multiprocessing import Process
from facerecog import check_face
import smtplib, ssl
#from multiprocessing import Process
#from concurrent.futures import ThreadPoolExecutor
#from test_stats import display_function



class Test_Stats:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Faculty DashBoard")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("image/admin_icon.ico")

        self.root.resizable(0, 0) 
        self.email=txt
        

        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="FACULTY DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.name = StringVar()
        self.testDate = StringVar()
        self.startTime = StringVar()
        self.endTime=StringVar()
        self.subject = StringVar()
        self.URL = StringVar()
        self.TestID = StringVar()
       

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        
        self.addtest=PIL.Image.open("image/addtest.png")
        self.readdtest=self.addtest.resize((180,30),PIL.Image.ANTIALIAS)
        self.faddtest=ImageTk.PhotoImage(self.readdtest)
        add_test_btn=Button(Dash_Frame,image=self.faddtest,command=self.add_test_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        add_test_btn.grid(row=0,column=0,padx=(0,30),pady=(20,10))
        #add_test_btn = Button(Dash_Frame,bg="#8B0000",text="Add Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.teststats=PIL.Image.open("image/teststats.png")
        self.reteststats=self.teststats.resize((180,30),PIL.Image.ANTIALIAS)
        self.fteststats=ImageTk.PhotoImage(self.reteststats)
        view_test_stats_btn=Button(Dash_Frame,image=self.fteststats, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        view_test_stats_btn.grid(row=1,column=0,padx=(0,30),pady=(0,10))

        self.penver=PIL.Image.open("image/verif.png")
        self.repenver=self.penver.resize((180,30),PIL.Image.ANTIALIAS)
        self.fpenver=ImageTk.PhotoImage(self.repenver)
        pending_verification_btn=Button(Dash_Frame,image=self.fpenver,command=self.pending_verf_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        pending_verification_btn.grid(row=2,column=0,padx=(0,30),pady=(0,10))

        self.blockacc=PIL.Image.open("image/blocked.png")
        self.reblockacc=self.blockacc.resize((180,30),PIL.Image.ANTIALIAS)
        self.fblockacc=ImageTk.PhotoImage(self.reblockacc)
        blocked_acc_btn=Button(Dash_Frame,image=self.fblockacc, command=self.blocked_acc_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        blocked_acc_btn.grid(row=3,column=0,padx=(0,30),pady=(0,10))

        #self.rules=PIL.Image.open("image/rules.png")
        #self.rerules = self.rules.resize((180,30),PIL.Image.ANTIALIAS)
        #self.frules=ImageTk.PhotoImage(self.rerules)
        #view_rules_btn=Button(Dash_Frame,image=self.frules, command=self.rules_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        #view_rules_btn.grid(row=4,column=0,padx=(0,30),pady=(0,10))
        
        # manage_employee_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Employee",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        # department_btn = Button(Dash_Frame,text="Department",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="STUDENTS STaTS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=755,height=635)
    
        #Table Frame

        Table_Frame1 = Frame(Manage_Frame,bg="#0A090C")
        Table_Frame1.place(x=3,y=6,width=740,height=595)

        

        X_scroll = Scrollbar(Table_Frame1,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame1,orient=VERTICAL)
        self.Table1 = ttk.Treeview(Table_Frame1,columns=("Email","Words Spoken","Multiple persons","Cell Phone","No Person","Study Material"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table1.xview)

        self.Table1.heading("Email",text="Email")
        self.Table1.heading("Words Spoken",text="Words Spoken")
        # self.Table.heading("Test URL",text="Test URL")
        self.Table1.heading("Multiple persons",text="Multiple persons")
        self.Table1.heading("Cell Phone",text="Cell Phone")
        self.Table1.heading("No Person",text="No Person")
        self.Table1.heading("Study Material",text="Study Material")



        

        self.Table1['show']="headings"
        self.Table1.column("Email",width=210)
        self.Table1.column("Words Spoken",width=50)
        # self.Table.column("Test URL",width=150)
        self.Table1.column("Multiple persons",width=60)
        self.Table1.column("Cell Phone",width=50)
        self.Table1.column("No Person",width=50)
        self.Table1.column("Study Material",width=50)
        
        

        

        self.Table1.pack(fill=BOTH,expand=1)
        #self.Table1.bind('<ButtonRelease 1>',self.get_fields)

        

        #Button Frame
        #btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        #btn_frame.place(x=12,y=520,width=410) 

        

        #add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)

        #update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        #delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        #clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="TEST DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=955,y=60,width=395,height=635)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=5,y=6,width=380,height=595)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Test-Name","Subject","Test Date"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        #self.Table.heading("Test-ID",text="Test-ID")
        self.Table.heading("Test-Name",text="Test-Name")
        # self.Table.heading("Test URL",text="Test URL")
        self.Table.heading("Subject",text="Subject")
        self.Table.heading("Test Date",text="Test Date")
        #self.Table.heading("Start Time",text="Start Time")



        

        self.Table['show']="headings"
        #self.Table.column("Test-ID",width=100)
        self.Table.column("Test-Name",width=140)
        # self.Table.column("Test URL",width=150)
        self.Table.column("Subject",width=60)
        self.Table.column("Test Date",width=60)
        #self.Table.column("Start Time",width=100)
        
        

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        # self.txt_Date.bind("<FocusIn>", self.foc_in)
        # self.txt_Date.bind("<FocusOut>", self.foc_out)


        # self.put_placeholder()
        self.show_data()

        

    def add_student(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()

            self.TestID = random.randint(3,1000)

            curr.execute("INSERT INTO TEST_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.TestID, self.name.get(), self.URL.get(), self.testDate.get(), self.txt_StartTime.get(),self.txt_EndTime.get(),self.subject.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()

        

        curr.execute("SELECT TEST_ID, TEST_NAME, SUBJECT, TEST_URL, TEST_DATE, START_TIME, END_TIME from TEST_DETAILS")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=(row[1],row[2],row[4],row[5]))

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.subject.set("")
            self.name.set("")
            self.URL.set("")
            self.testDate.set("")
            self.startTime.set("")
            self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']
            #self.TestID.set(row[0])
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()
            curr.execute("SELECT TEST_ID FROM TEST_DETAILS WHERE TEST_NAME=%s AND SUBJECT=%s",(row[0],row[1]))
            row1 = curr.fetchone()
            #print(row[0])
            curr.execute("SELECT EMAIL, WORDS_SPOKEN, MULTIPLE_PERSON_DETECTION, MOBILE_PHONE_DETECTION,NO_PERSON_DETECTION,STUDY_MATERIAL_DETECTION FROM ONLINE WHERE TEST_ID=%s",(row1[0]))
            rows = curr.fetchall()

            self.Table1.delete(*self.Table1.get_children())
            if(len(rows)!=0):
                for row in rows:

                    self.Table1.insert('',END,values=row)

            connect.commit()
            connect.close()

        #self.name.set(row[0])
        #self.URL.set(row[2])
        #self.testDate.set(row[3])
        #self.startTime.set(row[4])
        #elf.subject.set(row[1])


        

    def update(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()



            curr.execute("UPDATE TEST_DETAILS SET TEST_URL=%s, TEST_DATE=%s, START_TIME=%s, END_TIME=%s where SUBJECT=%s AND TEST_NAME=%s",(self.URL.get(),self.testDate.get(),self.startTime.get(),self.endTime.get(),self.subject.get(),self.name.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("DELETE from STUDENT where roll_no=%s",(self.roll_no.get()))

                                                                             

            

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    # def put_placeholder(self):

    #     self.txt_Date.insert(0,"DD-MM-YYYY")
    #     self.txt_Date['fg'] = "grey"

    #     self.txt_StartTime.insert(0,"HH-MM")
    #     self.txt_StartTime['fg'] = "grey"


    # def foc_in(self,event):

    #     if self.txt_Date['fg'] == "grey":

    #         self.txt_Date.delete('0', 'end')
    #         self['fg'] = "grey"


    # def foc_out(self, event):

    #     if not self.get():
    #         self.txt_Date.put_placeholder()

    #     if not self.get():
    #         self.txt_StartTime.put_placeholder()

            

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()        

        

    def add_test_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Faculty(st_root,self.email)
        st_root.mainloop()

    def pending_verf_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Pending_Verification(st_root,self.email)
        st_root.mainloop()

    def blocked_acc_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Blocked_Accounts(st_root,self.email)
        st_root.mainloop()

    def rules_btn(self):
        self.root.destroy()
        st_root = Tk()
        st = Rules(st_root, self.email)
        st_root,mainloop()

##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


class Rules:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Faculty DashBoard")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("image/admin_icon.ico")

        self.root.resizable(0, 0) 
        self.email=txt
        

        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="FACULTY DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.audio = StringVar()
        self.testDate = StringVar()
        self.startTime = StringVar()
        self.endTime=StringVar()
        self.subject = StringVar()
        self.URL = StringVar()
        self.TestID = StringVar()
       

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        
        self.addtest=PIL.Image.open("image/addtest.png")
        self.readdtest=self.addtest.resize((180,30),PIL.Image.ANTIALIAS)
        self.faddtest=ImageTk.PhotoImage(self.readdtest)
        add_test_btn=Button(Dash_Frame,image=self.faddtest,command=self.add_test_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        add_test_btn.grid(row=0,column=0,padx=(0,30),pady=(20,10))
        #add_test_btn = Button(Dash_Frame,bg="#8B0000",text="Add Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.teststats=PIL.Image.open("image/teststats.png")
        self.reteststats=self.teststats.resize((180,30),PIL.Image.ANTIALIAS)
        self.fteststats=ImageTk.PhotoImage(self.reteststats)
        view_test_stats_btn=Button(Dash_Frame,image=self.fteststats, command=self.test_stats_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        view_test_stats_btn.grid(row=1,column=0,padx=(0,30),pady=(0,10))

        self.penver=PIL.Image.open("image/verif.png")
        self.repenver=self.penver.resize((180,30),PIL.Image.ANTIALIAS)
        self.fpenver=ImageTk.PhotoImage(self.repenver)
        pending_verification_btn=Button(Dash_Frame,image=self.fpenver,command=self.pending_verf_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        pending_verification_btn.grid(row=2,column=0,padx=(0,30),pady=(0,10))

        self.blockacc=PIL.Image.open("image/blocked.png")
        self.reblockacc=self.blockacc.resize((180,30),PIL.Image.ANTIALIAS)
        self.fblockacc=ImageTk.PhotoImage(self.reblockacc)
        blocked_acc_btn=Button(Dash_Frame,image=self.fblockacc, command=self.blocked_acc_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        blocked_acc_btn.grid(row=3,column=0,padx=(0,30),pady=(0,10))


        #self.rules=PIL.Image.open("image/rules.png")
        #self.rerules = self.rules.resize((180,30),PIL.Image.ANTIALIAS)
        #self.frules=ImageTk.PhotoImage(self.rerules)
        #view_rules_btn=Button(Dash_Frame,image=self.frules, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        #view_rules_btn.grid(row=4,column=0,padx=(0,30),pady=(0,10))
        
        # manage_employee_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Employee",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        # department_btn = Button(Dash_Frame,text="Department",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="PROBABLE CHEATING WORDS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=1145,height=635)

        lbl_audio = Label(Manage_Frame,text="Probable cheating audio",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_audio.grid(row = 2,column=0,pady=10,padx=10,sticky="w")
        txt_audio = Text(Manage_Frame,height = 5, width = 52, font=("Georgia",15,"bold"),bd=5)
        txt_audio.grid(row = 2,column=1,pady=10,padx=5,sticky="w")
        words = self.show_data()
        print(words)
        txt_audio.insert(tk.END, words)


        self.updt=PIL.Image.open("image/update.png")
        self.reupdt=self.updt.resize((140,30),PIL.Image.ANTIALIAS)
        self.fupdt=ImageTk.PhotoImage(self.reupdt)
        update_btn=Button(Manage_Frame,image=self.fupdt, bd=0,cursor="hand2",command=partial(self.update_audio, words=txt_audio.get("1.0")), bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        update_btn.grid(row=4,column=1,padx=20,pady=10,sticky="nsew")
        
    
        #Table Frame

        #Table_Frame1 = Frame(Manage_Frame,bg="#0A090C")
        #Table_Frame1.place(x=3,y=6,width=740,height=595)

        

        #X_scroll = Scrollbar(Table_Frame1,orient=HORIZONTAL)
        #Y_scroll = Scrollbar(Table_Frame1,orient=VERTICAL)
        #self.Table1 = ttk.Treeview(Table_Frame1,columns=("Email","Words Spoken","Multiple persons","Cell Phone","No Person","Study Material"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        #X_scroll.pack(side=BOTTOM,fill=X)
        #Y_scroll.pack(side=RIGHT,fill=Y)
        #X_scroll.config(command=self.Table1.xview)

        #self.Table1.heading("Email",text="Email")
        #self.Table1.heading("Words Spoken",text="Words Spoken")
        # self.Table.heading("Test URL",text="Test URL")
        #self.Table1.heading("Multiple persons",text="Multiple persons")
        #self.Table1.heading("Cell Phone",text="Cell Phone")
        #self.Table1.heading("No Person",text="No Person")
        #self.Table1.heading("Study Material",text="Study Material")



        

        #self.Table1['show']="headings"
        #self.Table1.column("Email",width=210)
        #self.Table1.column("Words Spoken",width=50)
        # self.Table.column("Test URL",width=150)
        #self.Table1.column("Multiple persons",width=60)
        #self.Table1.column("Cell Phone",width=50)
        #self.Table1.column("No Person",width=50)
        #self.Table1.column("Study Material",width=50)
        
        

        

        #self.Table1.pack(fill=BOTH,expand=1)
        #self.Table1.bind('<ButtonRelease 1>',self.get_fields)

        

        #Button Frame
        #btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        #btn_frame.place(x=12,y=520,width=410) 

        

        #add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)

        #update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        #delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        #clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        #Detail_Frame = LabelFrame(self.root,text="TEST DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        #Detail_Frame.place(x=955,y=60,width=395,height=635)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        #Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        #Table_Frame.place(x=5,y=6,width=380,height=595)

        

        #X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        #Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        #self.Table = ttk.Treeview(Table_Frame,columns=("Test-Name","Subject","Test Date"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        #X_scroll.pack(side=BOTTOM,fill=X)
        #Y_scroll.pack(side=RIGHT,fill=Y)
        #X_scroll.config(command=self.Table.xview)
        #Y_scroll.config(command=self.Table.yview)

        #self.Table.heading("Test-ID",text="Test-ID")
        #self.Table.heading("Test-Name",text="Test-Name")
        # self.Table.heading("Test URL",text="Test URL")
        #self.Table.heading("Subject",text="Subject")
        #self.Table.heading("Test Date",text="Test Date")
        #self.Table.heading("Start Time",text="Start Time")



        

        #self.Table['show']="headings"
        #self.Table.column("Test-ID",width=100)
        #self.Table.column("Test-Name",width=140)
        # self.Table.column("Test URL",width=150)
        #self.Table.column("Subject",width=60)
        #self.Table.column("Test Date",width=60)
        #self.Table.column("Start Time",width=100)
        
        

        

        #self.Table.pack(fill=BOTH,expand=1)
        #self.Table.bind('<ButtonRelease 1>',self.get_fields)
        # self.txt_Date.bind("<FocusIn>", self.foc_in)
        # self.txt_Date.bind("<FocusOut>", self.foc_out)


        # self.put_placeholder()
        #self.show_data(txt_audio)

        

    def add_student(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()

            self.TestID = random.randint(3,1000)

            curr.execute("INSERT INTO TEST_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.TestID, self.name.get(), self.URL.get(), self.testDate.get(), self.txt_StartTime.get(),self.txt_EndTime.get(),self.subject.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Added")



    def update_audio(self, words):
        print(words)
        #f_audio = open("paper.txt", "r")
        #audio = f_audio.read()
        #if(audio != words):
            #print("words :"+words)
            #print("----------------------")
            #print("audio :"+audio)
            #f_update_file = open("paper.txt", "w")
            #f_update_file.write(updatedWords)
            #f_update_file.close()
        #else:
            #print("No change!")
        #f_audio.close()

        

    def show_data(self):


        f_audio = open("paper.txt", "r")
        
        audio = f_audio.read()

        f_audio.close()
        return audio
        #txt_audio.insert(tk.END, audio)
        #connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        #curr = connect.cursor()

        

        #curr.execute("SELECT TEST_ID, TEST_NAME, SUBJECT, TEST_URL, TEST_DATE, START_TIME, END_TIME from TEST_DETAILS")
        #rows = curr.fetchall()

        #if(len(rows)!=0):

            #self.Table.delete(*self.Table.get_children())
            #for row in rows:

                #self.Table.insert('',END,values=(row[1],row[2],row[4],row[5]))

            #connect.commit()
        #connect.close()

        

    def clear_field(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.subject.set("")
            self.name.set("")
            self.URL.set("")
            self.testDate.set("")
            self.startTime.set("")
            self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']
            #self.TestID.set(row[0])
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()
            curr.execute("SELECT TEST_ID FROM TEST_DETAILS WHERE TEST_NAME=%s AND SUBJECT=%s",(row[0],row[1]))
            row1 = curr.fetchone()
            #print(row[0])
            curr.execute("SELECT EMAIL, WORDS_SPOKEN, MULTIPLE_PERSON_DETECTION, MOBILE_PHONE_DETECTION,NO_PERSON_DETECTION,STUDY_MATERIAL_DETECTION FROM ONLINE WHERE TEST_ID=%s",(row1[0]))
            rows = curr.fetchall()

            self.Table1.delete(*self.Table1.get_children())
            if(len(rows)!=0):
                for row in rows:

                    self.Table1.insert('',END,values=row)

            connect.commit()
            connect.close()

        #self.name.set(row[0])
        #self.URL.set(row[2])
        #self.testDate.set(row[3])
        #self.startTime.set(row[4])
        #elf.subject.set(row[1])


        

    def update(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()



            curr.execute("UPDATE TEST_DETAILS SET TEST_URL=%s, TEST_DATE=%s, START_TIME=%s, END_TIME=%s where SUBJECT=%s AND TEST_NAME=%s",(self.URL.get(),self.testDate.get(),self.startTime.get(),self.endTime.get(),self.subject.get(),self.name.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.roll_no.get() == "" or self.name.get() == "" or self.email_id.get() == "" or self.gender.get()== "" or self.dob.get()== ""or self.contact.get() == "" or self.txt_address.get('1.0',END) == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("DELETE from STUDENT where roll_no=%s",(self.roll_no.get()))

                                                                             

            

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    # def put_placeholder(self):

    #     self.txt_Date.insert(0,"DD-MM-YYYY")
    #     self.txt_Date['fg'] = "grey"

    #     self.txt_StartTime.insert(0,"HH-MM")
    #     self.txt_StartTime['fg'] = "grey"


    # def foc_in(self,event):

    #     if self.txt_Date['fg'] == "grey":

    #         self.txt_Date.delete('0', 'end')
    #         self['fg'] = "grey"


    # def foc_out(self, event):

    #     if not self.get():
    #         self.txt_Date.put_placeholder()

    #     if not self.get():
    #         self.txt_StartTime.put_placeholder()

            

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()


    def test_stats_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Test_Stats(st_root,self.email)
        st_root.mainloop()

        

    def add_test_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Faculty(st_root,self.email)
        st_root.mainloop()

    def pending_verf_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Pending_Verification(st_root,self.email)
        st_root.mainloop()

    def blocked_acc_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Blocked_Accounts(st_root,self.email)
        st_root.mainloop()

##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


class Faculty:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Faculty DashBoard")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("image/admin_icon.ico")
        self.root.resizable(0, 0) 
        self.email=txt
        

        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="FACULTY DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.name = StringVar()
        self.testDate = StringVar()
        self.startTime = StringVar()
        self.endTime = StringVar()
        self.subject = StringVar()
        self.URL = StringVar()
        self.TestID = StringVar()
       

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        
        self.addtest=PIL.Image.open("image/addtest.png")
        self.readdtest=self.addtest.resize((180,30),PIL.Image.ANTIALIAS)
        self.faddtest=ImageTk.PhotoImage(self.readdtest)
        add_test_btn=Button(Dash_Frame,image=self.faddtest, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        add_test_btn.grid(row=0,column=0,padx=(0,30),pady=(20,10))
        #add_test_btn = Button(Dash_Frame,bg="#8B0000",text="Add Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.teststats=PIL.Image.open("image/teststats.png")
        self.reteststats=self.teststats.resize((180,30),PIL.Image.ANTIALIAS)
        self.fteststats=ImageTk.PhotoImage(self.reteststats)
        view_test_stats_btn=Button(Dash_Frame,image=self.fteststats,command=self.test_stats_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        view_test_stats_btn.grid(row=1,column=0,padx=(0,30),pady=(0,10))

        self.penver=PIL.Image.open("image/verif.png")
        self.repenver=self.penver.resize((180,30),PIL.Image.ANTIALIAS)
        self.fpenver=ImageTk.PhotoImage(self.repenver)
        pending_verification_btn=Button(Dash_Frame,image=self.fpenver,command=self.pending_verf_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        pending_verification_btn.grid(row=2,column=0,padx=(0,30),pady=(0,10))

        self.blockacc=PIL.Image.open("image/blocked.png")
        self.reblockacc=self.blockacc.resize((180,30),PIL.Image.ANTIALIAS)
        self.fblockacc=ImageTk.PhotoImage(self.reblockacc)
        blocked_acc_btn=Button(Dash_Frame,image=self.fblockacc, command=self.blocked_acc_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        blocked_acc_btn.grid(row=3,column=0,padx=(0,30),pady=(0,10))

        #self.rules=PIL.Image.open("image/rules.png")
        #self.rerules = self.rules.resize((180,30),PIL.Image.ANTIALIAS)
        #self.frules=ImageTk.PhotoImage(self.rerules)
        #view_rules_btn=Button(Dash_Frame,image=self.frules, command=self.rules_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        #view_rules_btn.grid(row=4,column=0,padx=(0,30),pady=(0,10))
        
        #view_test_stats_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Test Stats",font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3,command=self.test_stats_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        #pending_verification_btn = Button(Dash_Frame,text="Verifications",bg="#8B0000",fg="#F0EDEE",font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3,command=self.pending_verf_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        #blocked_acc_btn = Button(Dash_Frame,text="Blocked",bg="#8B0000",fg="#F0EDEE",font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3, command=self.blocked_acc_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        
        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="TEST DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=450,height=635)

                

        #m_title = Label(Manage_Frame,text="Test Details",bg="#F0EDEE",fg="#0A090C",
        #font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)



        lbl_name = Label(Manage_Frame,text="Test Name :",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_name.grid(row = 2,column=0,pady=10,padx=10,sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name,font=("Georgia",15,"bold"),bd=5)
        txt_name.grid(row = 2,column=1,pady=10,padx=5,sticky="w")



        lbl_URL = Label(Manage_Frame,text="Test URL :", bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_URL.grid(row = 3,column=0,pady=10,padx=10,sticky="w")
        txt_URL = Entry(Manage_Frame,textvariable=self.URL,font=("Georgia",15,"bold"),bd=5)
        txt_URL.grid(row = 3,column=1,pady=10,padx=5,sticky="w")



        lbl_Date = Label(Manage_Frame,text="Test Date :",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_Date.grid(row = 4,column=0,pady=10,padx=10,sticky="w")
        self.txt_Date = Entry(Manage_Frame,textvariable=self.testDate,font=("Georgia",15,"bold"),bd=5)
        self.txt_Date.grid(row = 4,column=1,pady=10,padx=5,sticky="w")



        lbl_StartTime = Label(Manage_Frame,text="Start Time :",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_StartTime.grid(row = 5,column=0,pady=10,padx=10,sticky="w")
        self.txt_StartTime = Entry(Manage_Frame,textvariable=self.startTime,font=("Georgia",15,"bold"),bd=5)
        self.txt_StartTime.grid(row = 5,column=1,pady=10,padx=5,sticky="w")



        lbl_EndTime = Label(Manage_Frame,text="End Time :",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_EndTime.grid(row = 6,column=0,pady=10,padx=10,sticky="w")
        self.txt_EndTime = Entry(Manage_Frame,textvariable=self.endTime,font=("Georgia",15,"bold"),bd=5)
        self.txt_EndTime.grid(row = 6,column=1,pady=10,padx=5,sticky="w")



        lbl_subject = Label(Manage_Frame,text="Subject.",bg="#FFFCF9",fg="black",font=("Arial",15,"bold"))
        lbl_subject.grid(row = 7,column=0,pady=10,padx=10,sticky="w")
        txt_subject = Entry(Manage_Frame,textvariable=self.subject,font=("Georgia",15,"bold"),bd=5)
        txt_subject.grid(row = 7,column=1,pady=10,padx=5,sticky="w")

        


       


        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#FFFCF9")
        btn_frame.place(x=30,y=490,width=400) 

        self.add=PIL.Image.open("image/add.png")
        self.readd=self.add.resize((140,30),PIL.Image.ANTIALIAS)
        self.fadd=ImageTk.PhotoImage(self.readd)
        add_btn=Button(btn_frame,image=self.fadd, bd=0,cursor="hand2",command=self.add_test,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        add_btn.grid(row=0,column=0,padx=20,pady=10,sticky="nsew")

        #add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.add_test).grid(row=0,column=0,padx=5,pady=10)

        self.updt=PIL.Image.open("image/update.png")
        self.reupdt=self.updt.resize((140,30),PIL.Image.ANTIALIAS)
        self.fupdt=ImageTk.PhotoImage(self.reupdt)
        update_btn=Button(btn_frame,image=self.fupdt, bd=0,cursor="hand2",command=self.update,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        update_btn.grid(row=0,column=1,padx=20,pady=10,sticky="nsew")
        
        #update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.update).grid(row=0,column=1,padx=5,pady=10)

        self.dlt=PIL.Image.open("image/delete.png")
        self.redlt=self.dlt.resize((140,30),PIL.Image.ANTIALIAS)
        self.fdlt=ImageTk.PhotoImage(self.redlt)
        delete_btn=Button(btn_frame,image=self.fdlt, bd=0,cursor="hand2",command=self.delete,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        delete_btn.grid(row=1,column=0,padx=20,pady=10,sticky="nsew")
        
        
        #delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.delete).grid(row=0,column=2,padx=5,pady=10)
        
        self.clr=PIL.Image.open("image/clear.png")
        self.reclr=self.clr.resize((140,30),PIL.Image.ANTIALIAS)
        self.fclr=ImageTk.PhotoImage(self.reclr)
        clear_btn=Button(btn_frame,image=self.fclr, bd=0,cursor="hand2",command=self.clear_field,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        clear_btn.grid(row=1,column=1,padx=20,pady=10,sticky="nsew")
        
        #clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="ALL TEST",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")#bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=650,y=60,width=700,height=635)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=3,y=7,width=685,height=595)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Test-ID","Test-Name","Test URL","Test Date","Start Time","End Time","Subject"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Test-ID",text="Test-ID")
        self.Table.heading("Test-Name",text="Test-Name")
        self.Table.heading("Test URL",text="Test URL")
        self.Table.heading("Test Date",text="Test Date")
        self.Table.heading("Start Time",text="Start Time")
        self.Table.heading("End Time",text="End Time")

        self.Table.heading("Subject",text="Subject")



        

        self.Table['show']="headings"
        self.Table.column("Test-ID",width=50)
        self.Table.column("Test-Name",width=100)
        self.Table.column("Test URL",width=150)
        self.Table.column("Test Date",width=70)
        self.Table.column("Start Time",width=70)
        self.Table.column("End Time",width=70)        
        self.Table.column("Subject",width=60)
        
        

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        # self.txt_Date.bind("<FocusIn>", self.foc_in)
        # self.txt_Date.bind("<FocusOut>", self.foc_out)


        # self.put_placeholder()
        self.show_data()

        

    def add_test(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()

            self.TestID = random.randint(3,1000)

            curr.execute("INSERT INTO TEST_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)",
            (self.TestID, self.name.get(), self.URL.get(), self.testDate.get(), self.txt_StartTime.get(), self.txt_EndTime.get(),self.subject.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()

        

        curr.execute("SELECT * from TEST_DETAILS")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=row)

            connect.commit()
        else:
            self.Table.delete(*self.Table.get_children())
        connect.close()

        

    def clear_field(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.subject.set("")
            self.name.set("")
            self.URL.set("")
            self.testDate.set("")
            self.startTime.set("")
            self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']

            self.name.set(row[1])
            self.URL.set(row[2])
            self.testDate.set(row[3])
            self.startTime.set(row[4])
            self.endTime.set(row[5])
            self.subject.set(row[6])


        

    def update(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()



            curr.execute("UPDATE TEST_DETAILS SET TEST_URL=%s, TEST_DATE=%s, START_TIME=%s, END_TIME=%s where SUBJECT=%s AND TEST_NAME=%s",(self.URL.get(),self.testDate.get(),self.startTime.get(),self.endTime.get(),self.subject.get(),self.name.get()))

            connect.commit()

            self.show_data()
            self.clear_field()
            connect.close()

            messagebox.showinfo("Succes","Record Successfully Updated")

        

    def delete(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","Fields are Empty")

        else:

            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()
            curr.execute("DELETE from TEST_DETAILS where SUBJECT=%s AND TEST_NAME=%s",(self.subject.get(),self.name.get()))
            connect.commit()
            self.show_data()
            self.clear_field()
            connect.close()
            messagebox.showinfo("Succes","Record Successfully Deleted")

        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    # def put_placeholder(self):

    #     self.txt_Date.insert(0,"DD-MM-YYYY")
    #     self.txt_Date['fg'] = "grey"

    #     self.txt_StartTime.insert(0,"HH-MM")
    #     self.txt_StartTime['fg'] = "grey"


    # def foc_in(self,event):

    #     if self.txt_Date['fg'] == "grey":

    #         self.txt_Date.delete('0', 'end')
    #         self['fg'] = "grey"


    # def foc_out(self, event):

    #     if not self.get():
    #         self.txt_Date.put_placeholder()

    #     if not self.get():
    #         self.txt_StartTime.put_placeholder()

            

    def logout(self):

        self.root.destroy() 

        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()        
        

    def test_stats_btn(self):

        self.root.destroy() 
        st_root = Tk()
        st = Test_Stats(st_root,self.email)
        st_root.mainloop()

    def pending_verf_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Pending_Verification(st_root,self.email)
        st_root.mainloop()

    def blocked_acc_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Blocked_Accounts(st_root,self.email)
        st_root.mainloop()

    def rules_btn(self):
        self.root.destroy()
        st_root = Tk()
        st = Rules(st_root, self.email)
        st_root,mainloop()
        

##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
class Pending_Verification:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Pending Verification")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("image/admin_icon.ico")        
        self.root.resizable(0, 0) 
        self.admin_email=txt
        
        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="FACULTY DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.admin_email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.name = StringVar()
        self.studentID = StringVar()
        self.email = StringVar()
        self.Contact_No = StringVar()
       

        #self.search_combo = StringVar()
        #self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        
        self.addtest=PIL.Image.open("image/addtest.png")
        self.readdtest=self.addtest.resize((180,30),PIL.Image.ANTIALIAS)
        self.faddtest=ImageTk.PhotoImage(self.readdtest)
        add_test_btn=Button(Dash_Frame,image=self.faddtest,command=self.add_test_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        add_test_btn.grid(row=0,column=0,padx=(0,30),pady=(20,10))
        #add_test_btn = Button(Dash_Frame,bg="#8B0000",text="Add Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.teststats=PIL.Image.open("image/teststats.png")
        self.reteststats=self.teststats.resize((180,30),PIL.Image.ANTIALIAS)
        self.fteststats=ImageTk.PhotoImage(self.reteststats)
        view_test_stats_btn=Button(Dash_Frame,image=self.fteststats,command=self.test_stats_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        view_test_stats_btn.grid(row=1,column=0,padx=(0,30),pady=(0,10))

        self.penver=PIL.Image.open("image/verif.png")
        self.repenver=self.penver.resize((180,30),PIL.Image.ANTIALIAS)
        self.fpenver=ImageTk.PhotoImage(self.repenver)
        pending_verification_btn=Button(Dash_Frame,image=self.fpenver, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        pending_verification_btn.grid(row=2,column=0,padx=(0,30),pady=(0,10))

        self.blockacc=PIL.Image.open("image/blocked.png")
        self.reblockacc=self.blockacc.resize((180,30),PIL.Image.ANTIALIAS)
        self.fblockacc=ImageTk.PhotoImage(self.reblockacc)
        blocked_acc_btn=Button(Dash_Frame,image=self.fblockacc, command=self.blocked_acc_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        blocked_acc_btn.grid(row=3,column=0,padx=(0,30),pady=(0,10))


        #self.rules=PIL.Image.open("image/rules.png")
        #self.rerules = self.rules.resize((180,30),PIL.Image.ANTIALIAS)
        #self.frules=ImageTk.PhotoImage(self.rerules)
        #view_rules_btn=Button(Dash_Frame,image=self.frules, command=self.rules_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        #view_rules_btn.grid(row=4,column=0,padx=(0,30),pady=(0,10))
    
        
        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="STUDENT DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=450,height=635)

                

        #m_title = Label(Manage_Frame,text="Student Details",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)



        lbl_name = Label(Manage_Frame,text="Name : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_name.grid(row = 2,column=0,pady=(70,20),padx=(10,0),sticky="w")
        txt_name = Label(Manage_Frame,textvariable=self.name,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        txt_name.grid(row = 2,column=1,pady=(70,20),padx=5,sticky="w")



        lbl_email = Label(Manage_Frame,text="Email : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_email.grid(row = 3,column=0,pady=20,padx=(10,0),sticky="w")
        txt_email = Label(Manage_Frame,textvariable=self.email,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        txt_email.grid(row = 3,column=1,pady=20,padx=5,sticky="w")



        lbl_contact = Label(Manage_Frame,text="Contact No. : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_contact.grid(row = 4,column=0,pady=20,padx=(10,0),sticky="w")
        self.txt_contact = Label(Manage_Frame,textvariable=self.Contact_No,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        self.txt_contact.grid(row = 4,column=1,pady=20,padx=5,sticky="w")

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#FFFCF9")
        btn_frame.place(x=70,y=520,width=310) 

        self.vrf=PIL.Image.open("image/verify.png")
        self.revrf=self.vrf.resize((140,30),PIL.Image.ANTIALIAS)
        self.fvrf=ImageTk.PhotoImage(self.revrf)
        verify_btn=Button(btn_frame,image=self.fvrf, bd=0,cursor="hand2",command=self.verify_account,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        verify_btn.grid(row=0,column=0,padx=5,pady=10,sticky="nsew")
        
        #verify_btn = Button(btn_frame,text="Verify",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Georgia",10,"bold"),borderwidth = 3,command=self.verify_account).grid(row=0,column=0,padx=5,pady=10)

        self.block=PIL.Image.open("image/block.png")
        self.reblock=self.block.resize((140,30),PIL.Image.ANTIALIAS)
        self.fblock=ImageTk.PhotoImage(self.reblock)
        block_btn=Button(btn_frame,image=self.fblock, bd=0,cursor="hand2",command=self.block_account,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        block_btn.grid(row=0,column=1,padx=5,pady=10,sticky="nsew")
        
        #block_btn = Button(btn_frame,text="Block",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Georgia",10,"bold"),borderwidth = 3,command=self.block_account).grid(row=0,column=1,padx=5,pady=10)



        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="STUDENTS LIST",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")#bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=650,y=60,width=700,height=635)

       

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=3,y=7,width=685,height=595)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Student-ID","Full Name","Contact","Email"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Student-ID",text="Student-ID")
        self.Table.heading("Full Name",text="Full Name")
        self.Table.heading("Contact",text="Contact")
        self.Table.heading("Email",text="Email")

        
        self.Table['show']="headings"
        self.Table.column("Student-ID",width=50)
        self.Table.column("Full Name",width=100)
        self.Table.column("Contact",width=100)
        self.Table.column("Email",width=180)


        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        #self.txt_Date.bind("<FocusIn>", self.foc_in)
        #self.txt_Date.bind("<FocusOut>", self.foc_out)


        #self.put_placeholder()
        self.show_data()


    
    def verify_account(self):
        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("UPDATE USERS SET VERIFIED='1' WHERE EMAIL=%s", (self.email.get()))
        receiver_email = self.email.get() # Receiver address
        connect.commit()
        self.show_data()
        self.clear_field()
        connect.close()

        #SENDING VERIFICATION SUCCESSFUL EMAIL TO USER
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "team.cordonbleu@gmail.com"  # Sender Adress
        password = "cordon@123"
        message = """\
        Subject: Account Verification

        ******Greetings from your Proctor******
        Your account has been verified by the admin and is ready to be used.
        All the best for your exams !"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        
            
    
    def block_account(self):
        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("UPDATE USERS SET BLOCKED=%s WHERE EMAIL=%s", (1,self.email.get()))
        connect.commit()
        self.clear_field()
        self.show_data()
        connect.close()
        messagebox.showinfo("Succes","Account blocked !")

        
 
    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("SELECT * from USERS WHERE VERIFIED=%s AND BLOCKED=%s", (0,0))
        rows = curr.fetchall()
        if(len(rows)>0):
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=(row[0],row[1],row[2],row[3]))

            connect.commit()
        else:
            self.Table.delete(*self.Table.get_children())
        connect.close()        


        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']

            self.studentID.set(row[0])
            self.name.set(row[1])
            self.Contact_No.set(row[2])
            self.email.set(row[3])

    def clear_field(self):
            self.name.set("")
            self.studentID.set("")
            self.email.set("")
            self.Contact_No.set("")

    #def put_placeholder(self):
         #self.txt_Date.insert(0,"DD-MM-YYYY")
         #self.txt_Date['fg'] = "grey"
         #self.txt_StartTime.insert(0,"HH-MM")
         #self.txt_StartTime['fg'] = "grey"


    #def foc_in(self,event):

         #if self.txt_Date['fg'] == "grey":

             #self.txt_Date.delete('0', 'end')
             #self['fg'] = "grey"

    #def foc_out(self, event):

         #if not self.get():
             #self.txt_Date.put_placeholder()

         #if not self.get():
             #self.txt_StartTime.put_placeholder()


    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()

    def add_test_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Faculty(st_root,self.admin_email)
        st_root.mainloop()

    def test_stats_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Test_Stats(st_root,self.admin_email)
        st_root.mainloop()

    def blocked_acc_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Blocked_Accounts(st_root,self.admin_email)
        st_root.mainloop()

    def rules_btn(self):
        self.root.destroy()
        st_root = Tk()
        st = Rules(st_root, self.email)
        st_root,mainloop()

##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################

class Blocked_Accounts:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Blocked Accounts")
        self.root.geometry("1350x700+0+0")
        self.root.iconbitmap("image/admin_icon.ico")
        self.root.resizable(0, 0) 
        self.admin_email=txt
        
        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="FACULTY DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.admin_email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.name = StringVar()
        self.studentID = StringVar()
        self.email = StringVar()
        self.Contact_No = StringVar()
       

        #self.search_combo = StringVar()
        #self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        
        self.addtest=PIL.Image.open("image/addtest.png")
        self.readdtest=self.addtest.resize((180,30),PIL.Image.ANTIALIAS)
        self.faddtest=ImageTk.PhotoImage(self.readdtest)
        add_test_btn=Button(Dash_Frame,image=self.faddtest, command=self.add_test_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        add_test_btn.grid(row=0,column=0,padx=(0,30),pady=(20,10))
        #add_test_btn = Button(Dash_Frame,bg="#8B0000",text="Add Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.teststats=PIL.Image.open("image/teststats.png")
        self.reteststats=self.teststats.resize((180,30),PIL.Image.ANTIALIAS)
        self.fteststats=ImageTk.PhotoImage(self.reteststats)
        view_test_stats_btn=Button(Dash_Frame,image=self.fteststats,command=self.test_stats_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        view_test_stats_btn.grid(row=1,column=0,padx=(0,30),pady=(0,10))

        self.penver=PIL.Image.open("image/verif.png")
        self.repenver=self.penver.resize((180,30),PIL.Image.ANTIALIAS)
        self.fpenver=ImageTk.PhotoImage(self.repenver)
        pending_verification_btn=Button(Dash_Frame,image=self.fpenver,command=self.pending_verf_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        pending_verification_btn.grid(row=2,column=0,padx=(0,30),pady=(0,10))

        self.blockacc=PIL.Image.open("image/blocked.png")
        self.reblockacc=self.blockacc.resize((180,30),PIL.Image.ANTIALIAS)
        self.fblockacc=ImageTk.PhotoImage(self.reblockacc)
        blocked_acc_btn=Button(Dash_Frame,image=self.fblockacc, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        blocked_acc_btn.grid(row=3,column=0,padx=(0,30),pady=(0,10))

        #self.rules=PIL.Image.open("image/rules.png")
        #self.rerules = self.rules.resize((180,30),PIL.Image.ANTIALIAS)
        #self.frules=ImageTk.PhotoImage(self.rerules)
        #view_rules_btn=Button(Dash_Frame,image=self.frules, command=self.rules_btn, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")
        #view_rules_btn.grid(row=4,column=0,padx=(0,30),pady=(0,10))
        
        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="STUDENT DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=450,height=635)

                

        #m_title = Label(Manage_Frame,text="Student Details",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)



        lbl_name = Label(Manage_Frame,text="Name : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_name.grid(row = 2,column=0,pady=(70,20),padx=(10,0),sticky="w")
        txt_name = Label(Manage_Frame,textvariable=self.name,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        txt_name.grid(row = 2,column=1,pady=(70,20),padx=5,sticky="w")



        lbl_email = Label(Manage_Frame,text="Email : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_email.grid(row = 3,column=0,pady=20,padx=(10,0),sticky="w")
        txt_email = Label(Manage_Frame,textvariable=self.email,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        txt_email.grid(row = 3,column=1,pady=20,padx=5,sticky="w")



        lbl_contact = Label(Manage_Frame,text="Contact No. : ",bg="#FFFCF9",fg="black",font=("Georgia",12,"bold"))
        lbl_contact.grid(row = 4,column=0,pady=20,padx=(10,0),sticky="w")
        self.txt_contact = Label(Manage_Frame,textvariable=self.Contact_No,font=("Georgia",12),anchor="w",height=1,width=30,borderwidth=2, relief="solid")
        self.txt_contact.grid(row = 4,column=1,pady=20,padx=5,sticky="w")

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#FFFCF9")
        btn_frame.place(x=140,y=520,width=210) 

        self.unbl=PIL.Image.open("image/unblock.png")
        self.reunbl=self.unbl.resize((140,30),PIL.Image.ANTIALIAS)
        self.funbl=ImageTk.PhotoImage(self.reunbl)
        start_btn=Button(btn_frame,image=self.funbl, bd=0,cursor="hand2",command=self.unblock_account,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        start_btn.grid(row=0,column=1,padx=5,pady=10,sticky="nsew")
        
        #unblock_btn = Button(btn_frame,text="Unblock",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.unblock_account).grid(row=0,column=1,padx=5,pady=10)



        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="STUDENTS LIST",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=650,y=60,width=700,height=635)

       

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=3,y=7,width=685,height=595)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Student-ID","Full Name","Contact","Email"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Student-ID",text="Student-ID")
        self.Table.heading("Full Name",text="Full Name")
        self.Table.heading("Contact",text="Contact")
        self.Table.heading("Email",text="Email")

        
        self.Table['show']="headings"
        self.Table.column("Student-ID",width=50)
        self.Table.column("Full Name",width=100)
        self.Table.column("Contact",width=100)
        self.Table.column("Email",width=180)


        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        #self.txt_Date.bind("<FocusIn>", self.foc_in)
        #self.txt_Date.bind("<FocusOut>", self.foc_out)


        #self.put_placeholder()
        self.show_data()


    
    def unblock_account(self):
        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("UPDATE USERS SET BLOCKED='0' WHERE EMAIL=%s", (self.email.get()))
        receiver_email = self.email.get() # Receiver address
        connect.commit()
        self.show_data()
        self.clear_field()
        connect.close()

        #SENDING VERIFICATION SUCCESSFUL EMAIL TO USER
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "team.cordonbleu@gmail.com"  # Sender Adress
        password = "cordon@123"
        message = """\
        Subject: Account Unblocked

        ******Greetings from your Proctor******
        Your account has been unblocked by the admin. 
        Wait for it to be verified, before you can start using it.
        All the best for your exams !"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        

        
 
    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("SELECT * from USERS WHERE BLOCKED=%s", (1))
        rows = curr.fetchall()
        if(len(rows)>0):
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                self.Table.insert('',END,values=(row[0],row[1],row[2],row[3]))

            connect.commit()
        else:
            self.Table.delete(*self.Table.get_children())
        connect.close()        


        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']

            self.studentID.set(row[0])
            self.name.set(row[1])
            self.Contact_No.set(row[2])
            self.email.set(row[3])

    def clear_field(self):
            self.name.set("")
            self.studentID.set("")
            self.email.set("")
            self.Contact_No.set("")

    #def put_placeholder(self):
         #self.txt_Date.insert(0,"DD-MM-YYYY")
         #self.txt_Date['fg'] = "grey"
         #self.txt_StartTime.insert(0,"HH-MM")
         #self.txt_StartTime['fg'] = "grey"


    #def foc_in(self,event):

         #if self.txt_Date['fg'] == "grey":

             #self.txt_Date.delete('0', 'end')
             #self['fg'] = "grey"

    #def foc_out(self, event):

         #if not self.get():
             #self.txt_Date.put_placeholder()

         #if not self.get():
             #self.txt_StartTime.put_placeholder()


    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()

    def add_test_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Faculty(st_root,self.admin_email)
        st_root.mainloop()

    def test_stats_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Test_Stats(st_root,self.admin_email)
        st_root.mainloop()

    def pending_verf_btn(self):
        self.root.destroy() 
        st_root = Tk()
        st = Pending_Verification(st_root,self.admin_email)
        st_root.mainloop()

    def rules_btn(self):
        self.root.destroy()
        st_root = Tk()
        st = Rules(st_root, self.email)
        st_root,mainloop()


##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


class Student:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Student DashBoard")
        self.root.geometry("1350x700+0+0")

        self.root.iconbitmap("image/uni.ico") 
        self.root.resizable(0, 0) 
        self.email = txt

        #master = Tk()

        #p1 = ImageTk.PhotoImage(file="image/uni.png")
        #master.iconphoto(False, p1)


        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="STUDENT DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        #self.pp = PIL.Image.open("ImagesAttendance/"+self.email_id+".jpeg")

        #self.resized = self.pp.resize((200,225), PIL.Image.ANTIALIAS)
        
        #self.new_pic = ImageTk.PhotoImage(self.resized)
        #self.pp = self.pp.resize((450, 350), Image. ANTIALIAS)
        #my_label = Label(Manage_Frame, image=self.new_pic, borderwidth=3, relief="solid").place(x=700, y=100)
        
        

        #Variables
        self.name = StringVar()
        self.testDate = StringVar()
        self.startTime = StringVar()
        self.endTime = StringVar()
        self.subject = StringVar()
        self.URL = StringVar()
        self.TestID = StringVar()
       

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        self.test=PIL.Image.open("image/tes.png")
        self.retest=self.test.resize((180,30),PIL.Image.ANTIALIAS)
        self.ftest=ImageTk.PhotoImage(self.retest)
        btn_test=Button(Dash_Frame,image=self.ftest, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_test.grid(row=0,column=0,padx=(0,30),pady=(20,10))

        #Test_btn = Button(Dash_Frame,bg="#8B0000",text="Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.profile=PIL.Image.open("image/profile.png")
        self.reprofile=self.profile.resize((180,30),PIL.Image.ANTIALIAS)
        self.fprofile=ImageTk.PhotoImage(self.reprofile)
        btn_profile=Button(Dash_Frame,image=self.fprofile,command= partial(self.student_profile_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_profile.grid(row=1,column=0,padx=(0,30),pady=(0,10))
        
        #student_profile_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Profile", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3,command= partial(self.student_profile_btn,self.email)).grid(row=1,column=0,padx=2,pady=2,sticky="w")


        self.stat=PIL.Image.open("image/stat.png")
        self.restat=self.stat.resize((180,30),PIL.Image.ANTIALIAS)
        self.fstat=ImageTk.PhotoImage(self.restat)
        btn_stat=Button(Dash_Frame,image=self.fstat,command= partial(self.student_test_stats_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_stat.grid(row=2,column=0,padx=(0,30),pady=(0,10))
        
        #student_test_stats_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Your Statistics", font=("Arial",9,"bold"),relief=RAISED,width=11,borderwidth = 3,pady=20,command= partial(self.student_test_stats_btn,self.email)).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        #tk.Button(Dash_Frame,bg="#8B0000", text="Employee",fg="#F0EDEE",command=lambda: master.switch_frame(employee_btn)).pack()

        # department_btn = Button(Dash_Frame,text="Department",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="TEST DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=200,y=60,width=450,height=635)

                

        #m_title = Label(Manage_Frame,text="Test Details",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)

        #m_title = Label(Manage_Frame,text="Test Details",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)

        lbl_name = Label(Manage_Frame,text="Test Name.",bg="#FFFCF9",fg="black",font=("Georgia",15,"bold"))
        lbl_name.grid(row = 2,column=0,pady=(70,20),padx=40,sticky="w")

    

        txt_name = Label(Manage_Frame,textvariable=self.name,font=("Georgia",15,"bold"),height=1,width=15,borderwidth=2, relief="solid")
        txt_name.grid(row = 2,column=1,pady=(70,20),padx=10,sticky="w")



##        lbl_URL = Label(Manage_Frame,text="Test URL.", bg="#F0EDEE",fg="black",font=("Arial",15,"bold"))
##        lbl_URL.grid(row = 3,column=0,pady=10,padx=20,sticky="w")
##
##
##        txt_URL = Entry(Manage_Frame,textvariable=self.URL,font=("Arial",15,"bold"),bd=5,relief=RAISED)
##        txt_URL.grid(row = 3,column=1,pady=10,padx=20,sticky="w")



        lbl_subject = Label(Manage_Frame,text="Subject.",bg="#FFFCF9",fg="black",font=("Georgia",15,"bold"))
        lbl_subject.grid(row = 3,column=0,pady=20,padx=40,sticky="w")

    

        txt_subject = Label(Manage_Frame,textvariable=self.subject,font=("Georgia",15,"bold"),height=1,width=15,borderwidth=2, relief="solid")
        txt_subject.grid(row = 3,column=1,pady=10,padx=10,sticky="w")



        lbl_Date = Label(Manage_Frame,text="Test Date.",bg="#FFFCF9",fg="black",font=("Georgia",15,"bold"))
        lbl_Date.grid(row = 4,column=0,pady=20,padx=40,sticky="w")

    

        self.txt_Date = Label(Manage_Frame,textvariable=self.testDate,font=("Georgia",15,"bold"),height=1,width=15,borderwidth=2, relief="solid")
        self.txt_Date.grid(row = 4,column=1,pady=10,padx=10,sticky="w")

        

        lbl_StartTime = Label(Manage_Frame,text="Start Time.",bg="#FFFCF9",fg="black",font=("Georgia",15,"bold"))
        lbl_StartTime.grid(row = 5,column=0,pady=20,padx=40,sticky="w")


        self.txt_StartTime = Label(Manage_Frame,textvariable=self.startTime,font=("Georgia",15,"bold"),height=1,width=15,borderwidth=2, relief="solid")
        self.txt_StartTime.grid(row = 5,column=1,pady=10,padx=10,sticky="w")

        lbl_EndTime = Label(Manage_Frame,text="End Time.",bg="#FFFCF9",fg="black",font=("Georgia",15,"bold"))
        lbl_EndTime.grid(row = 6,column=0,pady=20,padx=40,sticky="w")


        self.txt_EndTime = Label(Manage_Frame,textvariable=self.endTime,font=("Georgia",15,"bold"),height=1,width=15,borderwidth=2, relief="solid")
        self.txt_EndTime.grid(row = 6,column=1,pady=10,padx=10,sticky="w")



        

        


       


        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#FFFCF9")
        btn_frame.place(x=12,y=540,width=410)

        self.strt=PIL.Image.open("image/start.png")
        self.restrt=self.strt.resize((140,30),PIL.Image.ANTIALIAS)
        self.fstrt=ImageTk.PhotoImage(self.restrt)
        start_btn=Button(btn_frame,image=self.fstrt, bd=0,cursor="hand2",command=self.start_test,bg="#FFFCF9",activebackground="#FFFCF9")#.place(x=230,y=320)
        start_btn.grid(row=0,column=2,padx=140,pady=10,sticky="nsew")

        #start_btn = Button(btn_frame,text="Start Test",width=10,bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),borderwidth = 3,command=self.start_test).grid(row=0,column=0,padx=170,pady=10)

        #end_btn = Button(btn_frame,text="End Test",width=10,bg="#8B0000",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.end_test).grid(row=0,column=1,padx=5,pady=10)
        

##        add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)
##
##        update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)
##
##        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)
##
##        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="UPCOMING TEST",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")#bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=650,y=60,width=700,height=635)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,borderwidth = 3,pady=5,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=3,y=7,width=685,height=550)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Test-ID","Test-Name","Subject","Test Date","Start Time","End Time"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        self.Table.heading("Test-ID",text="Test-ID")
        self.Table.heading("Test-Name",text="Test-Name")
        self.Table.heading("Subject",text="Subject")
        self.Table.heading("Test Date",text="Test Date")
        self.Table.heading("Start Time",text="Start Time")
        self.Table.heading("End Time",text="End Time")
        



        

        self.Table['show']="headings"
        self.Table.column("Test-ID",width=40)
        self.Table.column("Test-Name",width=70)
        self.Table.column("Subject",width=70)
        self.Table.column("Test Date",width=60)
        self.Table.column("Start Time",width=60)
        self.Table.column("End Time",width=60)
        
        
        

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        #self.txt_Date.bind("<FocusIn>", self.foc_in)
        #self.txt_Date.bind("<FocusOut>", self.foc_out)


        #self.put_placeholder()
        self.show_data(self.email)


    #def run_io_tasks_in_parallel(tasks):
        #with ThreadPoolExecutor(max_workers = 2) as executor:
            #running_tasks = [executor.submit(task) for task in tasks]
            #for running_task in running_tasks:
                #running_task.result()



    
    def start_test(self):
        
        if self.URL.get()=="":
            messagebox.showerror("Error","Select the test")
        else:
            test_starttime=datetime.strptime(self.startTime.get(), '%H:%M:%S').time()
            test_startdate=datetime.strptime(self.testDate.get(), '%Y-%m-%d').date()
            if (date.today()!=test_startdate) or ((date.today()==test_startdate) and (test_starttime>datetime.strptime(datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time())) :
                messagebox.showerror("Error","Wait till exam start Time")
            else:
                connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                curr = connect.cursor()

                curr.execute("SELECT * FROM ONLINE WHERE EMAIL=%s AND TEST_ID=%s", (self.email,self.TestID.get()))
                row = curr.fetchone()
                if row==None:
                    cur = connect.cursor()
                    cur.execute("INSERT INTO ONLINE (STARTED, EMAIL, TEST_ID, WORDS_SPOKEN, MULTIPLE_PERSON_DETECTION, MOBILE_PHONE_DETECTION, NO_PERSON_DETECTION, STUDY_MATERIAL_DETECTION) VALUES (0, %s, %s, 0, 0, 0, 0, 0)", (self.email,self.TestID.get()))                               

                connect.commit()
                connect.close()
                messagebox.showinfo("Test Rules","1. Examinee has to look straight into the webcam to initialise the test.\n2. Nobody other than the examinee must be present in the same room.\n3. Examinee is not allowed to leave the place for the duration of the test.\n4. Use of mobile phones/tablets is strictly prohibited during any test.\n5. Examinee must not speak at all during the duration of the test.\n*ALL THE BEST FOR YOUR EXAM !*\n")

                if check_face(self.email):
                    con = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                    cur = con.cursor()
                    cur.execute("UPDATE ONLINE SET STARTED=%s  WHERE EMAIL=%s AND TEST_ID=%s", (1,self.email,self.TestID.get()))
                    con.commit()
                    con.close()
                    webbrowser.open(self.URL.get(),new=1)
                    Thread(target = self.wait_time).start()
                    
    def wait_time(self):
        stop_threads=False
        t1 = Thread(target = start_multiplepersons, args=(lambda : stop_threads,self.email,self.TestID.get()))
        t1.start()
        curr_time=datetime.strptime(datetime.now().strftime("%H:%M:%S"), '%H:%M:%S')
        end_time=datetime.strptime(self.endTime.get(), '%H:%M:%S')
        diff = (end_time - curr_time) 
        #print(diff.seconds) 
        
        t2 = Thread(target = start_audio, args=(diff.seconds,self.email,self.TestID.get()))
        t2.start()
        t3 = Thread(target = userActivityTracking, args=(lambda : stop_threads,self.email,self.TestID.get()))
        t3.start()

        
        test_time=datetime.strptime(self.endTime.get(), '%H:%M:%S').time()
        
        while(datetime.strptime(datetime.now().strftime("%H:%M:%S"), '%H:%M:%S').time()<test_time):
            time.sleep(1)

        stop_threads=True
        t1.join()
        t2.join()
        t3.join()
        print('Test Ended')
        messagebox.showinfo("Succes","Times up")        
            
    
    def end_test(self):
        if self.URL.get()=="":
            messagebox.showerror("Error","Select the test")
        else:
            webbrowser.open(self.URL.get(),new=1)
            print(self.TestID.get)
            start(self.email,self.TestID.get())
            
            
    

        

    def show_data(self, email):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()
        curr.execute("SELECT TEST_ID, TEST_NAME, SUBJECT, TEST_URL, TEST_DATE, START_TIME, END_TIME from TEST_DETAILS")
        rows = curr.fetchall()
        if(len(rows)!=0):
            self.Table.delete(*self.Table.get_children())
            for row in rows:
                now = datetime.now()
                current_time = timedelta(hours=int(now.strftime("%H")),minutes=int(now.strftime("%M")), seconds=int(now.strftime("%S")))
                if(date.today()<row[4]) or ((date.today()==row[4]) and (current_time<row[6])):
                    self.Table.insert('',END,values=(row[0],row[1],row[2],row[4],row[5],row[6]))

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.subject.set("")
            self.name.set("")
            self.URL.set("")
            self.testDate.set("")
            self.startTime.set("")
            self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']

            self.TestID.set(row[0])
            self.name.set(row[1])
            self.subject.set(row[2])
            self.testDate.set(row[3])
            self.startTime.set(row[4])
            self.endTime.set(row[5])

            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()

            curr.execute("SELECT TEST_URL from TEST_DETAILS WHERE TEST_ID=%s",(row[0]))
            self.url1 = curr.fetchone()
            # print(url)

            self.URL.set(*self.url1)
            connect.commit()
            connect.close()
   
        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    #def put_placeholder(self):
         #self.txt_Date.insert(0,"DD-MM-YYYY")
         #self.txt_Date['fg'] = "grey"
         #self.txt_StartTime.insert(0,"HH-MM")
         #self.txt_StartTime['fg'] = "grey"


    #def foc_in(self,event):

         #if self.txt_Date['fg'] == "grey":

             #self.txt_Date.delete('0', 'end')
             #self['fg'] = "grey"
            


    #def foc_out(self, event):

         #if not self.get():
             #self.txt_Date.put_placeholder()

         #if not self.get():
             #self.txt_StartTime.put_placeholder()

    def student_profile_btn(self,email):
        self.root.destroy()
        st_root = Tk()
        st = Student_Profile(st_root,email)
        st_root.mainloop()

    def student_test_stats_btn(self,email):
        self.root.destroy()
        st_root = Tk()
        st = Student_Test_Stats(st_root,email)
        st_root.mainloop()

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()


##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
        


class Student_Profile:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Student Profile")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0, 0) 

        self.email=txt
        

        

        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="STUDENT DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.email_id = txt
        self.name = StringVar()
        self.mobileNumber = StringVar()
        self.studentId = StringVar()
        self.numberOfExams = StringVar()
        #self.dp = StringVar()
       

        

        #self.search_combo = StringVar()
        #self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        self.test=PIL.Image.open("image/tes.png")
        self.retest=self.test.resize((180,30),PIL.Image.ANTIALIAS)
        self.ftest=ImageTk.PhotoImage(self.retest)
        btn_test=Button(Dash_Frame,image=self.ftest,command= partial(self.test_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_test.grid(row=0,column=0,padx=(0,30),pady=(20,10))

        #Test_btn = Button(Dash_Frame,bg="#8B0000",text="Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.profile=PIL.Image.open("image/profile.png")
        self.reprofile=self.profile.resize((180,30),PIL.Image.ANTIALIAS)
        self.fprofile=ImageTk.PhotoImage(self.reprofile)
        btn_profile=Button(Dash_Frame,image=self.fprofile, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_profile.grid(row=1,column=0,padx=(0,30),pady=(0,10))
        
        #student_profile_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Profile", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3,command= partial(self.student_profile_btn,self.email)).grid(row=1,column=0,padx=2,pady=2,sticky="w")


        self.stat=PIL.Image.open("image/stat.png")
        self.restat=self.stat.resize((180,30),PIL.Image.ANTIALIAS)
        self.fstat=ImageTk.PhotoImage(self.restat)
        btn_stat=Button(Dash_Frame,image=self.fstat,command= partial(self.student_test_stats_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_stat.grid(row=2,column=0,padx=(0,30),pady=(0,10))
        
        #tk.Button(Dash_Frame,bg="#8B0000", text="Employee",fg="#F0EDEE",command=lambda: master.switch_frame(employee_btn)).pack()

        # department_btn = Button(Dash_Frame,text="Department",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="STUDENT DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=1151,height=635)

                

        #m_title = Label(Manage_Frame,text="Student Details",bg="#F0EDEE",fg="#0A090C",font=("Arial",30,"bold","italic"))
        #m_title.grid(row = 0,columnspan=2,pady=20)


        con=pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        cur=con.cursor()
        cur.execute("select * from users where email=%s",(self.email_id))
        row=cur.fetchone()
        self.studentId = row[0]
        self.name = row[1]
        self.mobileNumber = row[2]
        self.dp_binary = row[6]

        with open('ImagesAttendance/'+self.email_id+'.jpeg','wb') as f:
            f.write(self.dp_binary)
        #self.dp = self.db_binary.codecs.decode('base64')

        #self.test = ImageTk.PhotoImage('ImagesAttendance/sahil.pradhan51@gmail.com.jpeg')
        #bg=Label(self.root,image=self.bg).place(x=10,y=10)


        self.pp = PIL.Image.open("ImagesAttendance/"+self.email_id+".jpeg")

        self.resized = self.pp.resize((200,225), PIL.Image.ANTIALIAS)
        
        self.new_pic = ImageTk.PhotoImage(self.resized)
        #self.pp = self.pp.resize((450, 350), Image. ANTIALIAS)
        my_label = Label(Manage_Frame, image=self.new_pic, borderwidth=3, relief="solid").place(x=900, y=10)
        #my_label.grid(column=3,sticky="w")

        #self.image = Image.open("ImagesAttendance/"+self.email_id+".jpeg")
        #self.image = image.resize((250, 250), Image.ANTIALIAS) ## The (250, 250) is (height, width)
        #self.pw.pic = ImageTk.PhotoImage(image)
        #pp = Label(self.root,image=self.image).place(x=200,y=200)

        
        #self.write_file(self.dp,self.email_id)
        #pic = ImageTk.PhotoImage(Image.open(self.dp))

        con.commit()
        con.close()

        conn=pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr=conn.cursor()
        curr.execute("select * from online where email=%s",(self.email_id))
        rows = curr.fetchall()
        if len(rows)==0:
            self.numberOfExams = 0;
        else:
            self.numberOfExams = len(rows)
        conn.commit()
        conn.close()
        
        #lbl_pic = Label(Manage_Frame,text="Student Photo : ",bg="#F0EDEE",fg="black",font=("Arial",15,"bold"))
        #lbl_pic.grid(row = 0,column=0,pady=10,padx=20,sticky="w")
    

        lbl_id = Label(Manage_Frame,text="Student ID : ",bg="#FFFCF9",fg="black",font=("Georgia",13,"bold"))
        lbl_id.grid(row = 1,column=0,pady=(30,10),padx=(50,20),sticky="w")
        txt_id = Label(Manage_Frame,text=self.studentId,font=("Georgia",12),height=1,width=30,borderwidth=2, relief="solid")
        txt_id.grid(row = 1,column=1,pady=(30,10),padx=20,sticky="w")



        lbl_name = Label(Manage_Frame,text="Student Name : ",bg="#FFFCF9",fg="black",font=("Georgia",13,"bold"))
        lbl_name.grid(row = 2,column=0,pady=10,padx=(50,20),sticky="w")
        txt_name = Label(Manage_Frame,text=self.name,font=("Georgia",12),height=1,width=30,borderwidth=2, relief="solid")
        txt_name.grid(row = 2,column=1,pady=10,padx=20,sticky="w")



        lbl_email = Label(Manage_Frame,text="Email : ",bg="#FFFCF9",fg="black",font=("Georgia",13,"bold"))
        lbl_email.grid(row = 3,column=0,pady=10,padx=(50,20),sticky="w")
        txt_email = Label(Manage_Frame,text=self.email_id,font=("Georgia",12),height=1,width=30,borderwidth=2, relief="solid")
        txt_email.grid(row = 3,column=1,pady=10,padx=20,sticky="w")



        lbl_mobile = Label(Manage_Frame,text="Mobile : ",bg="#FFFCF9",fg="black",font=("Georgia",13,"bold"))
        lbl_mobile.grid(row = 4,column=0,pady=10,padx=(50,20),sticky="w")
        txt_mobile = Label(Manage_Frame,text=self.mobileNumber,font=("Georgia",12),height=1,width=30,borderwidth=2, relief="solid")
        txt_mobile.grid(row = 4,column=1,pady=10,padx=20,sticky="w")



        lbl_exams = Label(Manage_Frame,text="Number of Exams completed : ",bg="#FFFCF9",fg="black",font=("Georgia",13,"bold"))
        lbl_exams.grid(row = 5,column=0,pady=10,padx=(50,20),sticky="w")
        txt_exams = Label(Manage_Frame,text=self.numberOfExams,font=("Georgia",12),height=1,width=30,borderwidth=2, relief="solid")
        txt_exams.grid(row = 5,column=1,pady=10,padx=20,sticky="w")


        

        #logout_btn = Button(Manage_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)


        

        #Button Frame
        btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        btn_frame.place(x=12,y=520,width=410) 

        #start_btn = Button(btn_frame,text="Start Test",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.start_test).grid(row=0,column=0,padx=5,pady=10)

        #end_btn = Button(btn_frame,text="End Test",width=10,bg="#8B0000",fg="#FFFCF9",font=("Arial",10,"bold"),command=self.end_test).grid(row=0,column=1,padx=5,pady=10)
        

##        add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)
##
##        update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)
##
##        delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)
##
##        clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9",
##        font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        #Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#FFFCF9")
        #Detail_Frame.place(x=550,y=95,width=800,height=600)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)


        

        #Table Frame

        #Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        #Table_Frame.place(x=10,y=60,width=760,height=505)

        

        #X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        #Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        #self.Table = ttk.Treeview(Table_Frame,columns=("Test-ID","Test-Name","Subject","Test Date","Start Time"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        #X_scroll.pack(side=BOTTOM,fill=X)
        #Y_scroll.pack(side=RIGHT,fill=Y)
        #X_scroll.config(command=self.Table.xview)
        #Y_scroll.config(command=self.Table.yview)

        #self.Table.heading("Test-ID",text="Test-ID")
        #self.Table.heading("Test-Name",text="Test-Name")
        #self.Table.heading("Subject",text="Subject")
        #self.Table.heading("Test Date",text="Test Date")
        #self.Table.heading("Start Time",text="Start Time")
        



        

        #self.Table['show']="headings"
        #self.Table.column("Test-ID",width=100)
        #self.Table.column("Test-Name",width=100)
        #self.Table.column("Subject",width=100)
        #self.Table.column("Test Date",width=100)
        #self.Table.column("Start Time",width=100)
        
        
        

        

        #self.Table.pack(fill=BOTH,expand=1)
        #self.Table.bind('<ButtonRelease 1>',self.get_fields)
        #self.txt_Date.bind("<FocusIn>", self.foc_in)
        #self.txt_Date.bind("<FocusOut>", self.foc_out)


        #self.put_placeholder()
        #self.show_data()


    #def run_io_tasks_in_parallel(tasks):
        #with ThreadPoolExecutor(max_workers = 2) as executor:
            #running_tasks = [executor.submit(task) for task in tasks]
            #for running_task in running_tasks:
                #running_task.result()
    def write_file(self, data, filename):
    # Convert binary data to proper format and write it on Hard Disk
        with open(filename, 'wb') as file:
            file.write(data)




    
    def start_test(self):
        if self.URL.get()=="":
            messagebox.showerror("Error","Select the test")
        else:
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()
            curr.execute("INSERT INTO ONLINE (STARTED, EMAIL, TEST_ID) VALUES (1, %s, %s)", (self.email,self.TestID.get()))
            connect.commit()
            connect.close()
            
            webbrowser.open(self.URL.get(),new=1)
            
            Thread(target = self.wait_time).start()
            
    def wait_time(self):
        stop_threads=False
        t1 = Thread(target = start_multiplepersons, args=(lambda : stop_threads,self.email,self.TestID.get()))
        t1.start()
        t2 = Thread(target = start_audio, args=(self.email,self.TestID.get()))
        t2.start()

        time.sleep(20)
        stop_threads=True
        t1.join()
        t2.join()
        print('Test Ended')
        messagebox.showinfo("Succes","Times up")        
            
    
    def end_test(self):
        if self.URL.get()=="":
            messagebox.showerror("Error","Select the test")
        else:
            webbrowser.open(self.URL.get(),new=1)
            print(self.TestID.get)
            start(self.email,self.TestID.get())
            
            
    

        

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()

        

        curr.execute("SELECT TEST_ID, TEST_NAME, SUBJECT, TEST_URL, TEST_DATE, START_TIME, END_TIME from TEST_DETAILS")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=(row[0],row[1],row[2],row[4],row[5],row[6]))

            connect.commit()
        connect.close()

        

    def clear_field(self):

        if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

            messagebox.showerror("Error","All Fields are Required")

        else:

            self.subject.set("")
            self.name.set("")
            self.URL.set("")
            self.testDate.set("")
            self.startTime.set("")
            self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        content = self.Table.item(cursor_row)
        row = content['values']

        

        
       
        self.TestID.set(row[0])
        self.name.set(row[1])
        self.subject.set(row[2])
        self.testDate.set(row[3])
        self.startTime.set(row[4])
        self.endTime.set(row[5])

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()

        curr.execute("SELECT TEST_URL from TEST_DETAILS WHERE TEST_ID=%s",(row[0]))
        self.url1 = curr.fetchone()
        # print(url)

        self.URL.set(*self.url1)
        connect.commit()
        connect.close()
   
        

    def search_data(self):

        if self.search_combo.get() == "" or self.search_field.get() == "":

            messagebox.showerror("Error","Some Fields might be Empty")

        else:

            connect = pymysql.connect("localhost","root","","ai_proctor")
            curr = connect.cursor()

            

            curr.execute("SELECT * from student where "+str(self.search_combo.get())+
                         " LIKE '%"+str(self.search_field.get())+"%'")

            rows = curr.fetchall()

            if(len(rows)!=0):

                self.Table.delete(*self.Table.get_children())

                for row in rows:

                    self.Table.insert('',END,values=row)

                connect.commit()
            connect.close()

            

    #def put_placeholder(self):
         #self.txt_Date.insert(0,"DD-MM-YYYY")
         #self.txt_Date['fg'] = "grey"
         #self.txt_StartTime.insert(0,"HH-MM")
         #self.txt_StartTime['fg'] = "grey"


    #def foc_in(self,event):

         #if self.txt_Date['fg'] == "grey":

             #self.txt_Date.delete('0', 'end')
             #self['fg'] = "grey"
            


    #def foc_out(self, event):

         #if not self.get():
             #self.txt_Date.put_placeholder()

         #if not self.get():
             #self.txt_StartTime.put_placeholder()

    def test_btn(self,email):

        self.root.destroy()
        st_root = Tk()
        st = Student(st_root,email)
        st_root.mainloop()

    def student_test_stats_btn(self,email):
        self.root.destroy()
        st_root = Tk()
        st = Student_Test_Stats(st_root,email)
        st_root.mainloop()


    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()


##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################


class Student_Test_Stats:

    def __init__(self,root,txt):
        self.root = root
        self.root.title("Student DashBoard")
        self.root.geometry("1350x700+0+0")
        self.root.resizable(0, 0) 
        self.email=txt

        logo_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#ff8f18")
        logo_Frame.place(x=0,y=0,width=198,height=60)
        
        logotitle = Label(logo_Frame,text="PROCTORX",font=("Georgia",20,"bold"),fg="#ffffff",bg="#ff8f18")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        logotitle.grid(row=0,column=1,pady=(5,0))
        
        nav_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        nav_Frame.place(x=199,y=0,width=1151,height=60)
        
        title = Label(nav_Frame,text="STUDENT DASHBOARD",font=("Georgia",20,"bold"),fg="#ffffff",bg="#143b64")
        #title = Label(self.root, text="STUDENT DASHBOARD",bd = 10, font=("Georgia", 30))

        #title.pack(side=TOP,fill=X)
        title.grid(row=0,column=1)

        self.img=PIL.Image.open("image/profile4.jpg")
        self.resimg=self.img.resize((50,50),PIL.Image.ANTIALIAS)
        self.my=ImageTk.PhotoImage(self.resimg)
        label=Label(nav_Frame,image=self.my,bd=0)
        #label.place(x=10,y=10)
        label.grid(row=0,column=3,padx=(5,3))
        
        lblemail = Label(nav_Frame,text=self.email,font=("Georgia",11),fg="#ffffff",bg="#143b64")#,height=1,width=15,borderwidth=2, relief="solid")
        lblemail.grid(row = 0,column=4,sticky="nsew")#,pady=5,padx=5)
        #lblemail = Label(nav_Frame,text=self.email,font=("Georgia",12),bg="#ffffff")#,height=1,width=15,borderwidth=2, relief="solid")
        #lblemail.grid(row = 2,column=3)#,pady=5,padx=5)

        self.limg=PIL.Image.open("image/logout3.png")
        self.lresimg=self.limg.resize((140,30),PIL.Image.ANTIALIAS)
        self.lmy=ImageTk.PhotoImage(self.lresimg)
        btn_logout=Button(nav_Frame,image=self.lmy, bd=0,cursor="hand2",command=self.logout,bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_logout.grid(row=0,column=2,padx=(350,5),sticky="nsew")

        

        #Variables
        self.email_id = txt
        self.name = StringVar()
        self.testDate = StringVar()
        self.startTime = StringVar()
        self.endTime=StringVar()
        self.subject = StringVar()
        self.URL = StringVar()
        self.TestID = StringVar()
       

        

        self.search_combo = StringVar()
        self.search_field = StringVar()

        
        #DashBoard Frame
        Dash_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="#143b64")
        Dash_Frame.place(x=0,y=60,width=198,height=635)

        self.test=PIL.Image.open("image/tes.png")
        self.retest=self.test.resize((180,30),PIL.Image.ANTIALIAS)
        self.ftest=ImageTk.PhotoImage(self.retest)
        btn_test=Button(Dash_Frame,image=self.ftest,command= partial(self.test_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_test.grid(row=0,column=0,padx=(0,30),pady=(20,10))

        #Test_btn = Button(Dash_Frame,bg="#8B0000",text="Test",fg="#F0EDEE", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3).grid(row=0,column=0,padx=2,pady=0,sticky="w")

        self.profile=PIL.Image.open("image/profile.png")
        self.reprofile=self.profile.resize((180,30),PIL.Image.ANTIALIAS)
        self.fprofile=ImageTk.PhotoImage(self.reprofile)
        btn_profile=Button(Dash_Frame,image=self.fprofile,command= partial(self.student_profile_btn,self.email), bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_profile.grid(row=1,column=0,padx=(0,30),pady=(0,10))
        
        #student_profile_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Profile", font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,borderwidth = 3,command= partial(self.student_profile_btn,self.email)).grid(row=1,column=0,padx=2,pady=2,sticky="w")


        self.stat=PIL.Image.open("image/stat.png")
        self.restat=self.stat.resize((180,30),PIL.Image.ANTIALIAS)
        self.fstat=ImageTk.PhotoImage(self.restat)
        btn_stat=Button(Dash_Frame,image=self.fstat, bd=0,cursor="hand2",bg="#143b64",activebackground="#143b64")#.place(x=230,y=320)
        btn_stat.grid(row=2,column=0,padx=(0,30),pady=(0,10))
        
        # manage_employee_btn = Button(Dash_Frame,bg="#8B0000",fg="#F0EDEE",text="Employee",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.employee_btn).grid(row=1,column=0,padx=2,pady=2,sticky="w")

        # department_btn = Button(Dash_Frame,text="Department",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.dept_btn).grid(row=2,column=0,padx=2,pady=2,sticky="w")

        # password_btn = Button(Dash_Frame,text="Password",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.pass_btn).grid(row=3,column=0,padx=2,pady=2,sticky="w")

        # exit_btn = Button(Dash_Frame,text="Exit",bg="#8B0000",fg="#F0EDEE",
        # font=("Arial",9,"bold"),relief=RAISED,width=11,pady=20,command=self.logout).grid(row=4,column=0,padx=2,pady=2,sticky="w")

                           

        #Manage Frame

        Manage_Frame = LabelFrame(self.root,text="STUDENTS STATS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Manage_Frame.place(x=199,y=60,width=580,height=635)
    
        #Table Frame

        Table_Frame1 = Frame(Manage_Frame,bg="#0A090C")
        Table_Frame1.place(x=10,y=10,width=550,height=595)

        

        X_scroll = Scrollbar(Table_Frame1,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame1,orient=VERTICAL)
        self.Table1 = ttk.Treeview(Table_Frame1,columns=("Words Spoken","Multiple persons","Cell Phone","No Person", "Study Material"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table1.xview)
        Y_scroll.config(command=self.Table1.yview)

        # self.Table1.heading("Email",text="Email")
        self.Table1.heading("Words Spoken",text="Words Spoken")
        # self.Table.heading("Test URL",text="Test URL")
        self.Table1.heading("Multiple persons",text="Multiple persons")
        self.Table1.heading("Cell Phone",text="Cell Phone")
        self.Table1.heading("No Person",text="No Person")
        self.Table1.heading("Study Material",text="Study Material")



        

        self.Table1['show']="headings"
        #self.Table1.column("Email",width=100)
        self.Table1.column("Words Spoken",width=100)
        # self.Table.column("Test URL",width=150)
        self.Table1.column("Multiple persons",width=100)
        self.Table1.column("Cell Phone",width=100)
        self.Table1.column("No Person",width=100)
        self.Table1.column("Study Material", width=100)
        
        

        

        self.Table1.pack(fill=BOTH,expand=1)
        #self.Table1.bind('<ButtonRelease 1>',self.get_fields)

        

        #Button Frame
        #btn_frame = Frame(Manage_Frame,bg="#F0EDEE")
        #btn_frame.place(x=12,y=520,width=410) 

        

        #add_btn = Button(btn_frame,text="Add",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.add_student).grid(row=0,column=0,padx=5,pady=10)

        #update_btn = Button(btn_frame,text="Update",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.update).grid(row=0,column=1,padx=5,pady=10)

        #delete_btn = Button(btn_frame,text="Delete",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.delete).grid(row=0,column=2,padx=5,pady=10)

        #clear_btn = Button(btn_frame,text="Clear",width=10,bg="#8B0000",fg="#FFFCF9", font=("Arial",10,"bold"),command=self.clear_field).grid(row=0,column=3,padx=5,pady=10)

        

        

        #Detail Frame
        Detail_Frame = LabelFrame(self.root,text="TEST DETAILS",font=("Georgia",14,"bold"),bd=4,relief=RIDGE,bg="#FFFCF9")
        Detail_Frame.place(x=780,y=60,width=570,height=635)

        

        # lbl_search = Label(Detail_Frame,text="Search-",bg="#FFFCF9",fg="#0A090C",
        # font=("Arial",18,"bold"))
        # lbl_search.grid(row = 0,column=0,pady=10,padx=15,sticky="w")

        

        # search_box = ttk.Combobox(Detail_Frame,width=12,textvariable=self.search_combo,
        # font=("Arial",13,"bold"),state="readonly")

        # search_box['values'] = ("Roll_No","SName","Contact_No")
        # search_box.grid(row=0,column=1,pady=10,padx=10,ipady=4,sticky="w")

        

        

        # txt_search = Entry(Detail_Frame,width=20,textvariable=self.search_field,
        # font=("Arial",10,"bold"),bd=5,relief=RAISED)
        # txt_search.grid(row = 0,column=2,pady=10,padx=20,ipady=4,sticky="w")

        

        # search_btn = Button(Detail_Frame,text="Search",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.search_data).grid(row=0,column=5,padx=10,pady=10)

        # show_all_btn = Button(Detail_Frame,text="Show All",bg="#8B0000",fg="#FFFCF9",
        # font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,command=self.show_data).grid(row=0,column=6,padx=10,pady=10)

        #logout_btn = Button(Detail_Frame,text="Log Out",bg="#8B0000",fg="#FFFCF9",
        #font=("Arial",10,"bold"),relief=RAISED,width=10,pady=5,borderwidth = 3,command=self.logout).grid(row=0,column=7,padx=10,pady=10)

        

        #Table Frame

        Table_Frame = Frame(Detail_Frame,bg="#0A090C")
        Table_Frame.place(x=10,y=10,width=540,height=595)

        

        X_scroll = Scrollbar(Table_Frame,orient=HORIZONTAL)
        Y_scroll = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Table = ttk.Treeview(Table_Frame,columns=("Test-Name","Subject","Test Date"),xscrollcommand=X_scroll.set,yscrollcommand=Y_scroll.set)

        X_scroll.pack(side=BOTTOM,fill=X)
        Y_scroll.pack(side=RIGHT,fill=Y)
        X_scroll.config(command=self.Table.xview)
        Y_scroll.config(command=self.Table.yview)

        #self.Table.heading("Test-ID",text="Test-ID")
        self.Table.heading("Test-Name",text="Test-Name")
        # self.Table.heading("Test URL",text="Test URL")
        self.Table.heading("Subject",text="Subject")
        self.Table.heading("Test Date",text="Test Date")
        #self.Table.heading("Start Time",text="Start Time")



        

        self.Table['show']="headings"
        #self.Table.column("Test-ID",width=100)
        self.Table.column("Test-Name",width=100)
        # self.Table.column("Test URL",width=150)
        self.Table.column("Subject",width=100)
        self.Table.column("Test Date",width=100)
        #self.Table.column("Start Time",width=100)
        
        

        

        self.Table.pack(fill=BOTH,expand=1)
        self.Table.bind('<ButtonRelease 1>',self.get_fields)
        # self.txt_Date.bind("<FocusIn>", self.foc_in)
        # self.txt_Date.bind("<FocusOut>", self.foc_out)


        # self.put_placeholder()
        self.show_data()

        

    # def add_student(self):

    #     if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "":

    #         messagebox.showerror("Error","All Fields are Required")

    #     else:
    #         connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
    #         curr = connect.cursor()

    #         self.TestID = random.randint(3,1000)

    #         curr.execute("INSERT INTO TEST_DETAILS VALUES(%s,%s,%s,%s,%s,%s,%s)",
    #         (self.TestID, self.name.get(), self.URL.get(), self.testDate.get(), self.txt_StartTime.get(),self.txt_EndTime.get(),self.subject.get()))

    #         connect.commit()

    #         self.show_data()
    #         self.clear_field()
    #         connect.close()

    #         messagebox.showinfo("Succes","Record Successfully Added")

        

    def show_data(self):

        connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
        curr = connect.cursor()

        

        curr.execute("SELECT TEST_ID, TEST_NAME, SUBJECT, TEST_URL, TEST_DATE, START_TIME, END_TIME from TEST_DETAILS")
        rows = curr.fetchall()

        if(len(rows)!=0):

            self.Table.delete(*self.Table.get_children())
            for row in rows:

                self.Table.insert('',END,values=(row[1],row[2],row[4],row[5]))

            connect.commit()
        connect.close()

        

    # def clear_field(self):

    #     if self.subject.get() == "" or self.name.get() == "" or self.URL.get() == "" or self.testDate.get()== "" or self.startTime.get() == "" or self.endTime.get() == "":

    #         messagebox.showerror("Error","All Fields are Required")

    #     else:

    #         self.subject.set("")
    #         self.name.set("")
    #         self.URL.set("")
    #         self.testDate.set("")
    #         self.startTime.set("")
    #         self.endTime.set("")

        

    def get_fields(self,event):

        cursor_row = self.Table.focus()
        if cursor_row!="":
            content = self.Table.item(cursor_row)
            row = content['values']
            #self.TestID.set(row[0])
            connect = pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
            curr = connect.cursor()
            curr.execute("SELECT TEST_ID FROM TEST_DETAILS WHERE TEST_NAME=%s AND SUBJECT=%s",(row[0],row[1]))
            row1 = curr.fetchone()
            #print(row[0])
            curr.execute("SELECT WORDS_SPOKEN, MULTIPLE_PERSON_DETECTION, MOBILE_PHONE_DETECTION,NO_PERSON_DETECTION,STUDY_MATERIAL_DETECTION FROM ONLINE WHERE TEST_ID=%s AND EMAIL=%s",(row1[0],self.email_id))
            row2 = curr.fetchone()
            self.Table1.delete(*self.Table1.get_children())
            if row2 != None:
                self.Table1.insert('',END,values=row2)
            else:
                messagebox.showerror("Error","You have not attemped this exam yet.")
                

            connect.commit()
            connect.close()

            #self.name.set(row[0])
            #self.URL.set(row[2])
            #self.testDate.set(row[3])
            #self.startTime.set(row[4])
            #elf.subject.set(row[1])



        

    # def search_data(self):

    #     if self.search_combo.get() == "" or self.search_field.get() == "":

    #         messagebox.showerror("Error","Some Fields might be Empty")

    #     else:

    #         connect = pymysql.connect("localhost","root","","ai_proctor")
    #         curr = connect.cursor()

            

    #         curr.execute("SELECT * from student where "+str(self.search_combo.get())+
    #                      " LIKE '%"+str(self.search_field.get())+"%'")

    #         rows = curr.fetchall()

    #         if(len(rows)!=0):

    #             self.Table.delete(*self.Table.get_children())

    #             for row in rows:

    #                 self.Table.insert('',END,values=row)

    #             connect.commit()
    #         connect.close()

            

    # def put_placeholder(self):

    #     self.txt_Date.insert(0,"DD-MM-YYYY")
    #     self.txt_Date['fg'] = "grey"

    #     self.txt_StartTime.insert(0,"HH-MM")
    #     self.txt_StartTime['fg'] = "grey"


    # def foc_in(self,event):

    #     if self.txt_Date['fg'] == "grey":

    #         self.txt_Date.delete('0', 'end')
    #         self['fg'] = "grey"


    # def foc_out(self, event):

    #     if not self.get():
    #         self.txt_Date.put_placeholder()

    #     if not self.get():
    #         self.txt_StartTime.put_placeholder()

            

    def logout(self):

        self.root.destroy() 
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()        

    def test_btn(self,email):
        self.root.destroy()
        st_root = Tk()
        st = Student(st_root,email)
        st_root.mainloop()

    def student_profile_btn(self,email):
        self.root.destroy()
        st_root = Tk()
        st = Student_Profile(st_root,email)
        st_root.mainloop()

##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################
##############################################################################################################################################################################################################################################################################

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#f0f0f0")
        self.root.resizable(0, 0)


        #===BG Image===(1)
        #self.bg=ImageTk.PhotoImage(file="image/wallpaper_white_1.jpg")
        #bg=Label(self.root,image=self.bg, borderwidth=0, highlightthickness=0).place(x=0,y=80)


        #===BG Image===(2)
        #self.bg=ImageTk.PhotoImage(file="image/wallpaper_white_2.jpg")
        #bg=Label(self.root,image=self.bg, borderwidth=0, highlightthickness=0).place(x=0,y=100)

        #===BG Image===(3)
        self.bg=ImageTk.PhotoImage(file="image/wallpaper_white_3(1).png")
        bg=Label(self.root,image=self.bg, borderwidth=0, highlightthickness=0).place(x=0,y=150)

        #===BG Image===(4)
        #self.bg=ImageTk.PhotoImage(file="image/wallpaper_white_4.jpg")
        #bg=Label(self.root,image=self.bg, borderwidth=0, highlightthickness=0).place(x=0,y=100)

       
                
        #===Left Image===
        #self.left=ImageTk.PhotoImage(file="image/side1.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=250,width=280,height=180)

        #====Register Frame===
        login_frame=Frame(self.root,bg="#f0f0f0")
        login_frame.place(x=650,y=100,width=700,height=700)
        #a13248 neon green color
        heading=Label(login_frame,text="AI Based Proctoring System",font=("times new roman",30,"bold"),bg="#f0f0f0",fg="#a13248").place(x=50, y=10) 
        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",20,"bold"),bg="#f0f0f0",fg="black").place(x=200,y=90)

        email=Label(login_frame,text="Email",font=("times new roman",15,"bold"),bg="#f0f0f0",fg="black").place(x=200,y=130)
        self.txt_email=Entry(login_frame,font=("times new roman",15),bg="#f0f0f0", fg="black", insertbackground='black')
        self.txt_email.place(x=200,y=160,width=250)
        
        password=Label(login_frame,text="Password",font=("times new roman",15,"bold"),bg="#f0f0f0",fg="black").place(x=200,y=210)
        self.txt_password=Entry(login_frame,font=("times new roman",15),bg="#f0f0f0", fg="black", insertbackground='black', show="*")
        self.txt_password.place(x=200,y=240,width=250)

        self.btn_img=ImageTk.PhotoImage(file="image/login1.jpg")
        self.btn_register_img=ImageTk.PhotoImage(file="image/register1.jpg")
        btn_login=Button(login_frame,image=self.btn_img, bd=0,cursor="hand2",command=self.login).place(x=230,y=320)
        
        signup = Label(login_frame,text="Don't have an account?",font=("times new roman",16),bg="#f0f0f0",fg="black").place(x=230,y=400)
        btn_signup=Button(login_frame,image=self.btn_register_img, bd=0,cursor="hand2", command=self.signup).place(x=230,y=440)


        self.secure=PIL.Image.open("image/secure.png")
        self.resecure=self.secure.resize((350,70),PIL.Image.ANTIALIAS)
        self.tksecure=ImageTk.PhotoImage(self.resecure)
        secure_label=Label(image=self.tksecure, bg="#f0f0f0",fg="white").place(x=20,y=600)
        #secure_label=Label(image=self.tksecure, bg="black",fg="black").place(x=980,y=20) top right
        
    
        

    def clear(self):
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)
        
        
    def login(self):
        if self.txt_email.get()=="" or self.txt_password.get()=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                cur=con.cursor()
                cur.execute("select * from users where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone()
                if row==None:
                     messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                else:
                    #print(row[6])
                    if row[7] == 0:
                        messagebox.showerror("Error","Your account has not yet been verified. Please try again later.",parent=self.root)
                    elif row[8] == 1:
                        messagebox.showerror("Error","Your account been blocked. Please contact the admin if this is a mistake.",parent=self.root)
                    else:
                        self.email = self.txt_email.get()
                        if row[5] == 'student':
                            self.root.destroy()
                            st_root = Tk()
                            st = Student(st_root,self.email)
                            st_root.mainloop()
                        else:
                            self.root.destroy()
                            st_root = Tk()
                            st = Faculty(st_root,self.email)
                            st_root.mainloop()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)

    def signup(self):
        self.root.destroy()
        st_root = Tk()
        st = Register(st_root)
        st_root.mainloop()


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1500x700+0+0")
        self.root.config(bg="#f1f6f2")
        self.root.resizable(0, 0) 


        #===Variable for Display Image
        self.display_image = ""

        #===BG Image===
        #self.bg=ImageTk.PhotoImage(file="image/b6.jpg")
        #bg=Label(self.root,image=self.bg).place(x=0,y=0,relheight=1)

        #===BG Image===(3)
        #self.bg=ImageTk.PhotoImage(file="image/reg_pic.jpg")
        self.bg=PIL.Image.open("image/reg_pic.jpg")
        self.re_reg=self.bg.resize((400,400),PIL.Image.ANTIALIAS)
        self.tk_re=ImageTk.PhotoImage(self.re_reg)
        bg=Label(self.root,image=self.tk_re, borderwidth=0, highlightthickness=0).place(x=70,y=100)
                
        #===Left Image===
        #self.left=ImageTk.PhotoImage(file="image/side1.jpg")
        #left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #===Left Image===
        #self.logo=ImageTk.PhotoImage(file="image/logo.jpg")
        #self.logo= self.logo.resize((250, 250), Image.ANTIALIAS)
        #logo=self.logo.resize((20,20), resample=0)
        #logo=Label(self.root,image=self.logo).place(x=200,y=200,width=100,height=100)

        #===Register Frame===
        frame1=Frame(self.root,bg="#f1f6f2")
        frame1.place(x=650,y=100,width=700,height=500)

        #a13248 maroon 

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="#f1f6f2",fg="black").place(x=50,y=30)

        #===row1===
        f_name=Label(frame1,text="Full Name",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="#f1f6f2", fg="black", insertbackground='black')
        self.txt_fname.place(x=50,y=130,width=250)

        
        Photo_ID=Label(frame1,text="Photo ID",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=370,y=100)
        button_explore = Button(frame1,text = "Browse Files",command = self.browseFiles).place(x=370,y=130,width=200)
        
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="#f1f6f2", fg="black", insertbackground='black')
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="#f1f6f2", fg="black", insertbackground='black')
        self.txt_email.place(x=370,y=200,width=250)
        
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=50,y=240)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="#f1f6f2", fg="black", insertbackground='black', show="*")
        self.txt_password.place(x=50,y=270,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="#f1f6f2",fg="black").place(x=370,y=240)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="#f1f6f2", fg="black", insertbackground='black', show="*")
        self.txt_cpassword.place(x=370,y=270,width=250)
        
        self.btn_img=ImageTk.PhotoImage(file="image/register1.jpg")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=340)
        signin = Label(frame1,text="Already have an account?",font=("times new roman",16),bg="#f1f6f2",fg="black").place(x=50,y=400)
        self.btn_img1=ImageTk.PhotoImage(file="image/login1.jpg")
        btn_login=Button(frame1,image=self.btn_img1,font=("times new roman",20),bg="#f1f6f2",fg="black",bd=0,cursor="hand2", command=self.login).place(x=50,y=450,width=180)

        self.secure=PIL.Image.open("image/secure.png")
        self.resecure=self.secure.resize((350,70),PIL.Image.ANTIALIAS)
        self.tksecure=ImageTk.PhotoImage(self.resecure)
        secure_label=Label(image=self.tksecure, bg="#f1f6f2",fg="white").place(x=20,y=600)
        #secure_label=Label(image=self.tksecure, bg="black",fg="black").place(x=980,y=20) top right

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Image files",
                                                        "*.jpeg*"),
                                                       ("all files",
                                                        "*.*")))
        with open(self.filename, "rb") as file1:
            self.display_image = file1.read()
            if self.display_image == "":
                messagebox.showinfo("Error","Please select an appropriate image",parent=self.root)
            else:
                messagebox.showinfo("Success","Image has been selected successfully",parent=self.root)
            
            #print(self.data)

    def login(self):
        self.root.destroy()
        st_root = Tk()
        st = Login_window(st_root)
        st_root.mainloop()
        

    def clear(self):
        #self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.txt_fname.delete(0,END)


    def register_data(self):
        pwd_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$" 
        pat = re.compile(pwd_regex)
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        print(re.search(pat, self.txt_password.get()))
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.display_image=="":
                messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif ((re.compile("^[0-9]{10}$")).match(self.txt_contact.get()))==None:
                messagebox.showerror("Error","Please enter valid contact no.",parent=self.root)
        elif (re.search(email_regex,self.txt_email.get()))==None:
                messagebox.showerror("Error","Please enter valid Email Address",parent=self.root)
        elif re.search(pat, self.txt_password.get())==None:
                messagebox.showerror("Error","Password \n1.must contain at least one number.\n2.must contain at least one uppercase and one lowercase character.\n3.must contain at least one special symbol.\n4.Should be between 6 to 20 characters long.",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
                messagebox.showerror("Error","Passoword and confirm passowrd should be same",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                cur=con.cursor()
                cur.execute("select * from users where email=%s",self.txt_email.get())
                row=cur.fetchone()
                con.commit()
                con.close()
                if row!=None:
                     messagebox.showerror("Error","User Already Exist",parent=self.root)
                else:
                    conn=pymysql.connect(host="localhost",user="root",password="",database="ai_proctor")
                    curr=conn.cursor()
                    curr.execute("INSERT INTO `users`(`Full Name`, `contact`, `email`, `password`, `Role`,`display_picture`, `verified`, `blocked` ) VALUES (%s, %s, %s, %s, 'student', %s, %s, %s)",(self.txt_fname.get(),self.txt_contact.get(),self.txt_email.get(),self.txt_password.get(), self.display_image, 0, 0))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Registered Successfully",parent=self.root)
                    self.clear()
                    
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)      
    

        
        



root=Tk()
root.resizable(True, True)
obj=Login_window(root)
root.mainloop()
