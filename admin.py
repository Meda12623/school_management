import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def start(win12):
    Ad_var = tk.StringVar()
    Adpass_var = tk.StringVar()

    # الاتصال بقاعدة البيانات
    try:
        con = sqlite3.connect('school_management.db')
        cursor = con.cursor()
        print("Database connected successfully")
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return

    # التطبيق الرئيسي
    win = tk.Toplevel(win12)

    def AdminLogin():
        username = Ad_var.get().strip()  # إزالة المسافات الزائدة
        password = Adpass_var.get().strip()  # إزالة المسافات الزائدة

        if not username or not password:
            messagebox.showerror("Error", "Kindly fill all fields")
            return

        print(f"Trying to login with Username: {username}, Password: {password}")  # طباعة البيانات المدخلة

        # تحقق من البيانات في قاعدة البيانات
        cursor.execute("SELECT * FROM Adlogin WHERE Username=? AND Adpass=?", (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", f"Welcome {username}")
            win.destroy()
            AdminPanel(username, result[1])  # مرر كلمة المرور القديمة هنا
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def AdminPanel(username, old_password):
        # نافذة لوحة التحكم
        win1 = tk.Tk()
        win1.geometry("600x500")
        win1.title("Admin Panel")
        win1.configure(background="grey")

        labelfont = ('times', 20, 'bold')

        ttk.Label(win1, text="SCHOOL MANAGEMENT SYSTEM", font=labelfont, background="blue", foreground="white").pack(pady=10)
        ttk.Label(win1, text=f"Welcome, {username}", font=labelfont, background="grey", foreground="white").pack(pady=10)

        # أزرار الخيارات المختلفة
        ttk.Button(win1, text="Student Details", width=30, command=lambda: show_student_details(win1)).pack(pady=5)
        ttk.Button(win1, text="Change Admin Password", width=30, command=lambda: change_password(win1, username, old_password)).pack(pady=5)
        ttk.Button(win1, text="Teacher Details", width=30, command=lambda: show_teacher_details(win1)).pack(pady=5)

        ttk.Button(win1, text="Logout", width=20, command=win1.destroy).pack(pady=20)
        win1.mainloop()

    def change_password(win1, username, old_password):
        # إنشاء نافذة جديدة لتغيير كلمة المرور
        student_window = tk.Toplevel(win1)
        student_window.geometry("300x200")
        student_window.title("New Password")
        ttk.Label(student_window, text="NEW PASSWORD", font=('times', 15), background="blue", foreground="white").pack(pady=10)
        
        new_pass = tk.StringVar()  # تعيين المتغير لكلمة المرور الجديدة
        ttk.Entry(student_window, textvariable=new_pass, font=('times', 15)).pack(pady=5)
        
        def submit_password():
            new_password = new_pass.get().strip()  # إزالة المسافات الزائدة

            # # التأكد من أن الحقل غير فارغ
            # if not new_password:
            #     messagebox.showerror("Input Error", "Please enter a password")
            #     return
            
            # التأكد من أن كلمة المرور الجديدة لا تساوي كلمة المرور القديمة
            if new_password == old_password:  # تأكد من أن كلمة المرور الجديدة ليست نفس القديمة
                messagebox.showerror("Error", "New password cannot be the same as the old password")
                return

            # تحديث كلمة المرور في قاعدة البيانات
            try:
                cursor.execute("UPDATE Adlogin SET Adpass=? WHERE Username=?", (new_password, username))
                con.commit()  # حفظ التغييرات في قاعدة البيانات
                messagebox.showinfo("Success", "Password Changed Successfully!")
                student_window.destroy()  # إغلاق نافذة تغيير كلمة المرور
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

        ttk.Button(student_window, text="Change", width=30, command=submit_password).pack(pady=5)

    def show_student_details(win1):
        # إنشاء نافذة جديدة لعرض بيانات الطلاب
        student_window = tk.Toplevel(win1)
        student_window.geometry("700x400")
        student_window.title("Student Details")

        # إنشاء Treeview لعرض بيانات الطلاب
        tree = ttk.Treeview(student_window, columns=("Rollno", "Name", "Password", "Grade", "Class", "Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"), show="headings")
        tree.heading("Rollno", text="Rollno")
        tree.heading("Name", text="Student Name")
        tree.heading("Password", text="Password")
        tree.heading("Grade", text="Grade")
        tree.heading("Class", text="Class")
        tree.heading("Subject 1", text="Subject 1")
        tree.heading("Subject 2", text="Subject 2")
        tree.heading("Subject 3", text="Subject 3")
        tree.heading("Subject 4", text="Subject 4")
        tree.heading("Subject 5", text="Subject 5")

        # استرجاع جميع الطلاب من الجدول 'student'
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()

        if not students:
            messagebox.showinfo("No Data", "No student data found in the database.")
            student_window.destroy()
            return

        # إدراج البيانات في الشجرة
        for student in students:
            tree.insert("", "end", values=(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8], student[9]))

        tree.pack(pady=20)

    def show_teacher_details(win1):
        # إنشاء نافذة جديدة لعرض بيانات المعلمين
        teacher_window = tk.Toplevel(win1)
        teacher_window.geometry("700x400")
        teacher_window.title("Teacher Details")

        # إنشاء Treeview لعرض بيانات المعلمين
        tree = ttk.Treeview(teacher_window, columns=("Email", "TeacherName", "Subject", "Password"), show="headings")
        tree.heading("Email", text="Email")
        tree.heading("TeacherName", text="Teacher Name")
        tree.heading("Subject", text="Subject")
        tree.heading("Password", text="Password")

        # استرجاع جميع المعلمين من الجدول 'Teachers'
        cursor.execute("SELECT * FROM Teachers")
        teachers = cursor.fetchall()

        if not teachers:
            messagebox.showinfo("No Data", "No teacher data found in the database.")
            teacher_window.destroy()
            return

        # إدراج البيانات في الشجرة
        for teacher in teachers:
            tree.insert("", "end", values=(teacher[0], teacher[1], teacher[2], teacher[3]))

        tree.pack(pady=20)

    # إعداد نافذة تسجيل الدخول
    win.title("Admin Login")
    win.geometry("600x500")
    win.resizable(0, 0)
    win.configure(background="grey")

    labelfont = ('times', 20, 'bold')

    ttk.Label(win, text="SCHOOL MANAGEMENT SYSTEM", font=labelfont, background="blue", foreground="white").pack(pady=10)
    ttk.Label(win, text="Admin Login", font=('times', 15, 'bold'), background="grey", foreground="white").pack(pady=10)

    ttk.Label(win, text="Admin Username", font=('times', 15, 'bold'), background="grey", foreground="white").pack(pady=5)
    ttk.Entry(win, textvariable=Ad_var, font=('times', 15)).pack(pady=5)

    ttk.Label(win, text="Admin Password", font=('times', 15, 'bold'), background="grey", foreground="white").pack(pady=5)
    ttk.Entry(win, textvariable=Adpass_var, show="*", font=('times', 15)).pack(pady=5)

    ttk.Button(win, text="Login", command=AdminLogin, width=20).pack(pady=20)

    win.mainloop()

if __name__ == "__main__":
    start(tk.Tk())
