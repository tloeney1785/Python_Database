import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from PIL import ImageTk, Image
import pymysql
import os 
import shutil 
import config

file_name = "default.png"
path = config.PHOTO_DIRECTORY + file_name
rows = None
num_of_rows = None
row_counter = 0

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

def load_database_results():
    
    global rows
    global num_of_rows
    try:
        con = pymysql.connect(host=config.DB_SERVER,
        user=config.DB_USER,
        password=config.DB_PASS,
        database=config.DB)
        sql = "SELECT * FROM tbl_users"
        cursor = con.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        num_of_rows = cursor.rowcount
        cursor.close()
        con.close()
        has_loaded_successfully = True

    except pymysql.InternalError as e:
        has_loaded_successfully = database_error(e)
    
    return has_loaded_successfully

def database_error(err):
    messagebox.showinfo("Error",err)
    return false

def image_path(file_path):
    open_image = Image.open(file_path)
    image = ImageTk.PhotoImage(open_image)
    return image

def load_photo_tab_one(file_path):
    image = image_path(file_path)
    imgLabelTabOne.configure(image=image)
    imgLabelTabOne.image = image

def scroll_forward():
    global row_counter
    global num_of_rows
    if row_counter >= (num_of_rows - 1):
        messagebox.showinfo("Database Error", "End of database")
    else:
        row_counter = row_counter + 1
        scroll_load_data()

def scroll_back():
    global row_counter
    if row_counter is 0:
        messagebox.showinfo("Database Error", "Start of database")
    else:
        row_counter = row_counter - 1
        scroll_load_data()

def scroll_load_data():
        fName.set(rows[row_counter][1])
        fam.set(rows[row_counter][2])
        job.set(rows[row_counter][3])
        try:
            ph_path = config.PHOTO_DIRECTORY + rows[row_counter][4]
            load_photo_tab_one(ph_path)
        except FileNotFoundError:
            load_photo_tab_one(config.PHOTO_DIRECTORY + "default.png")

form = tk.Tk()
form.title("Database")
form.geometry("500x280")
tab_parent = ttk.Notebook(form)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.bind("<<NotebookTabChanged>>", on_tab_selected)
tab_parent.add(tab1, text="All Entries")
tab_parent.add(tab2, text="Add New Entry")

fName = tk.StringVar()
fam = tk.StringVar()
job = tk.StringVar()

fNameTabTwo = tk.StringVar()
famTabTwo = tk.StringVar()
jobTabTwo = tk.StringVar()

###TAB ONE STUFF
firstLabelTabOne = tk.Label(tab1, text="First Name:", font="times 14")
familyLabelTabOne = tk.Label(tab1, text="Family Name:", font="times 14")
jobLabelTabOne = tk.Label(tab1, text="Job Title:", font="times 14")
firstEntryTabOne = tk.Entry(tab1, font="times 12", textvariable=fName)
familyEntryTabOne = tk.Entry(tab1, font="times 12",textvariable=fam)
jobEntryTabOne = tk.Entry(tab1, font="times 12",textvariable=job)
imgTabOne = image_path(path)
imgLabelTabOne = tk.Label(tab1, image=imgTabOne)
buttonForward = tk.Button(tab1, text="==> Next ==>", font="times 14", command=scroll_forward)
buttonBack = tk.Button(tab1, text="<== Prev <==", font="times 14", command=scroll_back)
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
firstEntryTabTwo = tk.Entry(tab2, font="times 12",textvariable=fNameTabTwo)
familyEntryTabTwo = tk.Entry(tab2, font="times 12",textvariable=famTabTwo)
jobEntryTabTwo = tk.Entry(tab2, font="times 12",textvariable=jobTabTwo)
imgTabTwo = image_path(path)
imgLabelTabTwo = tk.Label(tab2, image=imgTabTwo)
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

success = load_database_results()
if success:
    fName.set(rows[0][1])
    fam.set(rows[0][2])
    job.set(rows[0][3])
    photo_path = config.PHOTO_DIRECTORY + rows[0][4]
    load_photo_tab_one(photo_path)
tab_parent.pack(expand=1, fill='both')
form.mainloop()