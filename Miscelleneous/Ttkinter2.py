from tkinter import *
root = Tk()
root.geometry("500x500")

fa = Frame(bg="red", borderwidth=20, relief=SUNKEN)
fa.pack(fill="x")
fb = Frame(bg="green", borderwidth=10, relief=SUNKEN)
fb.pack(side="left", fill="y")
fc = Frame( bg="blue")
fc.pack(side="right",fill="y")
fd = Frame(bg="yellow", borderwidth=20)
fd.pack(side="bottom", fill="x")
a = Label( fa, text="HELLO  TOP")
b = Label( fb, text="HELLO  LEFT")
c = Label( fc, text="HELLO  RIGHT")
d = Label( fd, text="HELLO BOTTOM")
a.pack(side= "top"),b.pack(side = "left"), c.pack(side="right"), d.pack(side="bottom")

root.mainloop()