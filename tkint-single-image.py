#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import tkinter.filedialog as filedialog
#import tkFileDialog
import cv2


def select_image():
    global panelA #, panelB

    ####
    path=filedialog.askopenfilename()

    #cap=cv2.VideoCapture(path)


    image=cv2.imread(path)
        
    image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    image=Image.fromarray(image)
        
    image=ImageTk.PhotoImage(image)


    if panelA is None:
        panelA=Label(image=image)
        panelA.image=image
        
        panelA.pack(side="left",padx=10,pady=10)

     
    else:
        panelA.configure(image=image)
        
        panelA.image=image
       


root=Tk()
panelA=None

btn=Button(root,text="Select",command=select_image)
btn.pack(side="bottom",fill="both",expand="yes",padx=10,pady=10)

root.mainloop()








