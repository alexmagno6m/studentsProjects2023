from ttkbootstrap import *

root = Window(themename="vapor")





root.minsize(width=300, height=300)
frame1 = Frame(root, style="info", height=150)
frame1.pack(padx=15, pady=10)
e1 = Entry(frame1, style="info")
e1.pack(padx=10, pady=10)


frame2 = Frame(root, style="info", height=150)
frame2.pack(padx=15, pady= 10)
e2 = Entry(frame2, style="info")
e2.pack(padx=10, pady=10)



root.mainloop()