#!/usr/bin/env python3

import tkinter as Tk

root= Tk()

#C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

Tk.canvas.create_oval(10, 50, 240, 210, width = 0, fill = 'white')

#coord = 10, 50, 240, 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")

#C.pack()
root.mainloop()