#!/usr/bin/env python3

import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import numpy as np

video_name="test.mp4"
video=imageio.get_reader(video_name)
#video.resize((650,250))

def stream(label):

    for image in video.iter_data():
        #print(image)
        #img = Image.fromarray(image, 'RGB')
        #image=img.resize((650,250))
        img=Image.fromarray(image)
 
 
        #img.resize((100, 100))
        #img = np.resize(img, (128, 128))

        frame_image=ImageTk.PhotoImage(img)
        #frame_image.zoom(650,250)
        #frame_image._PhotoImage__size=(650,250)
        #frame_image.height=250
        #frame_image.width=650
        label.config(image=frame_image) #, width=650,height=250)
        label.image=frame_image

if __name__ =="__main__":

    root=tk.Tk()
    #tk.Frame(root,width=500,height=500)
    root.geometry("650x250")
    #root.resizable(height = 50, width = 50)
    #screen_width = root.winfo_screenwidth()
    #screen_height = root.winfo_screenheight()
    my_label=tk.Label(root)
    my_label.pack()
    thread=threading.Thread(target=stream,args=(my_label,))        
    thread.daemon=1
    thread.start()
    
    root.mainloop()