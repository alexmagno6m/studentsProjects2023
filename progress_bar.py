from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

root = ThemedTk()
#root = ThemedTk(theme='adapta')
#root = ThemedTk(theme="arc")
progress = IntVar()

root.title("Progress Bar")
root.minsize(200, 200)
style = Style()
style.theme_use('arc')
style.configure(style='TLabel', font=('Arial', 14))
style.configure('TProgressbar')

progressbar = Progressbar(root, orient=HORIZONTAL, length=100,
                          variable=progress,
                          style='TProgressbar')
progressbar.pack()
#progressbar.step(75)
progress.set(90)

label = Label(root, text='My Progress Bar', style='TLabel')
label.pack()



root.mainloop()


