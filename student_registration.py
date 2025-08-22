import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font

def start(win1):
    # Connect to SQLite database (it will create the file if not exists)
    con = sqlite3.connect('school_management.db')
    cursor = con.cursor()

    cursor.execute("DROP TABLE IF EXISTS student")
    # Create student table if not exists
    cursor.execute('''  
    CREATE TABLE IF NOT EXISTS student (
        Rollno INTEGER PRIMARY KEY AUTOINCREMENT,
        studentname TEXT,
        password TEXT,
        grade TEXT,
        Class TEXT,
        sub1 TEXT,
        sub2 TEXT,
        sub3 TEXT,
        sub4 TEXT,
        sub5 TEXT,
        sub1mark INT DEFAULT 0,
        sub2mark INT DEFAULT 0,
        sub3mark INT DEFAULT 0,
        sub4mark INT DEFAULT 0,
        sub5mark INT DEFAULT 0
    );
    ''')

    # Define lists of names, grades, classes, and subjects
    grades = ["A", "B", "C"]
    classes = ["1", "2", "3"]
    subjects = ["Math", "Science", "English", "History", "Geography"]

    # Tkinter window setup
    win = tk.Toplevel(win1)
    win.title("Student Management")
    win.geometry("700x800")
    win.resizable(0, 0)
    win.configure(background="grey")

    # Fonts
    labelfont = ('times', 20, 'bold')
    labelfont1 = ('times', 15, 'bold')
    labelfont2 = ('times', 18, 'bold')
    myFont = font.Font(size=15)

    # Header
    head = ttk.Label(win, text="\n\tSCHOOL MANAGEMENT SYSTEM\t\n")
    head.pack()
    head.configure(background="blue", width="200")
    head.config(font=labelfont2)

    # Section labels
    teacher_man = ttk.Label(win, text="\nStudent Management\n")
    teacher_man.pack()
    teacher_man.configure(background="grey")
    teacher_man.config(font=labelfont1)

    # Student Registration Section
    lab2 = ttk.Label(win, text="Student Name")
    lab2.pack()
    lab2.configure(background="grey")
    lab2.config(font=labelfont2)

    name_var = tk.StringVar()
    name_ent = ttk.Entry(win, width=30, textvariable=name_var)
    name_ent.pack()
    name_ent.config(font=labelfont1)

    lab2 = ttk.Label(win, text="Password")
    lab2.pack()
    lab2.configure(background="grey")
    lab2.config(font=labelfont2)

    pass_var = tk.StringVar()
    pass_ent = ttk.Entry(win, width=30, textvariable=pass_var, show='*')
    pass_ent.pack()
    pass_ent.config(font=labelfont1)

    lab3 = ttk.Label(win, text="Grade")
    lab3.pack()
    lab3.configure(background="grey")
    lab3.config(font=labelfont2)

    Add_var = ttk.Combobox(win, state='readonly', values=grades, width=30, textvariable=tk.StringVar())
    Add_var.pack()
    Add_var.config(font=labelfont1)

    lab4 = ttk.Label(win, text="Class")
    lab4.pack()
    lab4.configure(background="grey")
    lab4.config(font=labelfont2)

    Add1_var = ttk.Combobox(win, state='readonly', values=classes, width=30, textvariable=tk.StringVar())
    Add1_var.pack()
    Add1_var.config(font=labelfont1)

    lab5 = ttk.Label(win, text="Subjects")
    lab5.pack()
    lab5.configure(background="grey")
    lab5.config(font=labelfont2)

    Add2_var = tk.StringVar()
    Add2_ent = ttk.Combobox(win, state='readonly', values=subjects, width = 30, textvariable=Add2_var)
    Add2_ent.pack()
    Add2_ent.config(font=labelfont1)

    Add3_var = tk.StringVar()
    Add3_ent = ttk.Combobox(win, state='readonly', values=subjects, width = 30, textvariable=Add3_var)
    Add3_ent.pack()
    Add3_ent.config(font=labelfont1)

    Add4_var = tk.StringVar()
    Add4_ent = ttk.Combobox(win, state='readonly', values=subjects, width = 30, textvariable=Add4_var)
    Add4_ent.pack()
    Add4_ent.config(font=labelfont1)

    Add5_var = tk.StringVar()
    Add5_ent = ttk.Combobox(win, state='readonly', values=subjects, width = 30, textvariable=Add5_var)
    Add5_ent.pack()
    Add5_ent.config(font=labelfont1)

    Add6_var = tk.StringVar()
    Add6_ent = ttk.Combobox(win, state='readonly', values=subjects, width = 30, textvariable=Add6_var)
    Add6_ent.pack()
    Add6_ent.config(font=labelfont1)

    # Function to handle student registration
    def courseRegistration():
        # Get values from the input fields
        b = name_var.get()  # Student Name
        password = pass_var.get()
        c = Add_var.get()  # Grade
        d = Add1_var.get()  # Class
        e = Add2_var.get()  # Subject 1
        f = Add3_var.get()  # Subject 2
        g = Add4_var.get()  # Subject 3
        h = Add5_var.get()  # Subject 4
        i = Add6_var.get()  # Subject 5



        # Verify that all fields are filled
        if not all([b, password, c, d, e, f, g, h, i]):
            messagebox.showerror("Input Error", "All fields must be filled")
            return

        cursor.execute("SELECT studentname FROM student WHERE studentname=?", (b,))
        result = cursor.fetchone()
        con.commit()
        if result:
            print("student exists")
            messagebox.showerror("Input Error", "Student already registered")
            return
        if len(password) < 5:
            messagebox.showerror("Input Error", "Password must be at least 4 characters long")
            return

        arr = [e, f, g, h, i]
        for i in range(0, len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]==arr[j]:
                    messagebox.showerror("Input Error", "Fix repeated subjects")
                    return
        # Insert data into the student table
        cursor.execute("INSERT INTO student (studentname, password, grade, Class, sub1, sub2, sub3, sub4, sub5, sub1mark, sub2mark, sub3mark, sub4mark, sub5mark) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 0,0,0,0,0)",
                    (b, password, c, d, e, f, g, h, i))
        con.commit()
        
        messagebox.showinfo("Information", "Data added successfully!")

    # Function to delete all student records from the student table
    def delete_all_student_data():
        try:
            cursor.execute("DELETE FROM student")  # Delete all records from the student table
            con.commit()  # Commit the changes to the database
            messagebox.showinfo("Success", "All student records have been deleted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # Register button
    sub_butt = tk.Button(win, text="Register", command=courseRegistration)
    sub_butt['font'] = myFont
    sub_butt.pack(pady=10)
    sub_butt.configure(width="15")

    # Add a button to delete all student records
    delete_all_button = tk.Button(win, text="Delete All Student Data", command=delete_all_student_data)
    delete_all_button['font'] = myFont
    delete_all_button.pack(pady=10)
    delete_all_button.configure(width="25")

    # Run the main loop
    win.mainloop()

if __name__ == "__main__":
    start(tk.Tk())