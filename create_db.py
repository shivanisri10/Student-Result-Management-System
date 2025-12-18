import sqlite3
import os

def initialize_database():
    
    if os.path.exists("rms.db"):
        os.remove("rms.db")
    
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    
   
    cur.execute("""CREATE TABLE IF NOT EXISTS employee(
                    eid INTEGER PRIMARY KEY AUTOINCREMENT, 
                    f_name text, 
                    l_name text, 
                    contact text, 
                    email text, 
                    question text, 
                    answer text, 
                    password text)""")
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text, description text)")
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, dob text, contact text, admission text, course text, state text, city text, pin text, address text)")
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text, marks_ob text, full_marks text, per text)")
    
    con.commit()
    con.close()
    

if __name__ == "__main__":
    initialize_database()