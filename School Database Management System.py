import tkinter as tk
from tkinter import ttk, messagebox

def addstudent():
    name = name_var.get()
    age = age_var.get()
    grade = grade_var.get()

    if not name or not age or not grade:
        messagebox.showerror(title='Error', message='All the fields must be filled!')
        return

    tree_view.insert("", tk.END, values=(name, age, grade))
    messagebox.showinfo(title='Success', message='All the fields are stored!')
    clear()

# Function to clear input fields
def clear():
    name_var.set("")
    age_var.set("")
    grade_var.set("")

# Function to delete student
def deletestudent():
    selected_item = tree_view.selection()
    if not selected_item:
        messagebox.showerror(title='Error', message='Please select any student details!')
        return
    tree_view.delete(selected_item)
    messagebox.showinfo(title='Delete', message='Successfully deleted!')

# Main window
root = tk.Tk()
root.config(bg='purple')
root.title('Student Management')
root.geometry('500x500')

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
grade_var = tk.StringVar()

# Labels and Entries
tk.Label(root, text='Name', font=('arial', 20), bg='purple', fg='white').grid(row=0, column=0, padx=20, pady=20)
tk.Entry(root, textvariable=name_var, font=('arial', 20)).grid(row=0, column=1, padx=20, pady=20)

tk.Label(root, text='Age', font=('arial', 20), bg='purple', fg='white').grid(row=1, column=0, padx=20, pady=20)
tk.Entry(root, textvariable=age_var, font=('arial', 20)).grid(row=1, column=1, padx=20, pady=20)

tk.Label(root, text='Grade', font=('arial', 20), bg='purple', fg='white').grid(row=2, column=0, padx=20, pady=20)
tk.Entry(root, textvariable=grade_var, font=('arial', 20)).grid(row=2, column=1, padx=20, pady=20)

# Buttons
tk.Button(root, text='Add Student', font=('arial', 20), command=addstudent).grid(row=3, column=0, padx=20, pady=20)
tk.Button(root, text='Delete Student', font=('arial', 20), command=deletestudent).grid(row=3, column=1, padx=20, pady=20)

# Treeview table
columns = ('Name', 'Age', 'Grade')
tree_view = ttk.Treeview(root, columns=columns, show='headings')

for col in columns:
    tree_view.heading(col, text=col)
    tree_view.column(col, width=100)

tree_view.grid(row=4, column=0, padx=20, pady=20, columnspan=2)

root.mainloop()
