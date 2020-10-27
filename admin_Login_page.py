from tkinter import *
from typing import Pattern
from PIL import ImageTk
from tkinter import messagebox

class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("720x630+250+10")
        self.root.resizable(False,False)
        self.bg=ImageTk.PhotoImage(file="images/pg_2.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        lbl_user=Label(self.root,text="ADMIN LOGIN",font=("Supra Mezzo Medium",25,"bold"),fg="white",bg="#00B1AB").place(x=250,y=52)
        self.txt_user=Entry(self.root,font=("Supra Mezzo Medium",15,"bold"),bg="white")
        self.txt_user.place(x=210,y=162,width=400,height=66)

        self.txt_pass=Entry(self.root,font=("Supra Mezzo Medium",15,"bold"),bg="white")
        self.txt_pass.place(x=210,y=271,width=400,height=66)

        Login_btn=Button(self.root,command=self.login_function,text="LOGIN",fg="#00B1AB",bd=0,bg="white",font=("Supra Mezzo Medium",20,"bold")).place(x=209,y=393.25,width=400,height=66)
        forget_btn=Button(self.root,text="Forget Password?",bg="#00B1AB",bd=0,fg="#01827A",font=("Supra Mezzo Medium",15,"bold")).place(x=270,y=510)

    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="1234" or self.txt_user.get()!="user":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}",parent=self.root)        





root=Tk()
obj=login(root)
root.mainloop()



