from tkinter import *
from tkinter import messagebox
import mysql.connector
import re
class forgot:
    def __init__(self,window):
        self.window=window
        self.window.title("forgotpassword")
        self.window.geometry("600x500+0+0")

        #variable declaration
        self.usernamefield=StringVar()
        self.bestfriendfield=StringVar()
        self.passwordfield=StringVar()
        self.Cpasswordfield=StringVar()

        mainframe=Frame(self.window,height=500,width=600,bg="#f7d472")
        mainframe.place(x=0,y=0)

        label=Label(mainframe,text="Forgot Password",bg="black",font=("Book Antiqua",22,"bold"),fg="yellow",width=33)
        label.place(x=0,y=0)

        username=Label(mainframe,text="Username:-",bg="#f7d472",font=("Book Antiqua",18,"bold"))
        username.place(x=5,y=80)
        uentry=Entry(mainframe,font=("Book Antiqua",16,"bold"),width=30,bd=2,relief=RIDGE,textvariable=self.usernamefield)
        uentry.place(x=190,y=80)

        BestFr=Label(mainframe,text="Best Friend:-",bg="#f7d472",font=("Book Antiqua",18,"bold"))
        BestFr.place(x=5,y=150)
        bfentry=Entry(mainframe,font=("Book Antiqua",16,"bold"),width=30,bd=2,relief=RIDGE,textvariable=self.bestfriendfield)
        bfentry.place(x=190,y=150)

        Password=Label(mainframe,text="New Password:-",bg="#f7d472",font=("Book Antiqua",18,"bold"))
        Password.place(x=5,y=220)
        Pentry=Entry(mainframe,font=("Book Antiqua",16,"bold"),width=30,bd=2,relief=RIDGE,textvariable=self.passwordfield)
        Pentry.place(x=190,y=220)
        hintpassword=Label(mainframe,text="Note:-Combination of letter,number,special character,Lcase,Ucase,length of 8.....",font=("arial",7,"italic"),bg="#f7d472",height=1,fg="red")
        hintpassword.place(x=190,y=252)

        Conf_Pass=Label(mainframe,text="Con_Password:-",bg="#f7d472",font=("Book Antiqua",18,"bold"))
        Conf_Pass.place(x=5,y=290)
        cPentry=Entry(mainframe,font=("Book Antiqua",16,"bold"),width=30,bd=2,relief=RIDGE,textvariable=self.Cpasswordfield,show="*")
        cPentry.place(x=190,y=290)

        forgot=Button(mainframe,text="Forgot",font=("Book Antiqua",18,"bold"),command=self.forgot)
        forgot.place(x=230,y=370)

    def forgot(self):
        print(self.usernamefield.get(),self.bestfriendfield.get(),self.passwordfield.get(),self.Cpasswordfield.get())
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select COUNT(*) from loginregister WHERE Username='{}' AND BestFriend='{}'".format(self.usernamefield.get(),self.bestfriendfield.get())
        my_cursor.execute(query)
        for i in my_cursor:
            print(i[0])

        if self.usernamefield.get()=="" or self.bestfriendfield.get()=="" or self.passwordfield.get()=="" or self.Cpasswordfield.get()=="":
            messagebox.showinfo("Warning","Every Field is Required...",parent=self.window)
        elif i[0]==1:
            queue=[]
            print("for password validate")
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if(regex.search(self.passwordfield.get())) !=None:
                if len(self.passwordfield.get())==8:
                    numbers=0
                    strings=0
                    for j in self.passwordfield.get():
                        try:
                            int(j)
                            numbers=numbers+1
                        except:
                            strings=strings+1
                            queue.append(j)
                    if numbers==8 or strings==8:
                        print("either str or int 8")
                        messagebox.showwarning("Warning","Password should contains Combinaton UCase,LCase,Special character,number.",parent=self.window)
                    else:
                        a=len(queue)
                        upper=0
                        lower=0
                        for ij in queue:
                            if ij.isupper():
                                upper=upper+1
                            elif ij.islower():
                                lower=lower+1
                        if upper==a or lower==a:
                            print("either no lcase or no ucase")
                            messagebox.showwarning("Warning","Password should contains Combinaton UCase,LCase.",parent=self.window)
                        else:
                            if  self.passwordfield.get()== self.Cpasswordfield.get():
                                querys="UPDATE loginregister SET Password='{}',ConfirmPassword='{}' WHERE Username='{}' AND BestFriend='{}'".format(self.passwordfield.get(),self.Cpasswordfield.get(),self.usernamefield.get(),self.bestfriendfield.get())
                                my_cursor.execute(querys)
                                conn.commit()
                                conn.close()
                                messagebox.showinfo("Warning","Password Reset Successfully",parent=self.window)
                                self.usernamefield.set("")
                                self.bestfriendfield.set("")
                                self.passwordfield.set("")
                                self.Cpasswordfield.set("")
                            else:
                                messagebox.showinfo("Warning","Password and Confirm password should Same",parent=self.window)
                                self.Cpasswordfield.set("")
                else:
                    messagebox.showinfo("Warning","Password should have 8 Characters",parent=self.window)
                    self.passwordfield.set("")
                    self.Cpasswordfield.set("")
            else:
                messagebox.showinfo("Warning","Password should Contain Special Character.",parent=self.window)
                self.passwordfield.set("")
                self.Cpasswordfield.set("")
        elif i[0]==0:
            messagebox.showinfo("Warning","You have Entered the Invalid Username or Bestfriend",parent=self.window)
            self.usernamefield.set("")
            self.bestfriendfield.set("")


if __name__=="__main__":
    window=Tk()
    obj=forgot(window)
    window.mainloop()
