import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import os 
import shutil 
import config

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

form = tk.Tk()
form.title("Database")
form.geometry("500x280")
tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text="All Entries")
tab_parent.add(tab2, text="Add New Entry")

###TAB ONE STUFF
firstLabelTabOne = tk.Label(tab1, text="First Name:", font="times 14")
familyLabelTabOne = tk.Label(tab1, text="Family Name:", font="times 14")
jobLabelTabOne = tk.Label(tab1, text="Job Title:", font="times 14")
firstEntryTabOne = tk.Entry(tab1, font="times 12")
familyEntryTabOne = tk.Entry(tab1, font="times 12")
jobEntryTabOne = tk.Entry(tab1, font="times 12")
openImageTabOne = Image.open(path)
imgTabOne = ImageTk.PhotoImage(openImageTabOne)
imgLabelTabOne = tk.Label(tab1,image=imgTabOne)
buttonForward = tk.Button(tab1, text="==> Next ==>", font="times 14")
buttonBack = tk.Button(tab1, text="<== Prev <==", font="times 14")
###Grid placements
firstLabelTabOne.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabOne.grid(row=0, column=1, padx=15, pady=15)
familyLabelTabOne.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabOne.grid(row=1, column=1, padx=15, pady=15)
jobLabelTabOne.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabOne.grid(row=2, column=1, padx=15, pady=15)
imgLabelTabOne.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
buttonBack.grid(row=3, column=0, padx=15, pady=15)
buttonForward.grid(row=3, column=2, padx=15, pady=15)

###SECOND TAB STUFF
firstLabelTabTwo = tk.Label(tab2, text="First Name:", font="times 14")
familyLabelTabTwo = tk.Label(tab2, text="Family Name:", font="times 14")
jobLabelTabTwo = tk.Label(tab2, text="Job Title:", font="times 14")
firstEntryTabTwo = tk.Entry(tab2, font="times 12")
familyEntryTabTwo = tk.Entry(tab2, font="times 12")
jobEntryTabTwo = tk.Entry(tab2, font="times 12")
imgLabelTabTwo = tk.Label(tab2, font="times 12")
buttonCommit = tk.Button(tab2, text="Submit", font="times 14")
buttonAddImage = tk.Button(tab2, text="Add Image", font="times 14")
###GRID PLACEMENTS
firstLabelTabTwo.grid(row=0, column=0, padx=15, pady=15)
firstEntryTabTwo.grid(row=0, column=1, padx=15, pady=15)
imgLabelTabTwo.grid(row=0, column=2, rowspan=3, padx=15, pady=15)
familyLabelTabTwo.grid(row=1, column=0, padx=15, pady=15)
familyEntryTabTwo.grid(row=1, column=1, padx=15, pady=15)
jobLabelTabTwo.grid(row=2, column=0, padx=15, pady=15)
jobEntryTabTwo.grid(row=2, column=1, padx=15, pady=15)
buttonCommit.grid(row=4, column=0, padx=15, pady=15)
buttonAddImage.grid(row=4, column=2, padx=15, pady=15)

tab_parent.pack(expand=1, fill='both')

form.mainloop()