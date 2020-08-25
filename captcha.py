# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:25:24 2020

@author: Admin
"""


import random
from tkinter import *
from tkinter import messagebox

text="abcdefghijklmnopqrstuvwxyz0123456789"


def set_captcha():
    s=random.choices(text,k=6)
    Captcha.set("".join(s))


def check():
    if Captcha.get()==user_input.get():
        messagebox.showinfo("Success","Correct")
    else:
        messagebox.showerror("Error","Wrong")
        
    set_captcha()
    user_input.set("")
    
    
    

if __name__=="__main__":
    gui=Tk()
    gui.title("Captcha App")
    gui.geometry("300x100")
    Captcha=StringVar()
    user_input=StringVar()
    Label(gui,textvariable=Captcha,font="Arial 16 bold").pack()
    Entry(gui,textvariable=user_input,font="Arial 16 bold").pack()
    Button(gui,command=lambda:check(),text="Check",font="Arial 10").pack()
    
    
    set_captcha()
    gui.mainloop()
    
    