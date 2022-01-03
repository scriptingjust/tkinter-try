#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
#import tkFileDialog
import cv2


def select_image():
    global panelA, panelB

    ####
    path=filedialog.askopenfilename()

    if len(path) >0:
        image=cv2.imread(path)
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        edged=cv2.Canny(gray,50,100)

        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

        image=Image.fromarray(image)
        edged=Image.fromarray(edged)

        #ImageTk format what about video

        image=ImageTk.PhotoImage(image)
        edged=ImageTk.PhotoImage(edged)

    if panelA is None or panelB is None:

        panelA=Label(image=image)
        panelA.image=image
        #position of pic/video
        panelA.pack(side="left",padx=10,pady=10)

        panelB=Label(image=edged)
        panelB.image=edged
        panelB.pack(side="right",padx=10,pady=10)


        #updating panels
    else:
        panelA.configure(image=image)
        panelB.configure(image=edged)
        panelA.image=image
        panelB.image=edged


root=Tk()
panelA=None
panelB=None

btn=Button(root,text="Select",command=select_image)
btn.pack(side="bottom",fill="both",expand="yes",padx=10,pady=10)

root.mainloop()








