from tkinter import*
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import Tk,Toplevel,Button,Menu
import tkinter.messagebox
import cv2
import time
import mysql.connector
from datetime import date
#importing external file
from About import About
from DailyAttendanceRecord import DailyAttendanceRecord
from RegistedRecored import RegisteredRecord
from registrationWindow import Registration
from LoginRegistration import LoginRegistration
from help import Help


class Attendance:
    def __init__(self,window):
        self.window=window
        self.window.title("AttendancePage")
        self.window.geometry("1280x725+0+0")

        self.mainframe=Frame(self.window,height=725,width=1280,bd=5,bg="#a8a5a5",relief=GROOVE)
        self.mainframe.place(x=0,y=0)

        headlabel=Label(self.mainframe,text="Attendance Page",bg="black",fg="yellow",font=("ALGERIAN",27,"bold"),width=55,bd=2,relief=RIDGE)
        headlabel.place(x=0,y=0)
        
        cameraframe=Frame(self.mainframe,height=500,width=500,bg="green",bd=5,relief=RIDGE)
        cameraframe.place(x=40,y=100)

        #cameraframe photo
        camrep=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\CameraReplace.png.jpg")
        camrep=camrep.resize((490,490))
        self.photoimgcr=ImageTk.PhotoImage(camrep)
        Camreplabel=Label(cameraframe,image=self.photoimgcr,bg="#a8a5a5",bd=0,relief=RIDGE)
        Camreplabel.place(x=0,y=0,width=490,height=490)

        notelabel=Label(self.mainframe,text="Note:-Please Press the Camera Button to Scan the QrCode For Attendance.",font=("arial black",9,"bold"),bg="#a8a5a5",fg="brown")
        notelabel.place(x=44,y=75,width=498)

        #camra on off button
        imgbtn=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\cameraButton.png")
        imgbtn=imgbtn.resize((185,75))
        self.photoimg=ImageTk.PhotoImage(imgbtn)
        cameraButton=Button(self.mainframe,image=self.photoimg,bg="#a8a5a5",bd=0,relief=RIDGE,activebackground="#a8a5a5",command=self.CameraButton)
        cameraButton.place(x=240,y=620,width=90,height=70)

        #logout image button
        logoutimg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\logoutButton.png")
        logoutimg=logoutimg.resize((220,95))
        self.photoimg1=ImageTk.PhotoImage(logoutimg)
        logoutButton=Button(self.mainframe,image=self.photoimg1,bg="#a8a5a5",bd=0,relief=RIDGE,activebackground="#a8a5a5",command=self.return_prev)
        logoutButton.place(x=1100,y=70,width=150,height=70)

        #admin image button
        adminimg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\adminImg.png")
        adminimg=adminimg.resize((220,120))
        self.photoimg2=ImageTk.PhotoImage(adminimg)
        AdminButton=Button(self.mainframe,image=self.photoimg2,bg="#a8a5a5",bd=0,relief=RIDGE,activebackground="#a8a5a5",command=self.login_reg)
        AdminButton.place(x=850,y=70,width=220,height=70)



        #menu image 
        menuimg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\menubutton.png")
        menuimg=menuimg.resize((130,55))
        self.photoimg3=ImageTk.PhotoImage(menuimg)


        menuButton=Menubutton(self.mainframe,image=self.photoimg3,relief=FLAT,bg="#a8a5a5",font=("ALGERIAN",33,"bold"),bd=0,activebackground="#a8a5a5")
        menuButton.grid()
        menuButton.menu=Menu(menuButton,tearoff=0,font=("Arial Black",15,"bold"),bg="grey",bd=5,relief=SUNKEN)
        menuButton["menu"]=menuButton.menu
        menuButton.menu.add_command(label="Registration",activebackground="black",activeforeground="white",command=self.reg_win)
        menuButton.menu.add_separator()
        menuButton.menu.add_command(label="RegisteredStudent",activebackground="black",activeforeground="white",command=self.Reg_rec)
        menuButton.menu.add_separator()
        menuButton.menu.add_command(label="DailyAttendanceRecord",activebackground="black",activeforeground="white",command=self.dailyAttendanceRecord)
        menuButton.menu.add_separator()
        menuButton.menu.add_command(label="AttendanceStastics",activebackground="black",activeforeground="white")
        menuButton.menu.add_separator()
        menuButton.menu.add_command(label="About",activebackground="black",activeforeground="white",command=self.About)
        menuButton.menu.add_separator()
        menuButton.menu.add_command(label="Help?..",activebackground="black",activeforeground="white",command=self.help)
        menuButton.place(x=690,y=80,height=55,width=130)


        #Today attendance& Today messsage Frame
        self.tatten_matten_frame=Frame(self.mainframe,height=300,width=555,bg="#e3d6d5",bd=5,highlightbackground="#3c3d36",highlightthickness=3,relief=RIDGE)
        self.tatten_matten_frame.place(x=690,y=300)

        label=Label(self.mainframe,text="<<<<<TodaysAttendance>>>>>",font=("Cooper Black",15,"bold"),fg="#23241e",bg="#a8a5a5")
        label.place(x=805,y=270)

        #ATTENMARK IMAGE ON TODAYATTEN FRAME
        AttenMarkImgOnFrame=Image.open(r"D:/Vicky_All_Program/python/AttendanceManagmentSystem/attenMark.png")
        AttenMarkImgOnFrame=AttenMarkImgOnFrame.resize((400,300))
        self.AttenMarkimg=ImageTk.PhotoImage(AttenMarkImgOnFrame)
        AttenMarkImgLabel=Label(self.tatten_matten_frame,image=self.AttenMarkimg,bg="#e3d6d5",bd=0,relief=RIDGE,activebackground="#a8a5a5")
        AttenMarkImgLabel.place(x=60,y=10,width=400,height=250)

        #TodayPresenty button
        imgbtnPresentyRef=Image.open(r"D:/Vicky_All_Program/python/AttendanceManagmentSystem/TodayPresentyRefreshbtn.png")
        imgbtnPresentyRef=imgbtnPresentyRef.resize((300,100))
        self.photoimgref=ImageTk.PhotoImage(imgbtnPresentyRef)
        PresentyRefBtn=Button(self.mainframe,image=self.photoimgref,bg="#a8a5a5",bd=0,relief=RIDGE,activebackground="#a8a5a5",command=self.TodayPresenty)
        PresentyRefBtn.place(x=840,y=620,width=250,height=70)
        

        #fetching the present date
        self.today=date.today()
        print("today date",self.today)
        self.today=str(self.today)
        print("type of",type(self.today))


        global varr,varr1
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        """my_cursor=conn.cursor()
        query="select COUNT(*) from attendance where Date = '{}'".format(self.today)
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        var=my_cursor.fetchall()
        varr=var[0][0]
        print("number of attendance in today",varr)"""
        my_cursor1=conn.cursor()
        my_cursor1.execute("select COUNT(*) from register")
        var1=my_cursor1.fetchall()
        varr1=var1[0][0]
        print("number of regsiter in ",varr1)

        #local time
        t=time.localtime()
        self.ct=time.strftime("%H:%M:%S",t)
        print(self.ct)

        #self.TodayPresenty()

    #function for updating the varr variable
    def todayAtten(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select COUNT(*) from attendance where Date = '{}'".format(self.today)
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        var=my_cursor.fetchall()
        varr=var[0][0]
        print("number of attendance in today",varr)


    def TodayPresenty(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select * from attendance where Date = '{}'".format(self.today)
        my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
        for t in my_cursor:
            print("todays present guys are:",t)
        #sshowing the db table query data on screeen
        tree=ttk.Treeview(self.window)
        tree["columns"]=("sr_no.","name","roll","class","date","time")

        s=ttk.Style(self.window)
        s.theme_use("classic")
        s.configure(".",font=("Helvetica",11,"bold"))
        s.configure("Treeview.Heading",foreground="black",font=("Helvetica",11,"bold"))

        tree['show']='headings'

        tree.column("sr_no.",width=70,minwidth=70,anchor=tk.CENTER)
        tree.column("name",width=70,minwidth=70,anchor=tk.CENTER)
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

        tree.place(x=700,y=310,width=545,height=290)
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor0=conn.cursor()
        query="select * from attendance where Date='{}'".format(self.today)
        my_cursor0.execute(query)

        i=0
        for ro in my_cursor0:
            tree.insert('',i+1,text="",values=(i+1,ro[0],ro[1],ro[2],ro[3],ro[4]))
            i=i+1

        tree.place(x=700,y=310,width=545,height=290)
        


    def CameraButton(self):
        #local time
        t=time.localtime()
        self.ct=time.strftime("%H:%M:%S",t)
        print(self.ct)

        #showing after off camera
        AlreadyQ=[]
        queue=[]
        
        camera_id = 0
        delay = 1
        window_name = 'OpenCV QR Code' 

        timeout = time.time() + 10 
        cap = cv2.VideoCapture(camera_id)#camera object created use to  capture through camrea
        qcd = cv2.QRCodeDetector()#only camera detect qr only
        while time.time() < timeout:
            #self.TodayPresenty()
            ret, frame = cap.read()#read the captured frame
            resize = cv2.resize(frame, (1275, 725))
            
            if ret:# a boolean variable that returns true if the frame is available
                ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(resize)#detectAndDecodeMulti() was added to detect and decode multiple QR codes at once.
                if ret_qr:
                    for s, p in zip(decoded_info, points):#The function takes in iterables as arguments and returns an iterator. This iterator generates a series of tuples containing elements from each iterable.
                        if s:
                            #for fetching the current attendacne  number before marking the presenty
                            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                            my_cursor=conn.cursor()
                            query="select COUNT(*) from attendance where Date = '{}'".format(self.today)
                            my_cursor.execute(query)#STOPPED HERE due to date is not passing properly
                            var=my_cursor.fetchall()
                            varr=var[0][0]
                            print("number of attendance in today",varr)
                            
                            print("This is s:",s)
                            print("This is p:",p)
                            print("This is ret_qr:",ret_qr)
                            s=int(s)
                            color = (255, 0, 0)#RGB
                            conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                            my_cursor=conn.cursor()
                            my_cursor.execute("select * from register")
                            mmm=my_cursor.fetchall()
                            tempua=0
                            for i in mmm:
                                print("This is i[1]:",i[1])
                                if i[1]==s:
                                    print("i am authorized you are regiseter user")
                                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                                    my_cursor0=conn.cursor()
                                    query="select * from attendance where Date='{}'".format(self.today)
                                    my_cursor0.execute(query)#STOPPED HERE
                                    print(type(varr))
                                    if varr==0:
                                        print("empty and attendance mark successful")
                                        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                                        my_cursor1=conn.cursor()
                                        my_cursor1.execute("insert into attendance values(%s,%s,%s,%s,%s)",(
                                                                                                               i[0],
                                                                                                               i[1],
                                                                                                               i[2],
                                                                                                               self.today,
                                                                                                               self.ct,                                                                                
                                                                                                            ))
                                        conn.commit()
                                        conn.close()#UPTO HERE DONE SuccessFully But need to stop scannig same qr mysql showing dublicate entry
                                        print("attendacne marked successful")
                                        que="<<<Roll_Number_{}_Attendance_Marked_SuccessFully>>>".format(i[1])
                                        queue.append(que)
                                        #tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
                                        break
                                        
                                    else:
                                        print("i am in else mean today have some attendacne")
                                        temp=0
                                        for ij in my_cursor0:
                                            print("check i am present or not",i)
                                            if ij[1]==s:
                                                print("YOur attendance already marked")
                                                Alq="<<<Roll_Number_{}_Already_Attendance_Marked>>>".format(ij[1])
                                                if Alq not in AlreadyQ:
                                                    AlreadyQ.append(Alq)
                                                break
                                            else:
                                                temp=temp+1
                                                if temp==varr:
                                                    print("my your attenacne marked success")
                                                    conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                                                    my_cursor1=conn.cursor()
                                                    my_cursor1.execute("insert into attendance values(%s,%s,%s,%s,%s)",(
                                                                                                                           i[0],
                                                                                                                           i[1],
                                                                                                                           i[2],
                                                                                                                           self.today,
                                                                                                                           self.ct,                                                                                
                                                                                                                        ))
                                                    conn.commit()
                                                    conn.close()#UPTO HERE DONE SuccessFully But need to stop scannig same qr mysql showing dublicate entry
                                                    #tkinter.messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
                                                    que="<<<Roll_Number_{}_Attendance_Marked_SuccessFully>>>".format(i[1])
                                                    queue.append(que)
                                                    break
                                                    
                                else:
                                    print("unauthorized you are not regiseter user")
                                    tempua=tempua+1
                                    if tempua==varr1:
                                        print("your are not a register user")
                                        NoRegWarn=Label(self.mainframe,text="Note:-Some Unauthorized Attendance Reported.",font=("Arial Black",15,"bold"),fg="red",bg="#a8a5a5")
                                        NoRegWarn.place(x=700,y=200)
                                    
                        else:
                            print("Vicky")
                            color = (0, 255, 0)
                        frame = cv2.polylines(resize, [p.astype(int)], True, color, 8)#a polyline is used to create open shapes as the last point doesn't have to be connected to the first point
                cv2.imshow(window_name, resize)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

            #printing queue element
            """#Today attendance& Today messsage Frame for removing(overwrite) the AttenMark image from frame
            self.tatten_matten_frame=Frame(self.mainframe,height=300,width=555,bg="#e3d6d5",bd=5,highlightbackground="#3c3d36",highlightthickness=3,relief=RIDGE)
            self.tatten_matten_frame.place(x=690,y=300)
            
            global b
            b=5
            for i in queue:
                a="<<< Roll number ''{}'' your attendance marked successfully. >>>".format(i)
                print(a)
                presentylabel=Label(self.tatten_matten_frame,text=a,font=("ARIAL",10,"bold"),bg="#e3d6d5")
                presentylabel.place(x=20,y=b)
                b=b+20

            #for printing the notice about already marked presenty
            z=b
            for j in AlreadyQ:
                al="<<< Roll number '{}' your attendance Already marked. >>>".format(j)
                print(al)
                Apresentylabel=Label(self.tatten_matten_frame,text=al,font=("ARIAL",10,"bold"),bg="#e3d6d5",fg="red")
                Apresentylabel.place(x=20,y=z)
                z=z+20"""
            global index
            tree=ttk.Treeview(self.window)
            tree["columns"]=("Today")
            s=ttk.Style(self.window)
            s.theme_use("classic")
            s.configure(".",font=("Helvetica",11,"bold"))
            s.configure("Treeview.Heading",foreground="green",font=("Cooper Black",11,"bold"))

            tree['show']='headings'

            tree.column("Today",width=170,minwidth=170,anchor=tk.CENTER)


            tree.heading("Today",text="Attendance Marked",anchor=tk.CENTER)
            
            index=0
            for ij in AlreadyQ:
                tree.insert('',index,text="",values=(ij))

            for ij in queue:
                tree.insert('',index,text="",values=(ij))

            tree.place(x=700,y=310,width=545,height=290)


        cv2.destroyWindow(window_name)

    #for importing external file
    def About(self):
        self.new_window=Toplevel(self.window)
        self.app=About(self.new_window)

    def dailyAttendanceRecord(self):
        self.new_window=Toplevel(self.window)
        self.app=DailyAttendanceRecord(self.new_window)

    def Reg_rec(self):
        self.new_window=Toplevel(self.window)
        self.app=RegisteredRecord(self.new_window)

    def reg_win(self):
        self.new_window=Toplevel(self.window)
        self.app=Registration(self.new_window)

    def login_reg(self):
        self.new_window=Toplevel(self.window)
        self.app=LoginRegistration(self.new_window)

    def help(self):
        self.new_window=Toplevel(self.window)
        self.app=Help(self.new_window)

    def return_prev(self):
        self.window.destroy()
        

        
        


if __name__=="__main__":
    window=Tk()
    obj=Attendance(window)
    window.mainloop()
