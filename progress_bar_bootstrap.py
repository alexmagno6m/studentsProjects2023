from tkinter import  *

from  ttkbootstrap import *
#from ttkbootstrap.constants import *

root = Window(themename="solar")
#root = ThemedTk(theme='adapta')
#root = ThemedTk(theme="arc")
progress = IntVar()

root.title("Progress Bar")
root.minsize(200, 200)



progressbar = Progressbar(root, orient=HORIZONTAL, length=100,
                          variable=progress,
                          bootstyle='danger')
progressbar.pack()
#progressbar.step(75)
progress.set(90)

label = Label(root, text='My Progress Bar')
label.pack(padx=5, pady=5)
sep = Separator(root, bootstyle="info")
sep.pack(fill=X)
bt1 = Button(root, text="Accept", bootstyle='success-outline')
bt1.pack(padx=5, pady=5)
bt2 = Button(root, text="Cancel", command=root.destroy, bootstyle='danger-outline')
bt2.pack(padx=5, pady=5)


root.mainloop()


