from tkinter import *
from tkinter.ttk import *

root = Tk()
root.minsize(width=400, height=400)


frame1 = Frame(root)
frame1.pack()


eti1 = Label(frame1, text="Usuario")
eti1.grid(column=0, row=0, padx=5, pady=5, sticky="nsew")

root.mainloop()