from tkinter import *


root = Tk()
var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
def funcion1():
    w2 = Toplevel(root)
    l1 = Label(w2, text=var1.get())
    l1.pack()
    boton2 = Button(w2, text="Ventana 2", command=ventana2)
    boton2.pack()
    w2.mainloop()
def ventana2():
    w3 = Toplevel(root)
    w3.mainloop(())



bot = Button(root, text='Aceptar', command=funcion1)
bot.pack()
ent1 = Entry(root, textvariable=var1)
ent1.pack()
ent1 = Entry(root, textvariable=var2)
ent1.pack()
ent1 = Entry(root, textvariable=var3)
ent1.pack()
root.mainloop()