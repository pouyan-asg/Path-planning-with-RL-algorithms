import numpy as np
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

pixels = 40   # pictures pixels
env_height = 15  # grid height
env_width = 15  # grid width
global_variable = {}  # for the final route coordination

root = Tk()

root.title('Path Planing with Reinforcement Learning')
root.geometry(f'{env_width * pixels}x{env_height * pixels}+600+250')

canvas_widget = Canvas(bg='white', height=env_height * pixels, width=env_width * pixels)
for column in range(0, env_width * pixels, pixels):
    x0, y0, x1, y1 = column, 0, column, env_height * pixels
    canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

for row in range(0, env_height * pixels, pixels):
    x0, y0, x1, y1 = 0, row, env_height * pixels, row
    canvas_widget.create_line(x0, y0, x1, y1, fill='grey')


img_obstacle = Image.open("images/obstacle.png")
obstacle_object = ImageTk.PhotoImage(img_obstacle)

img_tree = Image.open("images/tree.png")
tree_object = ImageTk.PhotoImage(img_tree)

img_shop = Image.open("images/boot_tree.png")
shop_object = ImageTk.PhotoImage(img_shop)

img_building = Image.open("images/building.png")
building_object = ImageTk.PhotoImage(img_building)

img_cube = Image.open("images/rubik.png")
cube_object = ImageTk.PhotoImage(img_cube)

img_garbage = Image.open("images/garbage.png")
garbage_object = ImageTk.PhotoImage(img_garbage)

obstacle1 = canvas_widget.create_image(pixels * 2, 0, anchor='nw', image= obstacle_object)
obstacle2 = canvas_widget.create_image(pixels * 9, 0, anchor='nw', image= tree_object)
obstacle3 = canvas_widget.create_image(pixels * 11, 0, anchor='nw', image= obstacle_object)
obstacle4 = canvas_widget.create_image(pixels * 14, 0, anchor='nw',image=shop_object)
obstacle5 = canvas_widget.create_image(pixels * 5, 0, anchor='nw', image=obstacle_object)
obstacle6 = canvas_widget.create_image(0, pixels, anchor='nw', image=building_object)
obstacle7 = canvas_widget.create_image(pixels * 7, pixels, anchor='nw',image=obstacle_object)
obstacle8 = canvas_widget.create_image(pixels * 9, pixels, anchor='nw',image=obstacle_object)
obstacle9 = canvas_widget.create_image(pixels * 13, pixels, anchor='nw',image=obstacle_object)
obstacle10 = canvas_widget.create_image(pixels * 3, pixels * 2, anchor='nw', image=tree_object)
obstacle11 = canvas_widget.create_image(pixels * 5, pixels * 2, anchor='nw',
                                                 image= obstacle_object)
obstacle12 = canvas_widget.create_image(pixels * 11, pixels * 2, anchor='nw',
                                                 image=obstacle_object)
obstacle13 = canvas_widget.create_image(pixels * 0, pixels * 3, anchor='nw',
                                                 image=building_object)
obstacle14 = canvas_widget.create_image(pixels * 2, pixels * 4, anchor='nw',
                                                 image=shop_object)
obstacle15 = canvas_widget.create_image(pixels * 8, pixels * 3, anchor='nw',
                                                 image=obstacle_object)
obstacle16 = canvas_widget.create_image(pixels * 9, pixels * 3, anchor='nw',
                                                 image=tree_object)
obstacle17 = canvas_widget.create_image(pixels * 14, pixels * 3, anchor='nw',
                                                 image=obstacle_object)
obstacle19 = canvas_widget.create_image(pixels * 5, pixels * 4, anchor='nw',
                                                 image=building_object)
obstacle20 = canvas_widget.create_image(pixels * 10, pixels * 4, anchor='nw',
                                                 image=obstacle_object)
obstacle21 = canvas_widget.create_image(pixels * 13, pixels * 4, anchor='nw',
                                                 image=obstacle_object)
obstacle22 = canvas_widget.create_image(pixels * 8, pixels * 5, anchor='nw',
                                                 image=shop_object)
obstacle23 = canvas_widget.create_image(pixels * 3, pixels * 6, anchor='nw',
                                                 image=obstacle_object)
