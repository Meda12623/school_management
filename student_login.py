import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font

# إنشاء اتصال بقاعدة بيانات SQLite
con = sqlite3.connect('school_management.db')
cursor = con.cursor()

# إنشاء جدول الطلاب إذا لم يكن موجودًا
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        StudentID TEXT NOT NULL,
        StudentName TEXT NOT NULL,
        Class TEXT NOT NULL,
        Password TEXT NOT NULL
    )
''')
con.commit()

# بيانات الطلاب الافتراضية
students = [
    ('S001', 'Ali Hassan', '10A', 'pass123'),
    ('S002', 'Aya Mahmoud', '11B', '123456'),
    ('S003', 'Omar Ahmed', '10C', '987654'),
    ('S004', 'Sara Ali', '12A', 'sara2024')
]

# إدخال البيانات في جدول الطلاب إذا كانت فارغة
for student in students:
    cursor.execute("INSERT OR IGNORE INTO Students (StudentID, StudentName, Class, Password) VALUES (?, ?, ?, ?)", student)
con.commit()

# إعداد نافذة التطبيق الرئيسية
win = tk.Tk()
win.title("Student Login System")
win.geometry("600x300")
win.resizable(0, 0)
win.configure(background="grey")

# إعداد الخطوط
labelfont2 = ('times', 18, 'bold')

# وظيفة نافذة تسجيل الدخول

def login_window():
    def login():
        student_id = id_var.get()
        password = pass_var.get()

        if not (student_id and password):
            messagebox.showerror("Error", "Please fill all fields!")
            return

        cursor.execute("SELECT * FROM Students WHERE StudentID = ? AND Password = ?", (student_id, password))
        user = cursor.fetchone()

        if user:
            messagebox.showinfo("Success", f"Welcome, {user[1]} from Class {user[2]}!")
        else:
            messagebox.showerror("Error", "Invalid Student ID or Password!")

    login_win = tk.Toplevel(win)
    login_win.title("Login")
    login_win.geometry("400x300")
    login_win.configure(background="lightblue")

    ttk.Label(login_win, text="Student Login", font=labelfont2, background="lightblue", foreground="black").pack(pady=10)

    ttk.Label(login_win, text="Student ID", font=labelfont2, background="lightblue", foreground="black").pack()
    id_var = tk.StringVar()
    ttk.Entry(login_win, width=30, textvariable=id_var).pack()

    ttk.Label(login_win, text="Password", font=labelfont2, background="lightblue", foreground="black").pack()
    pass_var = tk.StringVar()
    ttk.Entry(login_win, width=30, textvariable=pass_var, show="*").pack()

    tk.Button(login_win, text="Login", command=login, font=font.Font(size=15), bg="blue", fg="white").pack(pady=20)

# وظيفة نافذة التسجيل

def register_window():
    import student_registration

# العنوان الرئيسي
ttk.Label(
    win, text="\n\tSTUDENT MANAGEMENT SYSTEM\t\n", font=('times', 20, 'bold'), background="darkblue", foreground="white"
).pack(pady=20)

# زري تسجيل الدخول والتسجيل
tk.Button(win, text="Login", command=login_window, font=font.Font(size=15), width=20).pack(pady=10)
tk.Button(win, text="Register", command=register_window, font=font.Font(size=15), width=20).pack(pady=10)

# تشغيل النافذة
win.mainloop()

# إغلاق الاتصال بقاعدة البيانات
con.close()
