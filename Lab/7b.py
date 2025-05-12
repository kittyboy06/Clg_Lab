import tkinter as tk
from tkinter import messagebox
def submit_form():
    username = entry_username.get()
    password = entry_password.get()
    messagebox.showinfo("Registration Successful",f"welcomme,{username}")
root = tk.Tk();
root.title("Registration Form")

label_username = tk.Label(root,text="Username")
label_username.grid(row=0,column=0,padx=10,pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0,column=1,padx=10,pady=10)
label_password = tk.Label(root,text="Password")
label_password.grid(row=1,column=0,padx=10,pady=10)
entry_password = tk.Entry(root,show="")
entry_password.grid(row=1,column=1,padx=10,pady=10)
submit_button = tk.Button(root,text="Submit",command=submit_form)
submit_button.grid(row=2,column=0,columnspan=2,pady=10)
root.mainloop()

