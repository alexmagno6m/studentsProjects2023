from tkinter import *

ruta = 'datos.txt'

opendata = open(ruta, 'r')

root = Tk()
var = StringVar()
def run():
    reg = open(ruta, 'a')
    reg.write(var.get())


entr1 = Entry(root, textvariable=var)
entr1.pack()
boton1 = Button(root, text="Aceptar", command=run)
boton1.pack()

root.mainloop()

print(var.get())