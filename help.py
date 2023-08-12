from tkinter import*
class Help:
    def __init__(self,window):
        self.window=window
        self.window.title("Help")
        self.window.geometry("1275x725+0+0")

        mainframe=Frame(self.window,height=725,width=1275,bg="#F0E3D1")
        mainframe.place(x=0,y=0)

        Help=Label(mainframe,text="HELP?",font=("cooper black",22,"italic"),fg="yellow",bg="black",width=65)
        Help.place(x=0,y=0)

        variable="1.Project Consist of six Activities such as Login,Registration,Attendance,LoginRegistration,RegisteredStudent,ViewAttendance."
        text=Label(mainframe,text=variable,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text.place(x=10,y=50)

        variable1="2.Login is Only for Authentication Purpose."
        text1=Label(mainframe,text=variable1,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text1.place(x=10,y=70)

        variable2="3.Registration of student for attendance purpose."
        text2=Label(mainframe,text=variable2,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text2.place(x=10,y=90)

        variable3="4.Attendance consist of camera for taking attendance purpose."
        text3=Label(mainframe,text=variable3,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text3.place(x=10,y=110)

        variable4="5.LoginRegistration is for register authorized person."
        text4=Label(mainframe,text=variable4,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text4.place(x=10,y=130)

        variable5="6.RegisteredStudent contain student who can give attendance."
        text5=Label(mainframe,text=variable5,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text5.place(x=10,y=150)

        variable6="7.ViewAttendance is use to see the Everydays attendance."
        text6=Label(mainframe,text=variable6,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text6.place(x=10,y=170)

        variable7="8.Attendance section attendacnce Camera will active for next 10second and can able to capture the multiple Qr in one Attendace session."
        text7=Label(mainframe,text=variable7,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text7.place(x=10,y=190)

        variable8="9.Registration is mandatory for giving attendance otherwise it will consider you as an Unauthorized person."
        text8=Label(mainframe,text=variable8,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text8.place(x=10,y=210)

        variable9="10.Initially Authorized person need to login the setup after that attendance will going to mark."
        text9=Label(mainframe,text=variable9,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text9.place(x=10,y=230)

        variable10="11.Only Authorized person can do the Login with username and password."
        text10=Label(mainframe,text=variable10,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text10.place(x=10,y=250)

        variable11="12.Can able to Manupulate the Registered Student."
        text11=Label(mainframe,text=variable11,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text11.place(x=10,y=270)

        variable12="13.Can able to Manupulate the Authorized Person."
        text12=Label(mainframe,text=variable12,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text12.place(x=10,y=290)

        variable13="14.Current day attendance status shown in the same attendance page."
        text13=Label(mainframe,text=variable13,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text13.place(x=10,y=310)

        variable14="15.Separate Attendance View also Provided where you can Search and Delete the specific Date and Roll number attendance."
        text14=Label(mainframe,text=variable14,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text14.place(x=10,y=330)

        variable15="16.Login password change can only done through Bestfriend name and Username."
        text15=Label(mainframe,text=variable15,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text15.place(x=10,y=350)

        variable16="17.Login Account deletion can only done through the Username and BestFriend Name."
        text16=Label(mainframe,text=variable16,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text16.place(x=10,y=370)

        variable17="18.Attendacne will marked along with date and specific time."
        text17=Label(mainframe,text=variable17,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text17.place(x=10,y=390)

        variable18="19.Attendance and Registration Done only under guidance of Authorized person."
        text18=Label(mainframe,text=variable18,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text18.place(x=10,y=410)

        variable19="20.Only Faculty can only operate the Attendance system."
        text19=Label(mainframe,text=variable19,font=("Cooper black",12,"bold"),fg="#636363",bg="#F0E3D1")
        text19.place(x=10,y=430)

        
        


if __name__=="__main__":
    window=Tk()
    obj=Help(window)
    window.mainloop()
