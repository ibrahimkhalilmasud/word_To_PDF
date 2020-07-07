### Need to install pip install docx2pdf



import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo

from docx2pdf import convert

win = tk.Tk()
win.title("Word to PDF Converter")


def openFile():
    file = askopenfile (filetypes = [('Word Files', '*.docx')])
    convert(file.name,r'C:\Users\Ibrah\Documents\Python\converted.pdf')
    showinfo("Done","File Successfully Converted")

label = tk.Label(win,text = "choose File: ")
label.grid(row=0,column=0,padx=5,pady=5)

button = ttk.Button(win,text = "Select" , width = 30, command = openFile)
button.grid(row = 0, column = 1, padx = 5, pady = 5 )

win.mainloop()
