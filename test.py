import tkinter as tk
from tkinter import filedialog
import os
import move

root = tk.Tk()
root.minsize(500,250)
root.title("File Manager")

title = tk.Label(root,text='Select Your Directory to Manage',font=("Arial",14))
title.place(relx=0.5,rely = 0.1,anchor = 'n')

defaulttext = tk.StringVar() 
defaulttext.set(os.getcwd()) 

inputdir = tk.Entry(root,width=40,font=("Arial",12),textvariable=defaulttext)
inputdir.place(relx = 0.05,rely=0.55,anchor= "w")

Managebutton = tk.Button(root,text = "Mange", width= 10)
Managebutton.place(relx = 0.95,rely=0.85,anchor= 'e')

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
        inputdir.delete(0,"end")
        inputdir.insert(tk.END,tempdir)

browsebutton = tk.Button(root,text = "Browse", width= 10,command=search_for_file_path)
browsebutton.place(relx = 0.95,rely=0.55,anchor= 'e')

move.filepath=inputdir.get()




root.mainloop()