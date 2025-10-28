import tkinter as tk
from tkinter import messagebox
import re

users = {}

def register():
    name = reg_name.get()
    email = reg_email.get()
    pwd = reg_pass.get()
    cpwd = reg_cpass.get()
    phone = reg_phone.get()

    if not all([name, email, pwd, cpwd, phone]):
        return messagebox.showerror("Error", "All fields are required!")

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return messagebox.showerror("Error", "Invalid Email!")

    if pwd != cpwd:
        return messagebox.showerror("Error", "Passwords do not match!")

    if not phone.isdigit() or len(phone) != 10:
        return messagebox.showerror("Error", "Invalid Phone Number!")

    users[email] = {"name": name, "password": pwd, "phone": phone}
    messagebox.showinfo("Success", "Registration Successful!")
    show_login()

def login():
    email = login_email.get()
    pwd = login_pass.get()

    if email in users and users[email]["password"] == pwd:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Invalid Credentials!")

def show_register():
    frame_login.pack_forget()
    frame_reg.pack()

def show_login():
    frame_reg.pack_forget()
    frame_login.pack()

root = tk.Tk()
root.title("Hostel Management System")
root.geometry("350x400")

# -------- Register Page --------
frame_reg = tk.Frame(root)

tk.Label(frame_reg, text="Register", font=("Arial", 18, "bold")).pack(pady=10)
reg_name = tk.Entry(frame_reg); tk.Label(frame_reg, text="Full Name").pack(); reg_name.pack()
reg_email = tk.Entry(frame_reg); tk.Label(frame_reg, text="Email").pack(); reg_email.pack()
reg_pass = tk.Entry(frame_reg, show="*"); tk.Label(frame_reg, text="Password").pack(); reg_pass.pack()
reg_cpass = tk.Entry(frame_reg, show="*"); tk.Label(frame_reg, text="Confirm Password").pack(); reg_cpass.pack()
reg_phone = tk.Entry(frame_reg); tk.Label(frame_reg, text="Phone Number").pack(); reg_phone.pack()

tk.Button(frame_reg, text="Register", command=register).pack(pady=10)
tk.Button(frame_reg, text="Already have an account? Login", command=show_login).pack()

# -------- Login Page --------
frame_login = tk.Frame(root)

tk.Label(frame_login, text="Login", font=("Arial", 18, "bold")).pack(pady=10)
login_email = tk.Entry(frame_login); tk.Label(frame_login, text="Email").pack(); login_email.pack()
login_pass = tk.Entry(frame_login, show="*"); tk.Label(frame_login, text="Password").pack(); login_pass.pack()

tk.Button(frame_login, text="Login", command=login).pack(pady=10)
tk.Button(frame_login, text="Create new account", command=show_register).pack()

frame_login.pack()

root.mainloop()
