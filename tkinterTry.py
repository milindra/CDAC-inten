from Tkinter import *

master = Tk()
b=Button(master,text="click");
w = Spinbox(master, from_=1, to=36)
w.pack()
b.pack()

def print_it(event):
    print var.get()

var = StringVar()
var.set("x")
OptionMenu(master, var, "a","b","c", command=print_it).pack()

mainloop()
