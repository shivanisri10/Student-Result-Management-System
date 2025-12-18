from tkinter import *
from PIL import Image, ImageTk, ImageDraw
import time
from math import *
import sqlite3
from tkinter import messagebox
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")

        left_lbl = Label(self.root, bg="#08A3D2", bd=0).place(x=0, y=0, relheight=1, width=600)
        
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)

        title = Label(login_frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)

        email = Label(login_frame, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)

        pass_ = Label(login_frame, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.txt_password = Entry(login_frame, font=("times new roman", 15), bg="lightgray", show="*")
        self.txt_password.place(x=250, y=280, width=350, height=35)

        btn_reg = Button(login_frame, text="Register new Account?", command=self.register_window, font=("times new roman", 14), bg="white", bd=0, fg="#B00857", cursor="hand2").place(x=250, y=320)
        btn_login = Button(login_frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)

        # Clock logic from the video
        self.lbl_clock = Label(self.root, compound=BOTTOM, bg="#081923", bd=0)
        self.lbl_clock.place(x=90, y=120, width=350, height=450)
        self.working()

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png").resize((300, 300), Image.LANCZOS)
        clock.paste(bg, (50, 50))
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50*cos(radians(hr))), fill="#DF005E", width=4)
        draw.line((origin, 200+80*sin(radians(min_)), 200-80*cos(radians(min_))), fill="white", width=3)
        draw.line((origin, 200+100*sin(radians(sec_)), 200-100*cos(radians(sec_))), fill="yellow", width=2)
        return clock

    def working(self):
        h, m, s = time.strftime("%H"), time.strftime("%M"), time.strftime("%S")
        hr, min_, sec_ = (int(h)/12)*360, (int(m)/60)*360, (int(s)/60)*360
        self.img = ImageTk.PhotoImage(self.clock_image(hr, min_, sec_))
        self.lbl_clock.config(image=self.img)
        self.lbl_clock.after(200, self.working)

    def register_window(self):
        self.root.destroy()
        os.system("python register.py")

    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?", (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome: {row[1]}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()