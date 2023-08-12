from tkinter import*
from PIL import Image,ImageTk
import tkinter.messagebox
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import tkinter as tk
import time
from datetime import date
class DailyAttendanceRecord:
    def __init__(self,window):
        self.window=window
        self.window.title("DailyAttendanceRecord")
        self.window.geometry("1280x725+0+0")

        #variable Declaraion
        self.yfield=StringVar()
        self.mfield=StringVar()
        self.dfield=StringVar()
        self.yfield1=StringVar()
        self.mfield1=StringVar()
        self.dfield1=StringVar()
        self.rollfieldS=StringVar()
        self.rollfieldD=StringVar()

        self.mainframe=Frame(window,bg="grey",width=1285,height=725,bd=5,relief=GROOVE)
        self.mainframe.place(x=0,y=44)

        headinglabel=Label(window,text="Daily Attendance Record's",fg="yellow",bg="black",width=67,font=("cooper black",20,"bold"),bd=5,relief=GROOVE)
        headinglabel.place(x=0,y=0)

        recordframe=Frame(self.mainframe,width=740,height=500,bg="black",bd=2,relief=SUNKEN)
        recordframe.place(x=265,y=60)

        searchRecLabel=Label(self.mainframe,text="Search Record's",font=("Cooper Black",18,"bold"),bd=2,relief=GROOVE,bg="grey")
        searchRecLabel.place(x=20,y=20)

        DeleteRecLabel=Label(self.mainframe,text="Delete Record's",font=("Cooper Black",18,"bold"),bd=2,relief=GROOVE,bg="grey")
        DeleteRecLabel.place(x=1045,y=20)

        Datedeletelabel=Label(self.mainframe,text="Please Enter Date Which\n You Want to Delete the Record.",font=("Bodoni MT",14,"bold"),bg="#8f8384")
        Datedeletelabel.place(x=1010,y=80)

        DateSearchlabel=Label(self.mainframe,text="Please Enter Date Which\n You Want to Search the Record.",font=("Bodoni MT",14,"bold"),bg="#8f8384")
        DateSearchlabel.place(x=2,y=80)

        DateEntryFrameS=Frame(self.mainframe,bg="#78807a",bd=2,relief=GROOVE,width=200,height=50)
        DateEntryFrameS.place(x=30,y=160)

        DateEntryFrameD=Frame(self.mainframe,bg="#78807a",bd=2,relief=GROOVE,width=200,height=50)
        DateEntryFrameD.place(x=1040,y=160)

        Rolldeletelabel=Label(self.mainframe,text="Please Enter Roll Number Which\n You Want to Delete the Record.",font=("Bodoni MT",14,"bold"),bg="#8f8384")
        Rolldeletelabel.place(x=1010,y=280)

        DateSearchlabel=Label(self.mainframe,text="Please Enter Roll Number Which\n You Want to Search the Record.",font=("Bodoni MT",14,"bold"),bg="#8f8384")
        DateSearchlabel.place(x=2,y=280)

        RollEntryFrameS=Frame(self.mainframe,bg="#78807a",bd=2,relief=GROOVE,width=100,height=50)
        RollEntryFrameS.place(x=80,y=380)

        RollEntryFrameD=Frame(self.mainframe,bg="#78807a",bd=2,relief=GROOVE,width=100,height=50)
        RollEntryFrameD.place(x=1090,y=380)

        #search button
        imgbtn=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\searchEntry.png")
        imgbtn=imgbtn.resize((185,75))
        self.photoimg=ImageTk.PhotoImage(imgbtn)
        searchButton=Button(self.mainframe,image=self.photoimg,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.Search)
        searchButton.place(x=30,y=500,width=200,height=70)

        #Delete button
        imgbtn1=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\deleteEntry.png")
        imgbtn1=imgbtn1.resize((200,130))
        self.photoimg1=ImageTk.PhotoImage(imgbtn1)
        deleteButton=Button(self.mainframe,image=self.photoimg1,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.Delete)
        deleteButton.place(x=1050,y=500,width=200,height=120)


        #refresh button
        imgbtn2=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refbtn.png")
        imgbtn2=imgbtn2.resize((250,150))
        self.photoimg2=ImageTk.PhotoImage(imgbtn2)
        RefButton=Button(self.mainframe,image=self.photoimg2,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.Refresh)
        RefButton.place(x=540,y=580,width=180,height=80)

        RecordsTotl=Label(self.mainframe,text="Total Record's:-",font=("Cooper Black",18,"bold"),bg="#756464")
        RecordsTotl.place(x=5,y=610)
        

        #date entry field for Search
        Slabel=Label(self.mainframe,text="Y  Y  Y  Y    --    M  M    --    D  D",font=("Cooper Black",10),bg="grey",fg="#2e2929")
        Slabel.place(x=40,y=139)
        
        Yfield=Entry(DateEntryFrameS,width=4,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.yfield)
        Yfield.place(x=5,y=5)

        dashlabel=Label(DateEntryFrameS,text="-",font=("arial",20,"bold"),bg="#78807a")
        dashlabel.place(x=74,y=5)

        Mfield=Entry(DateEntryFrameS,width=2,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.mfield)
        Mfield.place(x=95,y=5)
        

        dashlabel1=Label(DateEntryFrameS,text="-",font=("arial",20,"bold"),bg="#78807a")
        dashlabel1.place(x=135,y=5)

        Dfield=Entry(DateEntryFrameS,width=2,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.dfield)
        Dfield.place(x=155,y=5)

        #date entry field for Delete
        Dlabel=Label(self.mainframe,text="Y  Y  Y  Y    --    M  M    --    D  D",font=("Cooper Black",10),bg="grey",fg="#2e2929")
        Dlabel.place(x=1045,y=139)
        
        Yfield1=Entry(DateEntryFrameD,width=4,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.yfield1)
        Yfield1.place(x=5,y=5)

        dashlabel1=Label(DateEntryFrameD,text="-",font=("arial",20,"bold"),bg="#78807a")
        dashlabel1.place(x=74,y=5)

        Mfield1=Entry(DateEntryFrameD,width=2,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.mfield1)
        Mfield1.place(x=95,y=5)

        dashlabel12=Label(DateEntryFrameD,text="-",font=("arial",20,"bold"),bg="#78807a")
        dashlabel12.place(x=135,y=5)

        Dfield1=Entry(DateEntryFrameD,width=2,font=("arial",20,"bold"),bg="#a6a1a1",justify=CENTER,textvariable=self.dfield1)
        Dfield1.place(x=155,y=5)

        #Roll Number field for the Search
        RollFieldS=Entry(RollEntryFrameS,font=("arial",20,"bold"),width=5,bg="#a6a1a1",justify=CENTER,textvariable=self.rollfieldS)
        RollFieldS.place(x=8,y=5)

        #Roll Number field for the Delete
        RollFieldD=Entry(RollEntryFrameD,font=("arial",20,"bold"),width=5,bg="#a6a1a1",justify=CENTER,textvariable=self.rollfieldD)
        RollFieldD.place(x=8,y=5)

        #for resetingdata of variable imng
        resetSdate=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        resetSdate=resetSdate.resize((20,20))
        self.photoimgSD=ImageTk.PhotoImage(resetSdate)
        SDresetButton=Button(self.mainframe,image=self.photoimgSD,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.SDate)
        SDresetButton.place(x=200,y=215,width=20,height=20)

        resetSRoll=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        resetSRoll=resetSRoll.resize((20,20))
        self.photoimgSR=ImageTk.PhotoImage(resetSRoll)
        SRresetButton=Button(self.mainframe,image=self.photoimgSR,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.SRoll)
        SRresetButton.place(x=150,y=435,width=20,height=20)

        resetDdate=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        resetDdate=resetDdate.resize((20,20))
        self.photoimgDD=ImageTk.PhotoImage(resetDdate)
        DDresetButton=Button(self.mainframe,image=self.photoimgDD,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.DDate)
        DDresetButton.place(x=1210,y=215,width=20,height=20)

        resetDRoll=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        resetDRoll=resetDRoll.resize((20,20))
        self.photoimgDR=ImageTk.PhotoImage(resetDRoll)
        DRresetButton=Button(self.mainframe,image=self.photoimgSR,bg="grey",bd=0,relief=RIDGE,activebackground="grey",command=self.DRoll)
        DRresetButton.place(x=1160,y=435,width=20,height=20)

        
        

        #calling Refresh
        self.Refresh()
        #Calling Total rec
        self.TotalRec()

    def TotalRec(self):
        #for fetching the number of rows
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        my_cursor.execute("select COUNT(*) from Attendance")
        for rowcount in my_cursor:
            print("totoal attendance :",rowcount[0])

        RecordTotallabel=Label(self.mainframe,text=rowcount[0],font=("Algerian",25,"bold"),bg="grey",fg="green")
        RecordTotallabel.place(x=220,y=605)


    def Refresh(self):
        self.SDate()
        self.DDate()
        self.SRoll()
        self.DRoll()
        #local time
        t=time.localtime()
        self.ct=time.strftime("%H:%M:%S",t)
        print("current time:",self.ct)
        
        #fetching the present date
        self.today=date.today()
        print("today date",self.today)
        self.today=str(self.today)
        print("type of",type(self.today))
        
        #sshowing the db table query data on screeen
        tree=ttk.Treeview(self.window)
        tree["columns"]=("sr_no.","name","roll","class","date","time")

        s=ttk.Style(self.window)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

        tree['show']='headings'

        tree.column("sr_no.",width=30,minwidth=70,anchor=tk.CENTER)
        tree.column("name",width=100,minwidth=70,anchor=tk.CENTER)
        tree.column("roll",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("class",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("date",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("time",width=70,minwidth=70,anchor=tk.CENTER)

        tree.heading("sr_no.",text="Sr_No.",anchor=tk.CENTER)
        tree.heading("name",text="Name",anchor=tk.CENTER)
        tree.heading("roll",text="Roll_No.",anchor=tk.CENTER)
        tree.heading("class",text="Class",anchor=tk.CENTER)
        tree.heading("date",text="Date",anchor=tk.CENTER)
        tree.heading("time",text="Time",anchor=tk.CENTER)
        
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select * from attendance order by Date DESC"
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        
        i=0
        for ro in my_cursor:
            tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1],ro[2],ro[3],ro[4]))
            i=i+1

        tree.place(x=275,y=113,width=730,height=490)


    def SDate(self):
        #print("the value of stringvavr",len(self.yfield.get()))
        self.yfield.set("")
        self.mfield.set("")
        self.dfield.set("")
        
        
    def SRoll(self):
        self.rollfieldS.set("")
    def DRoll(self):
        self.rollfieldD.set("")
    def DDate(self):
        self.yfield1.set("")
        self.mfield1.set("")
        self.dfield1.set("")


        
        

    def Search(self):
        global datelen,outdate,dates
        a=len(self.yfield.get())
        #print("type",type(self.yfield.get()))
        a1=type(self.yfield.get())
        a11=self.yfield.get()
        b=len(self.mfield.get())
        b1=type(self.dfield.get())
        b11=self.mfield.get()
        c=len(self.dfield.get())
        c1=type(self.dfield.get())
        c11=self.dfield.get()
        d=len(self.rollfieldS.get())
        d1=type(self.rollfieldS.get())
        d11=self.rollfieldS.get()

        #fetching the present date
        self.today=date.today()
        print("today date",self.today)

        if a==4 or b==2 or c==2:
            dates="{}-{}-{}".format(a11,b11,c11)
            print(dates)
            datelen=len(dates)
            print("len of date",datelen)

            #fetching the present date
            todays=self.today.strftime("%Y-%m-%d")
            print(todays)
            
        elif a>4 or b>2 or c>2:
            dates="{}-{}-{}".format(a11,b11,c11)
            print(dates)
            datelen=len(dates)
            print("len of date",datelen)
        else:
            datelen=0
            
        if (datelen!=0 and d!=0):
            print("i am form if")
            try:
                a11=int(a11)
                b11=int(b11)
                c11=int(c11)
                d11=int(d11)
                if a!=4 or b!=2 or c!=2:
                    print("Your have not  entered the date in corresct format")
                    messagebox.showinfo("WARNING!!!",f"Please Enter the Date In correct Format!!!",parent=self.window)
                    self.SDate()
                    self.SRoll()
                elif a11>2100 or b11>12 or c11>31:
                    print("You have not enterd the correct date")
                    messagebox.showinfo("WARNING!!!",f"Please Enter valid Date",parent=self.window)
                    self.SDate()
                    self.SRoll()
                elif d11>1000:
                    messagebox.showinfo("WARNING!!!",f"Enter Roll Number less then 1000",parent=self.window)
                    self.SRoll()
                else:
                    #sshowing the db table query data on screeen
                    tree=ttk.Treeview(self.window)
                    tree["columns"]=("sr_no.","name","roll","class","date","time")

                    s=ttk.Style(self.window)
                    s.theme_use("classic")
                    s.configure(".",font=("Helvetica",11,"bold"))
                    s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

                    tree['show']='headings'

                    tree.column("sr_no.",width=30,minwidth=70,anchor=tk.CENTER)
                    tree.column("name",width=100,minwidth=70,anchor=tk.CENTER)
                    tree.column("roll",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("class",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("date",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("time",width=70,minwidth=70,anchor=tk.CENTER)

                    tree.heading("sr_no.",text="Sr_No.",anchor=tk.CENTER)
                    tree.heading("name",text="Name",anchor=tk.CENTER)
                    tree.heading("roll",text="Roll_No.",anchor=tk.CENTER)
                    tree.heading("class",text="Class",anchor=tk.CENTER)
                    tree.heading("date",text="Date",anchor=tk.CENTER)
                    tree.heading("time",text="Time",anchor=tk.CENTER)
        
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select * from attendance Where Date='{}' AND Roll_No={}".format(dates,d11)
                    my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        
                    i=0
                    for ro in my_cursor:
                        tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1],ro[2],ro[3],ro[4]))
                        i=i+1

                    tree.place(x=275,y=113,width=730,height=490)
        
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.SDate()
                self.SRoll()
        elif datelen!=0:
            print("i am form elif")
            try:
                a11=int(a11)
                b11=int(b11)
                c11=int(c11)
                if a!=4 or b!=2 or c!=2:
                    print("Your have not  entered the date in corresct format")
                    messagebox.showinfo("WARNING!!!",f"Please Enter the Date In correct Format!!!",parent=self.window)
                    self.SDate()
                    #self.SRoll()
                elif a11>2100 or b11>12 or c11>31:
                    print("You have not enterd the correct date")
                    messagebox.showinfo("WARNING!!!",f"Please Enter valid Date",parent=self.window)
                    self.SDate()
                    #self.SRoll()
                else:
                    tree=ttk.Treeview(self.window)
                    tree["columns"]=("sr_no.","name","roll","class","date","time")

                    s=ttk.Style(self.window)
                    s.theme_use("classic")
                    s.configure(".",font=("Helvetica",11,"bold"))
                    s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

                    tree['show']='headings'

                    tree.column("sr_no.",width=30,minwidth=70,anchor=tk.CENTER)
                    tree.column("name",width=100,minwidth=70,anchor=tk.CENTER)
                    tree.column("roll",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("class",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("date",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("time",width=70,minwidth=70,anchor=tk.CENTER)

                    tree.heading("sr_no.",text="Sr_No.",anchor=tk.CENTER)
                    tree.heading("name",text="Name",anchor=tk.CENTER)
                    tree.heading("roll",text="Roll_No.",anchor=tk.CENTER)
                    tree.heading("class",text="Class",anchor=tk.CENTER)
                    tree.heading("date",text="Date",anchor=tk.CENTER)
                    tree.heading("time",text="Time",anchor=tk.CENTER)
        
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select * from attendance Where Date='{}'".format(dates)
                    my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
                    
                    i=0
                    for ro in my_cursor:
                        tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1],ro[2],ro[3],ro[4]))
                        i=i+1

                    tree.place(x=275,y=113,width=730,height=490)
                    
                    
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.SDate()
                self.SRoll()
        elif d!=0:
            print("i am form elif2")
            try:
                d11=int(d11)
                if d11>1000:
                    messagebox.showinfo("WARNING!!!",f"Enter Roll Number less then 1000",parent=self.window)
                    self.SRoll()
                else:
                    """conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select * from attendance Where Roll_No={}".format(d11)
                    my_cursor.execute(query)
                    for i in my_cursor:
                        print(i)"""
                    #sshowing the db table query data on screeen
                    tree=ttk.Treeview(self.window)
                    tree["columns"]=("sr_no.","name","roll","class","date","time")

                    s=ttk.Style(self.window)
                    s.theme_use("classic")
                    s.configure(".",font=("Helvetica",11,"bold"))
                    s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

                    tree['show']='headings'

                    tree.column("sr_no.",width=30,minwidth=70,anchor=tk.CENTER)
                    tree.column("name",width=100,minwidth=70,anchor=tk.CENTER)
                    tree.column("roll",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("class",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("date",width=70,minwidth=70,anchor=tk.CENTER)
                    tree.column("time",width=70,minwidth=70,anchor=tk.CENTER)

                    tree.heading("sr_no.",text="Sr_No.",anchor=tk.CENTER)
                    tree.heading("name",text="Name",anchor=tk.CENTER)
                    tree.heading("roll",text="Roll_No.",anchor=tk.CENTER)
                    tree.heading("class",text="Class",anchor=tk.CENTER)
                    tree.heading("date",text="Date",anchor=tk.CENTER)
                    tree.heading("time",text="Time",anchor=tk.CENTER)
        
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select * from attendance Where Roll_No={}".format(d11)
                    my_cursor.execute(query)#STOPPED HERE due to but need do some validatiobn work of search
        
                    i=0
                    for ro in my_cursor:
                        tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1],ro[2],ro[3],ro[4]))
                        i=i+1

                    tree.place(x=275,y=113,width=730,height=490)
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.SRoll()
        elif a>4 or b>2 or c>2:
            messagebox.showinfo("WARNING!!!",f"You have Entered Invalid Date...",parent=self.window)
            self.SDate()
            self.SRoll()
        else:
            messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number for Searching....",parent=self.window)
            
        
            




        
    def Delete(self):
        global datelen,outdate,dates
        a=len(self.yfield1.get())
        #print("type",type(self.yfield.get()))
        a1=type(self.yfield1.get())
        a11=self.yfield1.get()
        b=len(self.mfield1.get())
        b1=type(self.mfield1.get())
        b11=self.mfield1.get()
        c=len(self.dfield1.get())
        c1=type(self.dfield1.get())
        c11=self.dfield1.get()
        d=len(self.rollfieldD.get())
        d1=type(self.rollfieldD.get())
        d11=self.rollfieldD.get()

        #fetching the present date
        self.today=date.today()
        print("today date",self.today)

        if a==4 or b==2 or c==2:
            dates="{}-{}-{}".format(a11,b11,c11)
            print(dates)
            datelen=len(dates)
            print("len of date",datelen)

            #fetching the present date
            todays=self.today.strftime("%Y-%m-%d")
            print(todays)
            
        elif a>4 or b>2 or c>2:
            dates="{}-{}-{}".format(a11,b11,c11)
            print(dates)
            datelen=len(dates)
            print("len of date",datelen)
        else:
            datelen=0
            
        if (datelen!=0 and d!=0):
            print("i am form if")
            try:
                a11=int(a11)
                b11=int(b11)
                c11=int(c11)
                d11=int(d11)
                if a!=4 or b!=2 or c!=2:
                    print("Your have not  entered the date in corresct format")
                    messagebox.showinfo("WARNING!!!",f"Please Enter the Date In correct Format!!!",parent=self.window)
                    self.SDate()
                    self.SRoll()
                elif a11>2100 or b11>12 or c11>31:
                    print("You have not enterd the correct date")
                    messagebox.showinfo("WARNING!!!",f"Please Enter valid Date",parent=self.window)
                    self.DDate()
                    self.DRoll()
                elif d11>1000:
                    messagebox.showinfo("WARNING!!!",f"Enter Roll Number less then 1000",parent=self.window)
                    self.DRoll()
                else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select COUNT(*) from  attendance Where Date='{}' AND Roll_No={}".format(dates,d11)
                    my_cursor.execute(query)
                    for i in my_cursor:
                        print(i[0])
                    if i[0]==0:
                        print("i have no data")
                        messagebox.showinfo("WARNING!!!",f"You Have No Data to Delete at Date {dates} and Roll_No. {d11}",parent=self.window)
                        self.DDate()
                        self.DRoll()
                    else:
                        print("have something")
                        query="DELETE from attendance Where Date='{}' AND Roll_No={}".format(dates,d11)
                        if messagebox.askyesno("Confirm","Are you sure want to delete Roll_No. {} at Date {}".format(d11,dates),parent=self.window)==True:
                            my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
                            conn.commit()
                            messagebox.showinfo("WARNING!!!",f"Successfully Deleted ",parent=self.window)
                            self.DRoll()
                            self.DDate()
                            self.TotalRec()
                            self.Refresh()
                        else:
                            messagebox.showinfo("Warning!!!","Operation Denied...",parent=self.window)
                            self.DRoll()
                            self.DDate()
                            self.Refresh()
        
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.DDate()
                self.DRoll()
        elif datelen!=0:
            print("i am form elif")
            try:
                a11=int(a11)
                b11=int(b11)
                c11=int(c11)
                if a!=4 or b!=2 or c!=2:
                    print("Your have not  entered the date in corresct format")
                    messagebox.showinfo("WARNING!!!",f"Please Enter the Date In correct Format!!!",parent=self.window)
                    self.DDate()
                    #self.SRoll()
                elif a11>2100 or b11>12 or c11>31:
                    print("You have not enterd the correct date")
                    messagebox.showinfo("WARNING!!!",f"Please Enter valid Date",parent=self.window)
                    self.DDate()
                    #self.SRoll()
                else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select COUNT(*) from  attendance Where Date='{}'".format(dates)
                    my_cursor.execute(query)
                    for i in my_cursor:
                        print(i[0])
                    if i[0]==0:
                        print("i have no data")
                        messagebox.showinfo("WARNING!!!",f"You Have No Data to Delete at Date {dates} ...",parent=self.window)
                        self.DDate()
                        #self.DRoll()
                    else:
                        print("have something")
                        query="DELETE from attendance Where Date='{}' ".format(dates)
                        if messagebox.askyesno("Confirm","Are you sure want to delete All Data at Date {}".format(dates),parent=self.window)==True:
                            my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
                            conn.commit()
                            messagebox.showinfo("WARNING!!!",f"Successfully Deleted ",parent=self.window)
                            self.DRoll()
                            self.DDate()
                            self.TotalRec()
                            self.Refresh()
                        else:
                            messagebox.showinfo("Warning!!!","Operation Denied...",parent=self.window)
                            self.Refresh()
                    
                    
                    
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.DDate()
                self.DRoll()
        elif d!=0:
            print("i am form elif2")
            try:
                d11=int(d11)
                if d11>1000:
                    messagebox.showinfo("WARNING!!!",f"Enter Roll Number less then 1000",parent=self.window)
                    self.DRoll()
                else:
                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                    my_cursor=conn.cursor()
                    query="select COUNT(*) from  attendance Where Roll_No={}".format(d11)
                    my_cursor.execute(query)
                    for i in my_cursor:
                        print(i[0])
                    if i[0]==0:
                        print("i have no data")
                        messagebox.showinfo("WARNING!!!",f"You Have No Data to Delete at Roll_No. {d11}",parent=self.window)
                        #self.DDate()
                        self.DRoll()
                    else:
                        print("have something")
                        query="DELETE from attendance Where Roll_No={}".format(d11)
                        if messagebox.askyesno("Confirm","Are you sure want to delete All Data at Roll_No. {}".format(d11),parent=self.window)==True:
                            my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
                            conn.commit()
                            messagebox.showinfo("WARNING!!!",f"Successfully Deleted ",parent=self.window)
                            self.DRoll()
                            self.DDate()
                            self.TotalRec()
                            self.Refresh()
                        else:
                            messagebox.showinfo("Warning!!!","Operation Denied...",parent=self.window)
                            self.DRoll()
                            self.DDate()
                            self.Refresh()
        
            except:
                messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number in Numeric Format Only",parent=self.window)
                print("Please enter the date in numbric form")
                self.DRoll()
        elif a>4 or b>2 or c>2:
            messagebox.showinfo("WARNING!!!",f"You have Entered Invalid Date...",parent=self.window)
            self.DDate()
            self.DRoll()
        else:
            messagebox.showinfo("WARNING!!!",f"Please Enter Date And Roll number for Searching....",parent=self.window)


        

if __name__=="__main__":
    window=Tk()
    obj=DailyAttendanceRecord(window)
    window.mainloop()
