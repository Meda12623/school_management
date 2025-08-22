import tkinter as tk
from tkinter import font
import admin  # استيراد ملف admin
from teacher_registration import start as start_teacher  # استيراد التسجيل للمدرسين

# إعداد نافذة التطبيق الرئيسية
win = tk.Tk()
win.title("Student Login System")
win.geometry("400x400")
win.configure(background="grey")

# إعداد الخطوط
button_font = font.Font(size=15)

# العنوان الرئيسي0
tk.Label(
    win, text="\nChoose Your Role\t\n", font=('times', 20, 'bold'), background="darkblue", foreground="white", anchor='center'
).pack(pady=20)

# تعريف وظائف الأزرار
def teacher_registration():
    start_teacher(win)

def student_login():
    import student_login
    student_login.start(win)  # استدعاء نافذة تسجيل الدخول للطلاب

def admin_login():
    admin.start(win)  # استدعاء نافذة تسجيل الدخول للمسؤول

# أزرار الأدوار الثلاثة
tk.Button(win, text="Teacher", font=button_font, width=20, command=teacher_registration).pack(pady=10)
tk.Button(win, text="Student", font=button_font, width=20, command=student_login).pack(pady=10)
tk.Button(win, text="Admin", font=button_font, width=20, command=admin_login).pack(pady=10)

# تشغيل النافذة
win.mainloop()
