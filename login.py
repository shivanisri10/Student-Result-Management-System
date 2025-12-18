from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3
import os
class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #=====Images=======
        self.phone_image=ImageTk.PhotoImage(file="images/side.png") 
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)
        
        #=====Login Frame=======
        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Andalus",15),bg="white",fg="#767676").place(x=50,y=100)
        self.uname=StringVar()
        self.psw=StringVar()
        txt_username=Entry(login_frame,textvariable=self.uname,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767676").place(x=50,y=200)
        txt_pass=Entry(login_frame,textvariable=self.psw,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Antenna",15,"bold"),bg="#008DFF",activebackground="#008DFF",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="Forgot Password?",font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #=====Register Frame=======
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have an account?",font=("times new roman",13),bg="white").place(x=40,y=20)
        btn_signup=Button(register_frame,text="Sign Up",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E",command=self.register_window).place(x=200,y=17)

    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def login(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.uname.get()=="" or self.psw.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                # [00:12:13] Database check for email and password
                cur.execute("select * from employee where email=? AND pass=?",(self.uname.get(),self.psw.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.uname.get()}",parent=self.root)
                    self.root.destroy()
                    # [00:12:15] Launching dashboard.py exactly like the video
                    os.system("python dashboard.py") 
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Login_System(root)
    root.mainloop()