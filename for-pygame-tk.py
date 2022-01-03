#!/usr/bin/env python3

import pygame
import tkinter as tk
import os

root=tk.Tk()
embed=tk.Frame(root,width=500,height=500)
embed.grid(columnspan=600,rowspan=500)
embed.pack(side="left")

#buttonwin=tk.Frame(root,width=75,height=500)
#buttonwin.pack(side="left")

screen=pygame.display.set_mode((500,500))
screen.fill(pygame.Color(0,255,255))
pygame.display.init()
pygame.display.update()

def draw():
    pygame.draw.circle(screen,(0,0,0),(250,250),125)
    pygame.display.update()

    button1=tk.Button(buttonwin,text="Draw",command=draw)
    button1.pack(side="left")
    #canvas.update()
    root.update()

while True:
    pygame.display.update()
    root.update()    

