obstacle24 = canvas_widget.create_image(pixels * 6, pixels * 6, anchor='nw',
                                                 image=obstacle_object)
obstacle25 = canvas_widget.create_image(pixels * 11, pixels * 6, anchor='nw',
                                                 image=tree_object)
obstacle26 = canvas_widget.create_image(pixels * 14, pixels * 6, anchor='nw',
                                                 image=obstacle_object)
obstacle27 = canvas_widget.create_image(pixels * 0, pixels * 7, anchor='nw',
                                                  image=obstacle_object)
obstacle28 = canvas_widget.create_image(pixels * 1, pixels * 7, anchor='nw',
                                                 image=tree_object)
obstacle29 = canvas_widget.create_image(pixels * 9, pixels * 7, anchor='nw',
                                                 image=cube_object)
obstacle30 = canvas_widget.create_image(pixels * 3, pixels * 8, anchor='nw',
                                                 image=building_object)
obstacle31 = canvas_widget.create_image(pixels * 5, pixels * 8, anchor='nw',
                                                 image=obstacle_object)
obstacle32 = canvas_widget.create_image(pixels * 9, pixels * 8, anchor='nw',
                                                 image=shop_object)
obstacle33 = canvas_widget.create_image(pixels * 12, pixels * 8, anchor='nw',
                                                 image=tree_object)
obstacle34 = canvas_widget.create_image(pixels * 14, pixels * 8, anchor='nw',
                                                 image=obstacle_object)
obstacle35 = canvas_widget.create_image(pixels * 0, pixels * 9, anchor='nw',
                                                 image=shop_object)
obstacle36 = canvas_widget.create_image(pixels * 7, pixels * 9, anchor='nw',
                                                 image=obstacle_object)
obstacle37 = canvas_widget.create_image(pixels * 3, pixels * 10, anchor='nw',
                                                 image=building_object)
obstacle38 = canvas_widget.create_image(pixels * 5, pixels * 10, anchor='nw',
                                                 image=tree_object)
obstacle39 = canvas_widget.create_image(pixels * 12, pixels * 10, anchor='nw',
                                                 image=obstacle_object)
obstacle40 = canvas_widget.create_image(pixels * 1, pixels * 11, anchor='nw',
                                                 image=tree_object)
obstacle41 = canvas_widget.create_image(pixels * 6, pixels * 11, anchor='nw',
                                                 image=obstacle_object)
obstacle42 = canvas_widget.create_image(pixels * 9, pixels * 11, anchor='nw',
                                                 image=tree_object)
obstacle43 = canvas_widget.create_image(pixels * 12, pixels * 12, anchor='nw',
                                                 image=garbage_object)
obstacle44 = canvas_widget.create_image(pixels * 13, pixels * 12, anchor='nw',
                                                 image=garbage_object)
obstacle45 = canvas_widget.create_image(pixels * 14, pixels * 12, anchor='nw',
                                                 image=garbage_object)
obstacle46 = canvas_widget.create_image(pixels * 2, pixels * 13, anchor='nw',
                                                 image=obstacle_object)
obstacle47 = canvas_widget.create_image(pixels * 4, pixels * 13, anchor='nw',
                                                 image=building_object)
obstacle48 = canvas_widget.create_image(pixels * 7, pixels * 13, anchor='nw',
                                                 image=obstacle_object)
obstacle49 = canvas_widget.create_image(pixels * 12, pixels * 13, anchor='nw',
                                                 image=garbage_object)
obstacle50 = canvas_widget.create_image(pixels * 14, pixels * 13, anchor='nw',
                                                 image=garbage_object)
obstacle51 = canvas_widget.create_image(pixels * 0, pixels * 14, anchor='nw',
                                                 image=building_object)
obstacle52 = canvas_widget.create_image(pixels * 14, pixels * 14, anchor='nw',
                                                 image=garbage_object)

img_flag = Image.open("images/flag.png")
flag_object = ImageTk.PhotoImage(img_flag)
flag = canvas_widget.create_image(pixels * 13, pixels * 13, anchor='nw', image=flag_object)

img_robot = Image.open("images/agent.png")
robot = ImageTk.PhotoImage(img_robot)
agent = canvas_widget.create_image(0, 0, anchor='nw', image=robot)

canvas_widget.pack()

root.mainloop()