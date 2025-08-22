
# # حذف الجدول القديم إذا كان موجودًا
# cursor.execute("DROP TABLE IF EXISTS Teachers")

# # إعادة إنشاء الجدول بالعمود الجديد Email
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Teachers (
#         Email TEXT NOT NULL,
#         TeacherName TEXT NOT NULL,
#         Subject TEXT NOT NULL,
#         Password TEXT NOT NULL
#     )
# ''')
# con.commit()

# # بيانات المدرسين
# teachers = [
#     ('mina.ibrahim@gmail.com', 'Mina Ibrahim', 'Math', '122154'),
#     ('saad.hegazy@gmail.com', 'Saad Hegazy', 'Math', '345000'),
#     ('mohammed.hafez@gmail.com', 'Mohammed Hafez', 'Arabic', '351200'),
#     ('reda.mohammed@gmail.com', 'Reda Mohammed', 'Arabic', '951357'),
#     ('jana.mahrous@gmail.com', 'Jana Mahrous', 'English', '154122'),
#     ('amira.eid@gmail.com', 'Amira Eid', 'English', '342666'),
#     ('ahmed.gamal@gmail.com', 'Ahmed Gamal', 'Social Studies', '654321'),
#     ('yasser.mohammed@gmail.com', 'Yasser Mohammed', 'Social Studies', '654951'),
#     ('karima.atef@gmail.com', 'Karima Atef', 'Science', '205205'),
#     ('mohammed.maged@gmail.com', 'Mohammed Maged', 'Science', '241122')
# ]

# # إدخال البيانات في الجدول
# for teacher in teachers:
#     cursor.execute(
#         "INSERT INTO Teachers (Email, TeacherName, Subject, Password) VALUES (?, ?, ?, ?)",
#         teacher
#     )
# con.commit()
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font
from teacher_management import start as teacher_management_start

def start(win):
    # إنشاء اتصال بقاعدة بيانات SQLite
    con = sqlite3.connect('school_management.db')
    cursor = con.cursor()

    # DROP THE TABLE TO RESET DATABASE
    cursor.execute("DROP TABLE IF EXISTS Teachers")

    # إنشاء جدول المدرسين إذا لم يكن موجودًا
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            Email TEXT NOT NULL,
            TeacherName TEXT NOT NULL,
            Subject TEXT NOT NULL,
            Password TEXT NOT NULL
        )
    ''')
    con.commit()

    teachers = [
        ('mina.ibrahim@gmail.com', 'Mina Ibrahim', 'Math', '122154'),
        ('saad.hegazy@gmail.com', 'Saad Hegazy', 'Math', '345000'),
        ('mohammed.hafez@gmail.com', 'Mohammed Hafez', 'Arabic', '351200'),
        ('reda.mohammed@gmail.com', 'Reda Mohammed', 'Arabic', '951357'),
        ('jana.mahrous@gmail.com', 'Jana Mahrous', 'English', '154122'),
        ('amira.eid@gmail.com', 'Amira Eid', 'English', '342666'),
        ('ahmed.gamal@gmail.com', 'Ahmed Gamal', 'Social Studies', '654321'),
        ('yasser.mohammed@gmail.com', 'Yasser Mohammed', 'Social Studies', '654951'),
        ('karima.atef@gmail.com', 'Karima Atef', 'Science', '205205'),
        ('mohammed.maged@gmail.com', 'Mohammed Maged', 'Science', '241122')
    ]
    # إدخال البيانات في الجدول
    for teacher in teachers:
        cursor.execute(
            "INSERT INTO Teachers (Email, TeacherName, Subject, Password) VALUES (?, ?, ?, ?)",
            teacher
        )
    con.commit()

    # إعداد نافذة التطبيق الرئيسية
    win = tk.Toplevel(win)
    email_var = tk.StringVar()
    pass_var = tk.StringVar()
    win.title("School Management System")
    win.geometry("600x300")
    win.resizable(0, 0)
    win.configure(background="grey")

    # إعداد الخطوط
    labelfont2 = ('times', 18, 'bold')

    # وظيفة نافذة تسجيل الدخول
    def login_window():
        def login():
            email = email_var.get()
            password = pass_var.get()
            print (email, password)

            if not (email and password):
                messagebox.showerror("Error", "Please fill all fields!")
                return

            cursor.execute("SELECT * FROM Teachers WHERE Email = ? AND Password = ?", (email, password))
            user = cursor.fetchone()

            if user:
                messagebox.showinfo("Success", f"Welcome, {user[1]}!")
                win.destroy()
                teacher_management_start(win, user[2])
            else:
                messagebox.showerror("Error", "Invalid email or password!")

        login_win = tk.Toplevel(win)
        login_win.title("Login")
        login_win.geometry("400x300")
        login_win.configure(background="grey")

        ttk.Label(login_win, text="Login", font=labelfont2, background="grey", foreground="white").pack(pady=10)

        ttk.Label(login_win, text="Email", font=labelfont2, background="grey", foreground="white").pack()
        ttk.Entry(login_win, width=30, textvariable=email_var).pack()

        ttk.Label(login_win, text="Password", font=labelfont2, background="grey", foreground="white").pack()
        ttk.Entry(login_win, width=30, textvariable=pass_var, show="*").pack()
 
        tk.Button(login_win, text="Login", command=login, font=font.Font(size=15)).pack(pady=20)

    # وظيفة نافذة التسجيل
    def register_window():
        def register():
            email = email_var.get()
            name = name_var.get()
            subject = subject_var.get()
            password = pass_var.get()

            if not (email and name and subject and password):
                messagebox.showerror("Error", "Please fill all fields!")
                return

            cursor.execute("SELECT * FROM Teachers WHERE Email = ?", (email,))
            if cursor.fetchone():
                messagebox.showerror("Error", "Email already exists!")
                return

            try:
                cursor.execute(
                    "INSERT INTO Teachers (Email, TeacherName, Subject, Password) VALUES (?, ?, ?, ?)",
                    (email, name, subject, password)
                )
                con.commit()
                messagebox.showinfo("Success", "Registration successful!")
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error occurred: {e}")

        register_win = tk.Toplevel(win)
        register_win.title("Register")
        register_win.geometry("400x400")
        register_win.configure(background="grey")

        ttk.Label(register_win, text="Register", font=labelfont2, background="grey", foreground="white").pack(pady=10)

        ttk.Label(register_win, text="Email", font=labelfont2, background="grey", foreground="white").pack()
        email_var = tk.StringVar()
        ttk.Entry(register_win, width=30, textvariable=email_var).pack()

        ttk.Label(register_win, text="Name", font=labelfont2, background="grey", foreground="white").pack()
        name_var = tk.StringVar()
        ttk.Entry(register_win, width=30, textvariable=name_var).pack()

        ttk.Label(register_win, text="Subject", font=labelfont2, background="grey", foreground="white").pack()
        subject_var = tk.StringVar()    
        subject_ent = ttk.Combobox(register_win, state='readonly', values=["Math", "Science", "English", "History", "Geography"], width = 30, textvariable=subject_var)
        subject_ent.pack()
        subject_ent.config()

        ttk.Label(register_win, text="Password", font=labelfont2, background="grey", foreground="white").pack()
        pass_var = tk.StringVar()
        ttk.Entry(register_win, width=30, textvariable=pass_var, show="*").pack()

        tk.Button(register_win, text="Register", command=register, font=font.Font(size=15)).pack(pady=20)

    # العنوان الرئيسي
    ttk.Label(
        win, text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n", font=('times', 20, 'bold'), background="blue", foreground="white"
    ).pack(pady=20)

    # زري تسجيل الدخول والتسجيل
    tk.Button(win, text="Login", command=login_window, font=font.Font(size=15), width=20).pack(pady=10)
    tk.Button(win, text="Register", command=register_window, font=font.Font(size=15), width=20).pack(pady=10)

    # تشغيل النافذة
    win.mainloop()

    # إغلاق الاتصال بقاعدة البيانات
    con.close()

