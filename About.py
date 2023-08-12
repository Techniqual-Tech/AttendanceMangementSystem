from tkinter import*

class About:
    def __init__(self,window):
        self.window=window
        self.window.title("About Page")
        self.window.config(bg="black")
        self.window.geometry("1280x725+0+0")

        mainframe=Frame(self.window,height="715",width="1270",bg="#e3e2de")
        mainframe.place(x=5,y=5)

        about=Label(mainframe,text=u"\u2666\u2666\u2666\u2666\u2666\u2666 About \u2666\u2666\u2666\u2666\u2666\u2666",font=("Cooper Black",30,"bold"),bg="black",fg="yellow",width=46)
        about.place(x=0,y=0)

        cameralabel=Label(mainframe,text=u"\U0001F4F7",font=("Cooper black",50,"bold"),bg="black",fg="yellow")
        cameralabel.place(x=0,y=-32)

        handlabel=Label(mainframe,text=	u"\U0001F44B",font=("Cooper black",41,"bold"),bg="black",fg="yellow")
        handlabel.place(x=1170,y=-17)

        pointinghand=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand.place(x=80,y=100)

        ph=Label(mainframe,text="This is QR Code Based Attendance Management System.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph.place(x=120,y=105)
        
        pointinghand1=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand1.place(x=80,y=150)

        ph1=Label(mainframe,text="Purpose Is to Quick And Fast Attendance Management.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph1.place(x=120,y=155)

        pointinghand2=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand2.place(x=80,y=200)

        ph2=Label(mainframe,text="Specific For Particular Standard Attendance Management.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph2.place(x=120,y=205)

        pointinghand3=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand3.place(x=80,y=250)

        ph3=Label(mainframe,text="QR Code Generated At Time Of Student Registration.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph3.place(x=120,y=255)

        pointinghand4=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand4.place(x=80,y=300)

        ph4=Label(mainframe,text="Generated QR Code Required For Attendance.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph4.place(x=120,y=305)

        pointinghand5=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand5.place(x=80,y=350)

        ph5=Label(mainframe,text="Registered Student Can Be Managed By Authorized Person.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph5.place(x=120,y=355)

        pointinghand6=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand6.place(x=80,y=400)

        ph5=Label(mainframe,text="Need To Start Camera before Attendance , Will Active For Next 10sec. ",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph5.place(x=120,y=405)

        pointinghand7=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand7.place(x=80,y=450)

        ph5=Label(mainframe,text="We Can take a View of All Day's Attendance.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph5.place(x=120,y=455)

        pointinghand8=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand8.place(x=80,y=500)

        ph5=Label(mainframe,text="Attendance Can Be Search Or Can Be Delete.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph5.place(x=120,y=505)

        pointinghand9=Label(mainframe,text=u"\U0001F449",font=("Cooper black",22,"bold"),bg="#e3e2de")
        pointinghand9.place(x=80,y=550)

        ph5=Label(mainframe,text="Authorized Person Can Login By Entering Username and Password.",bg="#e3e2de",font=("Copperplate Gothic Bold",20,"italic"))
        ph5.place(x=120,y=555)


        

if __name__=="__main__":
    window=Tk()
    obj=About(window)
    window.mainloop()
    
