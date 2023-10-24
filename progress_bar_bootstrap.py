from tkinter import  *

from  ttkbootstrap import *
#from ttkbootstrap.constants import *




root = Window(themename="solar")
b = IntVar()

progress = IntVar()
a = IntVar()
b = IntVar()
#root = ThemedTk(theme='adapta')
#root = ThemedTk(theme="arc")



def option_selected(event):
    progress.set(5)
    a = comb1.get()
    if a == "Option 1":
        progress.set(10)
        b.set(10)
    elif a == "Option 2":
        progress.set(10 + b.get())


root.title("Progress Bar")
root.minsize(200, 200)


progressbar = Progressbar(root, orient=HORIZONTAL, length=100,
                          variable=progress,
                          bootstyle='danger')
progressbar.pack()
#progressbar.step(75)
#progress.set(25)

label = Label(root, text='My Progress Bar')
label.pack(padx=5, pady=5)
sep = Separator(root, bootstyle="info")
sep.pack(fill=X)
values = ['Selecciona', 'Option 1', 'Option 2', 'Option 3']
comb1 = Combobox(root, values=values)
comb1.current(0)
comb1.pack()
comb1.bind("<<ComboboxSelected>>", option_selected)
bt1 = Button(root, text="Accept", bootstyle='success-outline')
bt1.pack(padx=5, pady=5)
bt2 = Button(root, text="Cancel", command=root.destroy, bootstyle='danger-outline')
bt2.pack(padx=5, pady=5)

root.mainloop()


