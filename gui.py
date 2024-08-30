import tkinter as tk
from tkinter import messagebox
def myfun():
    name=entername.get()
    password=enterpass.get()
    print(f"name:{name}")
    print(f"password:{password}")
root=tk.Tk()
root.title("user form")
root.geometry("500x300")

labelname=tk.Label(root,text="Name")
labelname.pack(pady=5)
entername=tk.Entry(root)
entername.pack(pady=5)
labelpass=tk.Label(root,text="Password")
labelpass.pack(pady=5)
enterpass=tk.Entry(root,show="*")
enterpass.pack(pady=5)

submit=tk.Button(root,text="submit",command=myfun)
submit.pack(pady=5)
root.mainloop()
