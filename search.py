import sqlite3
import tkinter as tk
from tkinter import messagebox

subject_index = 0


def start(win, subject: str):
    conn = sqlite3.connect('school_management.db')
    cursor = conn.cursor()
    
    student_name = ''
    
    def search_student():
        global subject_index
        student_name = entry_name.get()
        cursor.execute("SELECT * FROM student WHERE studentname LIKE ?", ('%' + student_name + '%',))
        student = cursor.fetchone()
        if not student:
            return
        
        student_name = student[1]
        for i in range(0, len(student)):
            if type(student[i]) == str:
                if student[i].lower() == subject.lower():
                    subject_index = i

        if student:
            # Populate fields with student data
            label_rollno.config(text=f"Roll No: {student[0]}")
            label_class.config(text=f"Class: {student[5]}")
            label_sub1.config(text=f"{student[subject_index]} Marks: {student[subject_index + 5]}")
            print(subject_index)
            
            # Enable the update grade button
            button_update_grade.config(state=tk.NORMAL)
        else:
            messagebox.showinfo("Not Found", "Student not found")

    # Function to update the grade
    def update_grade():
        global subject_index
        new_grade = entry_grade.get()
        if not new_grade:
            messagebox.showinfo("Error", "Please enter a new grade")
            return
        
        # Mapping subject index to corresponding column in the database
        subject_column_mapping = {
            5: "sub1mark",
            6: "sub2mark",
            7: "sub3mark",
            8: "sub4mark",
            9: "sub5mark"
        }
        
        # Make sure subject_index corresponds to a valid subject
        if subject_index not in subject_column_mapping:
            messagebox.showinfo("Error", "Invalid subject index")
            return
    
        subject_column = subject_column_mapping[subject_index]

        with sqlite3.connect('school_management.db') as con:
            cursor2 = con.cursor()
        # Update the grade in the correct subject column
            sql = f"UPDATE student SET {subject_column} = ? WHERE studentname = ?"
            
            print(f"Executing SQL: {sql}")
            cursor2.execute(sql, (new_grade, student_name))
            conn.commit()
            messagebox.showinfo("Success", "Grade updated successfully")
            conn.close()

    # Tkinter window setup
    window = tk.Tk()
    window.title("Search and Update Student Grade")
    window.geometry("400x400")

    # Search Section
    label_name = tk.Label(window, text="Enter Student Name:")
    label_name.pack()

    entry_name = tk.Entry(window)
    entry_name.pack()

    button_search = tk.Button(window, text="Search", command=search_student)
    button_search.pack()

    # Display student details
    label_rollno = tk.Label(window, text="Roll No:")
    label_rollno.pack()

    label_class = tk.Label(window, text="Class:")
    label_class.pack()

    label_sub1 = tk.Label(window, text="Subject 1:")
    label_sub1.pack()

    # Grade update section
    label_update_grade = tk.Label(window, text="Enter New Grade:")
    label_update_grade.pack()

    entry_grade = tk.Entry(window)
    entry_grade.pack()

    button_update_grade = tk.Button(window, text="Update Grade", command=update_grade, state=tk.DISABLED)
    button_update_grade.pack()

    # Run the window
    window.mainloop()

    # Close database connection when the window is closed
    conn.close()

start(tk.Tk(), "History")
