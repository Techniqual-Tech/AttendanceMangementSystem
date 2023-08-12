from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
#importing class from file 
from forgotpassword import forgot
from Attendance import Attendance

class Login:
    def __init__(self,window):
        self.window=window
        self.window.title("LoginPage")
        self.window.geometry("1275x725+0+0")

        #variable declaration
        self.usernamefield=StringVar()
        self.passwordfield=StringVar()

        mainframe=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\loginpage.jpg")
        mainframe=mainframe.resize((1275,725))
        self.photoimgcr=ImageTk.PhotoImage(mainframe)
        mainframe=Frame(self.window,bg="#a8a5a5",bd=0,relief=RIDGE)
        mainframe.place(x=0,y=0,width=1275,height=725)

        Imagelabel=Label(self.window,bg="#a8a5a5",image=self.photoimgcr,bd=0,relief=RIDGE)
        Imagelabel.place(x=0,y=0,width=1275,height=725)

        login=Label(self.window,bg="#132542",bd=5,relief=RIDGE)
        login.place(x=440,y=70,width=400,height=600)

        Logintitle=Label(login,text="Login Form",font=("Bodoni MT Black",20,"bold"),bg="#132542",fg="#0713f0")
        Logintitle.place(x=110,y=10)

        loginlogo=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Loginl.png")
        loginlogo=loginlogo.resize((80,80))
        self.photoimglogo=ImageTk.PhotoImage(loginlogo)
        Llogolabel=Label(login,bg="#132542",image=self.photoimglogo,bd=0,relief=RIDGE)
        Llogolabel.place(x=150,y=70,width=80,height=80)

        username=Label(login,text="Username",font=("Lucida Fax",15,"bold"),bg="#132542",fg="#2874ed")
        username.place(x=40,y=200)

        uEntry=Entry(login,font=("Lucida Fax",15,"bold"),textvariable=self.usernamefield)
        uEntry.place(x=45,y=235)

        Password=Label(login,text="Password",font=("Lucida Fax",15,"bold"),bg="#132542",fg="#2874ed")
        Password.place(x=40,y=270)

        pEntry=Entry(login,font=("Lucida Fax",15,"bold"),textvariable=self.passwordfield,show="*")
        pEntry.place(x=45,y=305)

        forgotbtn=Button(login,text="Forgot Password?",bg="#132542",bd=0,command=self.forgot_pass,font=("Lucida Fax",12,"italic"),fg="#2874ed",activebackground="#132542",activeforeground="#4e91fc")
        forgotbtn.place(x=165,y=350)

        loginb=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\loginbutton.png")
        loginb=loginb.resize((150,80))
        self.photoimglogin=ImageTk.PhotoImage(loginb)
        loginbtn=Button(login,image=self.photoimglogin,bg="#132542",bd=0,font=("Lucida Fax",12,"italic"),command=self.Login,fg="#2874ed",activebackground="#132542",activeforeground="#4e91fc")
        loginbtn.place(x=100,y=400)

    def clear(self):
        self.usernamefield.set("")
        self.passwordfield.set("")

    def Login(self):
        print(self.usernamefield.get(),self.passwordfield.get())
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select COUNT(*) from loginregister WHERE Username='{}' AND Password='{}'".format(self.usernamefield.get(),self.passwordfield.get())
        my_cursor.execute(query)
        for i in my_cursor:
            print(i[0])

        if (self.usernamefield.get()=="" or self.passwordfield.get()==""):
            messagebox.showinfo("Error","Field is Empty",parent=self.window) 
        elif i[0]==1:
            self.clear()
            self.attendance()
        elif i[0]==0:
            messagebox.showinfo("Warning","Invalid Username or Password...",parent=self.window)
            self.clear()

    #for calling external file from here
    def forgot_pass(self):
        self.new_window=Toplevel(self.window)
        self.app=forgot(self.new_window)

    def attendance(self):
        self.new_window=Toplevel(self.window)
        self.app=Attendance(self.new_window)
        

if __name__=="__main__":
    window=Tk()
    obj=Login(window)
    window.mainloop()
