from tkinter import*
from PIL import Image, ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import sqlite3

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #=====Title=======
        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")
        title = Label(self.root, text="Student Result Management System", padx=10, 
                      compound=LEFT, image=self.logo_dash, font=("goudy old style", 20, "bold"), 
                      bg="#03303e", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #=====Menus=======
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=60, width=1330, height=80)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=10, y=5, width=210, height=45)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=230, y=5, width=210, height=45)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=450, y=5, width=210, height=45)
        btn_view = Button(M_Frame, text="View Student Results", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=670, y=5, width=210, height=45)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=890, y=5, width=210, height=45)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1110, y=5, width=210, height=45)

        #=====Content Window (Alignment Adjusted to Left)=======
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        # Changed x from 400 to 220 to fix right-side alignment
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=220, y=160, width=920, height=350)

        #=====Details Widgets (Alignment Adjusted to Left)=======
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=220, y=520, width=300, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=530, y=520, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=("goudy old style", 20, "bold"), bd=10, relief=RIDGE, bg="#038071", fg="white")
        self.lbl_result.place(x=840, y=520, width=300, height=100)

        #=====Footer=======
        footer = Label(self.root, text="SRMS-Student Result Management System\nContact Us for any Technical Issue: shivanisrir007@gmail.com", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        self.update_content()

    def update_content(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            res = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(res))}]")

            cur.execute("select * from student")
            res = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(res))}]")

            cur.execute("select * from result")
            res = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(res))}]")

            # Refresh data every 5 seconds without updating a clock label
            self.lbl_course.after(5000, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}")

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()