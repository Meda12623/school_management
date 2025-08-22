import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as font

def start(win, subject):
    # إنشاء اتصال بقاعدة بيانات SQLite
    con = sqlite3.connect('school_management.db')
    cursor = con.cursor()

    # إعداد نافذة إدارة المعلمين
    def Search():
        messagebox.showinfo("Functionality", "Teacher Search Screen Coming Soon!")

    def Courses():
        messagebox.showinfo("Functionality", "Courses Management Screen Coming Soon!")

    # إعداد نافذة التطبيق
    win = tk.Tk()
    win.title("Teacher Management")
    win.geometry("600x500")
    win.resizable(0, 0)
    win.configure(background="grey")

    # إعداد خطوط النصوص
    labelfont = ('times', 20, 'bold')
    labelfont1 = ('times', 15, 'bold')
    labelfont2 = ('times', 18, 'bold')

    # العنوان الرئيسي
    ttk.Label(
        win, text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n", font=labelfont2, background="blue", foreground="white"
    ).pack()

    # عنوان نافذة إدارة المعلمين
    ttk.Label(
        win, text="\n\nTeacher Management\n", font=labelfont1, background="grey", foreground="white"
    ).pack()

    # زر البحث
    ttk.Label(win, text="Search", font=labelfont1, background="grey", foreground="white").pack()
    search_butt = tk.Button(win, text="Search", command=Search, font=font.Font(size=15), width=20)
    search_butt.pack(pady=10)

    # زر إدارة الدورات
    ttk.Label(win, text="Courses", font=labelfont1, background="grey", foreground="white").pack()
    courses_butt = tk.Button(win, text="Courses", command=Courses, font=font.Font(size=15), width=20)
    courses_butt.pack(pady=10)

    # تشغيل النافذة
    win.mainloop()
