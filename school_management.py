import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as font

# إنشاء اتصال بقاعدة البيانات
con = sqlite3.connect('school_management.db')
cursor = con.cursor()
# إنشاء جدول ourSubject إذا لم يكن موجودًا مسبقًا
try:
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS ourSubject( 
            subjectName TEXT NOT NULL,                  -- اسم الدورة 
            TeacherName TEXT NOT NULL                  -- اسم المدرس 
        ) 
    ''')
    con.commit()
    print("Table 'ourSubjects' created successfully with subjectName and TeacherName!")
except sqlite3.Error as e:
    print(f"Error creating table: {e}")

# إضافة البيانات التي ذكرتها إلى جدول ourSubject
subject_data = [
    ('Math', 'Mina Ibrahim'),
    ('Math', 'Saad Hegazy'),
    ('Arabic', 'Mohammed Hafez'),
    ('English', 'Jana Mahrous'),
    ('English', 'Amira Eid'),
    ('Social Studies', 'Ahmed Gamal'),
    ('Social Studies', 'Yasser Mohammed'),
    ('Science', 'Karima Atef'),
    ('Science', 'Mohammed Maged')
]

try:
    cursor.executemany(
        "INSERT INTO ourSubject (subjectName, TeacherName) VALUES (?, ?)",
        subject_data
    )
    con.commit()
    print("Data added successfully to 'ourSubject' table!")
except sqlite3.Error as e:
    print(f"Error occurred: {e}")

# دالة تسجيل الدورة
def subjectRegistration():
    subject_name = name_var.get()  # الحصول على اسم المادة
    teacher_name = Add_var.get()  # الحصول على اسم المعلم
    
    # التحقق من ملء الحقول
    if not (subject_name and teacher_name):
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    try:
        # إدخال البيانات في جدول ourSubject
        cursor.execute(
            "INSERT INTO ourSubject (subjectName, TeacherName) VALUES (?, ?)",
            (subject_name, teacher_name)
        )
        con.commit()
        messagebox.showinfo("Success", "Subject Registered Successfully!")
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error occurred: {e}")

# إعداد نافذة التطبيق
win = tk.Tk()
win.title("Course Management")
win.geometry("600x700")
win.resizable(0, 0)
win.configure(background="grey")

# إعداد الخطوط
labelfont = ('times', 20, 'bold')
labelfont1 = ('times', 15, 'bold')
labelfont2 = ('times', 18, 'bold')

# العنوان الرئيسي
ttk.Label(
    win, text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n", font=labelfont2, background="blue", foreground="white"
).pack()

# عنوان إدارة الدورات
ttk.Label(
    win, text="\nschool Management\n", font=labelfont1, background="grey", foreground="white"
).pack()

# إدخال اسم المادة
ttk.Label(win, text="subject Name:", font=labelfont2, background="grey", foreground="white").pack()
name_var = tk.StringVar()
tk.Entry(win, textvariable=name_var, font=labelfont1, width=30).pack()

# إدخال اسم المعلم
ttk.Label(win, text="Teacher Name:", font=labelfont2, background="grey", foreground="white").pack()
Add_var = tk.StringVar()
tk.Entry(win, textvariable=Add_var, font=labelfont1, width=30).pack()

# زر التسجيل
myFont = font.Font(size=15)
tk.Button(win, text="Register", command=subjectRegistration, font=myFont, width=15).pack(pady=10)

# تشغيل النافذة
win.mainloop()

# إغلاق الاتصال بعد الانتهاء من العمليات
con.close()