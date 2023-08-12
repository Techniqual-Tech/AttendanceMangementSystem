from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import re
import mysql.connector
class LoginRegistration:
    def __init__(self,window):
        self.window=window
        self.window.title("LoginRegistration")
        self.window.geometry("1280x725+0+0")

        heading=Label(self.window,text="LoginRegistration",font=("Cooper Black",31,"bold"),fg="yellow",bg="black",width=45)
        heading.place(x=0,y=0)

        self.mainframe=Frame(self.window,bg="grey",width="1280",height="680",relief=RIDGE,bd=5)
        self.mainframe.place(x=0,y=53)

        self.registerFrame=Frame(self.mainframe,bg="#a0faa6",width="800",height="600",relief=RIDGE,bd=5)
        self.registerFrame.place(x=20,y=40)

        self.deleteFrame=Frame(self.mainframe,bg="#f2afa0",width="400",height="600",relief=RIDGE,bd=5)
        self.deleteFrame.place(x=850,y=40)

        #variable declaration
        self.Namefield=StringVar()
        self.Designationfield=StringVar()
        self.Usernamefield=StringVar()
        self.Passwordfield=StringVar()
        self.CPasswordfield=StringVar()
        self.BestFfield=StringVar()
        self.DUsernamefield=StringVar()
        self.DPasswordfield=StringVar()
        self.DBestFfield=StringVar()
        

        #loginregister image
        Lreg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\loginregister.png")
        Lreg=Lreg.resize((180,80))
        self.photoimgcr=ImageTk.PhotoImage(Lreg)
        LregLabel=Label(self.registerFrame,image=self.photoimgcr,bg="#a0faa6",bd=0,relief=RIDGE)
        LregLabel.place(x=300,y=0,width=160,height=60)

        #deletereg image
        Dreg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\deletereg.png")
        Dreg=Dreg.resize((150,60))
        self.photoimgcr1=ImageTk.PhotoImage(Dreg)
        DregLabel=Label(self.deleteFrame,image=self.photoimgcr1,bg="#f2afa0",bd=0,relief=RIDGE)
        DregLabel.place(x=120,y=0,width=150,height=60)

        NameLabel=Label(self.registerFrame,text="Name :-",font=("ALGERIAN",20,"bold"),bg="#a0faa6")
        NameLabel.place(x=5,y=90)
        NameEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.Namefield)
        NameEntry.place(x=280,y=80)

        DesignationLabel=Label(self.registerFrame,text="Designation :-",font=("ALGERIAN",20,"bold"),bg="#a0faa6")
        DesignationLabel.place(x=5,y=150)
        DesigEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.Designationfield)
        DesigEntry.place(x=280,y=140)

        UserNameLabel=Label(self.registerFrame,text="UserName :-",font=("ALGERIAN",20,"bold"),bg="#a0faa6")
        UserNameLabel.place(x=5,y=210)
        UnameEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.Usernamefield)
        UnameEntry.place(x=280,y=200)
        hintusername=Label(self.registerFrame,text="Note:-length should be 8 character, begin with letter, no special character.....",font=("arial",7,"italic"),bg="#a0faa6",height=1,fg="red")
        hintusername.place(x=280,y=245)

        PasswordLabel=Label(self.registerFrame,text="Password :-",font=("ALGERIAN",20,"bold"),bg="#a0faa6")
        PasswordLabel.place(x=5,y=270)
        PassEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.Passwordfield)
        PassEntry.place(x=280,y=260)
        hintpassword=Label(self.registerFrame,text="Note:-Combination of letter,number,special character,Lcase,Ucase,length of 8.....",font=("arial",7,"italic"),bg="#a0faa6",height=1,fg="red")
        hintpassword.place(x=280,y=305)

        CPasswordLabel=Label(self.registerFrame,text="Confirm Password :-",font=("ALGERIAN",18,"bold"),bg="#a0faa6")
        CPasswordLabel.place(x=5,y=330)
        CPassEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.CPasswordfield,show="*")
        CPassEntry.place(x=280,y=320)

        SchoolFredLabel=Label(self.registerFrame,text="Best Friend :-",font=("ALGERIAN",20,"bold"),bg="#a0faa6")
        SchoolFredLabel.place(x=5,y=390)
        ScolfEntry=Entry(self.registerFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=30,textvariable=self.BestFfield)
        ScolfEntry.place(x=280,y=380)
        sfrndHint=Label(self.registerFrame,text="Note:-Required in case forgot password & Account deletion....",font=("arial",7,"italic"),bg="#a0faa6",height=1,fg="red")
        sfrndHint.place(x=280,y=425)

        self.checkvar1=IntVar()
        checkbutton=Checkbutton(self.registerFrame,variable=self.checkvar1,onvalue=1,offvalue=0,bg="#a0faa6",font=("cooper black",11,"bold"))
        checkbutton.place(x=270,y=440)
        tclabel=Button(self.registerFrame,text="I agree term's and condition.",bg="#a0faa6",font=("cooper black",11,"bold"),fg="blue",bd=0,activebackground="#a0faa6")
        tclabel.place(x=290,y=440)

        text="1)Provided Information is Correct.\n2)Registration Done Under Authorized Person.\n3)You are the Faculty Person."
        tclabel.bind("<Button-1>",lambda e:message(text))

        def message(msg):
            messagebox.showwarning("T & C",msg,parent=self.window) 


        LRbutton=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\regbuttonLR.png")
        LRbutton=LRbutton.resize((130,60))
        self.photoimgcr2=ImageTk.PhotoImage(LRbutton)
        LRButton=Button(self.registerFrame,image=self.photoimgcr2,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.Register)
        LRButton.place(x=350,y=490,width=125,height=55)


        Dusername=Label(self.deleteFrame,text="UserName",font=("ALGERIAN",20,"bold"),bg="#f2afa0")
        Dusername.place(x=120,y=90)
        DusernameE=Entry(self.deleteFrame,font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=20,textvariable=self.DUsernamefield)
        DusernameE.place(x=40,y=130)

        Dpass=Label(self.deleteFrame,text="Password",font=("ALGERIAN",20,"bold"),bg="#f2afa0")
        Dpass.place(x=120,y=190)
        DpassE=Entry(self.deleteFrame,font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=20,show="*",textvariable=self.DPasswordfield)
        DpassE.place(x=40,y=230)
        
        DSchoolFredLabel=Label(self.deleteFrame,text="Best Friend",font=("ALGERIAN",20,"bold"),bg="#f2afa0")
        DSchoolFredLabel.place(x=100,y=290)
        DScolfEntry=Entry(self.deleteFrame,text="Name",font=("Arial",20,"bold"),relief=RIDGE,bd=5,width=20,textvariable=self.DBestFfield)
        DScolfEntry.place(x=40,y=330)

        unreg=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\unreg.png")
        unreg=unreg.resize((180,130))
        self.photoimgcrD=ImageTk.PhotoImage(unreg)
        unregbutton=Button(self.deleteFrame,image=self.photoimgcrD,bg="#f2afa0",bd=0,relief=RIDGE,activebackground="#f2afa0",command=self.Unsubscribed)
        unregbutton.place(x=115,y=490,width=160,height=70)

        self.checkvar2=IntVar()
        checkbutton1=Checkbutton(self.deleteFrame,variable=self.checkvar2,offvalue=0,onvalue=1,bg="#f2afa0",font=("cooper black",11,"bold"))
        checkbutton1.place(x=50,y=400)
        Dtclabel=Button(self.deleteFrame,text="I agree term's and condition.",bg="#f2afa0",font=("cooper black",11,"bold"),fg="blue",bd=0,activebackground="#f2afa0")
        Dtclabel.place(x=70,y=400)

        textt="1)Unregister Only Done By Authorized Person.\n2)Register Person should have the knowledge about their unregistration.\n3)Unregistration cause revoking some permission from authorized person."
        Dtclabel.bind("<Button-1>",lambda e:messages(textt))

        def messages(msg):
            messagebox.showwarning("T & C",msg,parent=self.window)



    #for resetingdata of variable imng
        NameC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        NameC=NameC.resize((20,20))
        self.photoimg1=ImageTk.PhotoImage(NameC)
        NameresetButton=Button(self.registerFrame,image=self.photoimg1,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.nameC)
        NameresetButton.place(x=750,y=100,width=20,height=20)

        DesignationC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        DesignationC=DesignationC.resize((20,20))
        self.photoimg2=ImageTk.PhotoImage(DesignationC)
        DesignationresetButton=Button(self.registerFrame,image=self.photoimg2,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.DesigC)
        DesignationresetButton.place(x=750,y=160,width=20,height=20)

        UsernameC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        UsernameC=UsernameC.resize((20,20))
        self.photoimg3=ImageTk.PhotoImage(UsernameC)
        UsernameresetButton=Button(self.registerFrame,image=self.photoimg3,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.UserNC)
        UsernameresetButton.place(x=750,y=220,width=20,height=20)

        PasswordC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        PasswordC=PasswordC.resize((20,20))
        self.photoimg4=ImageTk.PhotoImage(PasswordC)
        PasswordresetButton=Button(self.registerFrame,image=self.photoimg4,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.PassC)
        PasswordresetButton.place(x=750,y=280,width=20,height=20)

        PasswordCC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        PasswordCC=PasswordCC.resize((20,20))
        self.photoimg5=ImageTk.PhotoImage(PasswordCC)
        PasswordCresetButton=Button(self.registerFrame,image=self.photoimg5,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.CPassC)
        PasswordCresetButton.place(x=750,y=340,width=20,height=20)

        BestFrC=Image.open(r"D:\Vicky_All_Program\python\AttendanceManagmentSystem\Refdeldata.png")
        BestFrC=BestFrC.resize((20,20))
        self.photoimg6=ImageTk.PhotoImage(BestFrC)
        BestFrresetButton=Button(self.registerFrame,image=self.photoimg6,bg="#a0faa6",bd=0,relief=RIDGE,activebackground="#a0faa6",command=self.BestFrC)
        BestFrresetButton.place(x=750,y=400,width=20,height=20)

    #clear methods
    def nameC(self):
        self.Namefield.set("")
    def DesigC(self):
        self.Designationfield.set("")
    def UserNC(self):
        self.Usernamefield.set("")
    def PassC(self):
        self.Passwordfield.set("")
    def CPassC(self):
        self.CPasswordfield.set("")
    def BestFrC(self):
        self.BestFfield.set("")
    def DUserNC(self):
        self.DUsernamefield.set("")
    def DPassC(self):
        self.DPasswordfield.set("")
    def DBestFrC(self):
        self.DBestFfield.set("")
        
    def Register(self):
        print("Register")
        print(self.Namefield.get(),self.Designationfield.get(),self.Usernamefield.get(),self.Passwordfield.get(),self.CPasswordfield.get(),self.BestFfield.get())
        if self.Namefield.get()=="" or self.Designationfield.get()=="" or self.Usernamefield.get()=="" or self.Passwordfield.get()=="" or self.CPasswordfield.get()=="" or self.BestFfield.get()=="":
            messagebox.showwarning("Warning","Every Field is Mandatory.",parent=self.window)
            print("every field is mandatory")
        elif self.checkvar1.get()==0:
            messagebox.showwarning("Warning","You Have to agree with term's and condition.",parent=self.window)
            print("You havent chcek the ta nd c")
        else:
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            character=False
            if(regex.search(self.Usernamefield.get())) == None:
                if len(self.Usernamefield.get())==8:
                    number=0
                    string=0
                    for i in self.Usernamefield.get():
                        try:
                            int(i)
                            number=number+1
                        except:
                            string=string+1
                            if number==0 and string==1:
                                character=True
                                
                    if number==8:
                        messagebox.showwarning("Warning","UserName shouldn't alone Numeric.",parent=self.window)
                        print("UserName shouldn't alone Numeric")
                        self.UserNC()
                    elif string==8:
                        messagebox.showwarning("Warning","UserName shouldn't alone Alphabetic.",parent=self.window)
                        self.UserNC()
                    elif character==False:
                        messagebox.showwarning("Warning","UserName shouldn start with letter.",parent=self.window)
                        self.UserNC()
                    else:
                        queue=[]
                        print("for password validate")
                        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
                        if(regex.search(self.Passwordfield.get())) !=None:
                            if len(self.Passwordfield.get())==8:
                                numbers=0
                                strings=0
                                for j in self.Passwordfield.get():
                                    try:
                                        int(j)
                                        numbers=numbers+1
                                    except:
                                        strings=strings+1
                                        queue.append(j)
                                if numbers==8 or strings==8:
                                    print("either str or int 8")
                                    messagebox.showwarning("Warning","Password should contains Combinaton UCase,LCase,Special character,number.",parent=self.window)
                                    self.PassC()
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
                                        self.PassC()
                                    else:
                                        if  self.Passwordfield.get()== self.CPasswordfield.get():
                                            try:
                                                int(self.BestFfield.get())
                                                messagebox.showwarning("Warning","Best Friend Name can't be Numeric",parent=self.window)
                                                self.BestFrC()
                                            except:
                                                conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
                                                my_cursor=conn.cursor()
                                                query="select COUNT(*) from loginregister WHERE Username='{}'".format(self.Usernamefield.get())
                                                my_cursor.execute(query)
                                                for i in my_cursor:
                                                    print(i[0])
                                                if i[0]==0:
                                                    my_cursor.execute("insert into loginregister values(%s,%s,%s,%s,%s,%s)",(
                                                                                                               self.Namefield.get(),
                                                                                                               self.Designationfield.get(),
                                                                                                               self.Usernamefield.get(),
                                                                                                               self.Passwordfield.get(),
                                                                                                               self.CPasswordfield.get(),
                                                                                                               self.BestFfield.get(),
                                                                                                            ))
                                                    conn.commit()
                                                    conn.close()
                                                    messagebox.showwarning("NOTE","Registeration succesfully.",parent=self.window)
                                                    self.nameC()
                                                    self.DesigC()
                                                    self.UserNC()
                                                    self.PassC()
                                                    self.CPassC()
                                                    self.BestFrC()
                                                elif i[0]==1:
                                                    messagebox.showwarning("Warning","Username {} Already Registered".format(self.Usernamefield.get()),parent=self.window)
                                                    self.UserNC()
                                        else:
                                            messagebox.showwarning("Warning","Password and Confirm Password should same",parent=self.window)
                                            self.CPassC()
                                    

                        else:
                            print("No special characatr")
                            messagebox.showwarning("Warning","Password should be length of eigth character Can contains Combinaton UCase,LCase,Special character,number.",parent=self.window)
                            self.PassC()
                        
                else:
                    messagebox.showwarning("Warning","Username should be eight character in length.",parent=self.window)
                    self.UserNC()
                
                            
                print("String is accepted")
            else:
                print("String is not accepted.")
                messagebox.showwarning("Warning","UserName should AlphaNumeric shouldn't contain special symbol",parent=self.window)
                self.UserNC()
                
            

    def Unsubscribed(self):
        print("Unsubscribed")
        print(self.DUsernamefield.get(),self.DPasswordfield.get(),self.DBestFfield.get())
        conn=mysql.connector.connect(host="localhost",username="root",password="vicky@123//",database="attendanceproject")
        my_cursor=conn.cursor()
        query="select COUNT(*) from loginregister WHERE Username='{}' AND Password='{}' AND BestFriend='{}'".format(self.DUsernamefield.get(),self.DPasswordfield.get(),self.DBestFfield.get())
        my_cursor.execute(query)
        for i in my_cursor:
            print(i[0])
        if self.DUsernamefield.get()=="" or self.DPasswordfield.get()=="" or self.DBestFfield.get()=="":
            messagebox.showwarning("Warning","Every Field is Mandatory...",parent=self.window)
        elif self.checkvar2.get()==0:
            messagebox.showwarning("Warning","You Have to Agree with term's and condition...",parent=self.window)
        else:
            if i[0]==0:
                messagebox.showwarning("Warning","No Data Found with\nUserame={}\nPassword={}\nBestFriend={}".format(self.DUsernamefield.get(),self.DPasswordfield.get(),self.DBestFfield.get()),parent=self.window)
                self.DUserNC()
                self.DPassC()
                self.DBestFrC()
            elif i[0]==1:
                queryd="DELETE from loginregister WHERE Username='{}' AND Password='{}' AND BestFriend='{}'".format(self.DUsernamefield.get(),self.DPasswordfield.get(),self.DBestFfield.get())
                my_cursor.execute(queryd)
                conn.commit()
                conn.close()
                messagebox.showwarning("NOTE","Data Delete Successfully with Username '{}'".format(self.DUsernamefield.get()),parent=self.window)
                self.DUserNC()
                self.DPassC()
                self.DBestFrC()
                

        

        

if __name__=="__main__":
    window=Tk()
    obj=LoginRegistration(window)
    window.mainloop()
    
    
