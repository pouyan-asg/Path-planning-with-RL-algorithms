import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

pixels = 80   # pictures pixels
env_height = 4  # grid height
env_width = 12  # grid width
global_variable = {}  # for the final route coordination

root = Tk()

root.title('Cliff Walking - Sutton Book')
root.geometry(f'{env_width * pixels}x{env_height * pixels}+450+250')

canvas_widget = tk.Canvas(bg='white', height=env_height * pixels, width=env_width * pixels)
for column in range(0, env_width * pixels, pixels):
    x0, y0, x1, y1 = column, 0, column, env_height * pixels
    canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

for row in range(0, env_height * pixels, pixels):
    x0, y0, x1, y1 = 0, row, env_width * pixels, row
    canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

img_cliff = Image.open("images/cliff.png")
cliff_object = ImageTk.PhotoImage(img_cliff)

obstacle1 = canvas_widget.create_image(pixels, pixels * 3, anchor='nw',image=cliff_object)
obstacle2 = canvas_widget.create_image(pixels * 2, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle3 = canvas_widget.create_image(pixels * 3, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle4 = canvas_widget.create_image(pixels * 4, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle5 = canvas_widget.create_image(pixels * 5, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle6 = canvas_widget.create_image(pixels * 6, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle7 = canvas_widget.create_image(pixels * 7, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle8 = canvas_widget.create_image(pixels * 8, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle9 = canvas_widget.create_image(pixels * 9, pixels * 3, anchor='nw',
                                                 image=cliff_object)
obstacle10 = canvas_widget.create_image(pixels * 10, pixels * 3, anchor='nw',
                                                 image=cliff_object)

img_flag = Image.open("images/end.png")
flag_object = ImageTk.PhotoImage(img_flag)
flag = canvas_widget.create_image(pixels * 11, pixels * 3, anchor='nw', image=flag_object)

img_robot = Image.open("images/robot.png")
robot = ImageTk.PhotoImage(img_robot)
agent = canvas_widget.create_image(pixels * 0, pixels * 0, anchor='nw', image=robot)

img_start = Image.open("images/start.png")
start_object = ImageTk.PhotoImage(img_start)
start = canvas_widget.create_image(pixels * 0, pixels * 3, anchor='nw', image=start_object)

canvas_widget.pack()

root.mainloop()