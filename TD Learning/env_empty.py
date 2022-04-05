import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

pixels = 40   # pictures pixels
env_height = 15  # grid height
env_width = 15  # grid width
global_variable = {}  # for the final route coordination


class Environment(tk.Tk, object):
    def __init__(self):
        super(Environment, self).__init__()
        self.num_actions = 4  # actions = ['up', 'down', 'right', 'left']
        self.title('Path Planing with Reinforcement Learning')
        self.geometry(f'{env_width * pixels}x{env_height * pixels}+600+250')
        self.build_environment()
        self.comparison_dic = {}
        self.path_dic = {}
        self.key_dic = 0
        self.fake = True  # fake variable for reaching final Goal for first time
        self.longest_path = 0
        self.shortest_path = 0

    def build_environment(self):
        self.canvas_widget = tk.Canvas(self, bg='white',
                                       height=env_height * pixels, width=env_width * pixels)
        for column in range(0, env_width * pixels, pixels):
            x0, y0, x1, y1 = column, 0, column, env_height * pixels
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')
        for row in range(0, env_height * pixels, pixels):
            x0, y0, x1, y1 = 0, row, env_height * pixels, row
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

        img_obstacle = Image.open("images/obstacle.png")
        self.obstacle_object = ImageTk.PhotoImage(img_obstacle)

        img_tree = Image.open("images/tree.png")
        self.tree_object = ImageTk.PhotoImage(img_tree)

        img_shop = Image.open("images/shop.png")
        self.shop_object = ImageTk.PhotoImage(img_shop)

        img_building = Image.open("images/building.png")
        self.building_object = ImageTk.PhotoImage(img_building)

        img_cube = Image.open("images/rubik.png")
        self.cube_object = ImageTk.PhotoImage(img_cube)

        img_garbage = Image.open("images/garbage.png")
        self.garbage_object = ImageTk.PhotoImage(img_garbage)

        # self.obstacle1 = self.canvas_widget.create_image(pixels * 2, 0, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle2 = self.canvas_widget.create_image(pixels * 9, 0, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle3 = self.canvas_widget.create_image(pixels * 11, 0, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle4 = self.canvas_widget.create_image(pixels * 14, 0, anchor='nw',
        #                                                  image=self.shop_object)
        # self.obstacle5 = self.canvas_widget.create_image(pixels * 5, 0, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle6 = self.canvas_widget.create_image(0, pixels, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle7 = self.canvas_widget.create_image(pixels * 7, pixels, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle8 = self.canvas_widget.create_image(pixels * 9, pixels, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle9 = self.canvas_widget.create_image(pixels * 13, pixels, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle10 = self.canvas_widget.create_image(pixels * 3, pixels * 2, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle11 = self.canvas_widget.create_image(pixels * 5, pixels * 2, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle12 = self.canvas_widget.create_image(pixels * 11, pixels * 2, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle13 = self.canvas_widget.create_image(pixels * 0, pixels * 3, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle14 = self.canvas_widget.create_image(pixels * 2, pixels * 4, anchor='nw',
        #                                                  image=self.shop_object)
        # self.obstacle15 = self.canvas_widget.create_image(pixels * 8, pixels * 3, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle16 = self.canvas_widget.create_image(pixels * 9, pixels * 3, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle17 = self.canvas_widget.create_image(pixels * 14, pixels * 3, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle19 = self.canvas_widget.create_image(pixels * 5, pixels * 4, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle20 = self.canvas_widget.create_image(pixels * 10, pixels * 4, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle21 = self.canvas_widget.create_image(pixels * 13, pixels * 4, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle22 = self.canvas_widget.create_image(pixels * 8, pixels * 5, anchor='nw',
        #                                                  image=self.shop_object)
        # self.obstacle23 = self.canvas_widget.create_image(pixels * 3, pixels * 6, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle24 = self.canvas_widget.create_image(pixels * 6, pixels * 6, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle25 = self.canvas_widget.create_image(pixels * 11, pixels * 6, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle26 = self.canvas_widget.create_image(pixels * 14, pixels * 6, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle27 = self.canvas_widget.create_image(pixels * 0, pixels * 7, anchor='nw',
        #                                                   image=self.obstacle_object)
        # self.obstacle28 = self.canvas_widget.create_image(pixels * 1, pixels * 7, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle29 = self.canvas_widget.create_image(pixels * 9, pixels * 7, anchor='nw',
        #                                                  image=self.cube_object)
        # self.obstacle30 = self.canvas_widget.create_image(pixels * 3, pixels * 8, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle31 = self.canvas_widget.create_image(pixels * 5, pixels * 8, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle32 = self.canvas_widget.create_image(pixels * 9, pixels * 8, anchor='nw',
        #                                                  image=self.shop_object)
        # self.obstacle33 = self.canvas_widget.create_image(pixels * 12, pixels * 8, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle34 = self.canvas_widget.create_image(pixels * 14, pixels * 8, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle35 = self.canvas_widget.create_image(pixels * 0, pixels * 9, anchor='nw',
        #                                                  image=self.shop_object)
        # self.obstacle36 = self.canvas_widget.create_image(pixels * 7, pixels * 9, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle37 = self.canvas_widget.create_image(pixels * 3, pixels * 10, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle38 = self.canvas_widget.create_image(pixels * 5, pixels * 10, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle39 = self.canvas_widget.create_image(pixels * 12, pixels * 10, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle40 = self.canvas_widget.create_image(pixels * 1, pixels * 11, anchor='nw',
        #                                                  image=self.tree_object)
        # self.obstacle41 = self.canvas_widget.create_image(pixels * 6, pixels * 11, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle42 = self.canvas_widget.create_image(pixels * 9, pixels * 11, anchor='nw',
        #                                                  image=self.tree_object)
        self.obstacle43 = self.canvas_widget.create_image(pixels * 12, pixels * 12, anchor='nw',
                                                         image=self.garbage_object)
        self.obstacle44 = self.canvas_widget.create_image(pixels * 13, pixels * 12, anchor='nw',
                                                         image=self.garbage_object)
        self.obstacle45 = self.canvas_widget.create_image(pixels * 14, pixels * 12, anchor='nw',
                                                         image=self.garbage_object)
        # self.obstacle46 = self.canvas_widget.create_image(pixels * 2, pixels * 13, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle47 = self.canvas_widget.create_image(pixels * 4, pixels * 13, anchor='nw',
        #                                                  image=self.building_object)
        # self.obstacle48 = self.canvas_widget.create_image(pixels * 7, pixels * 13, anchor='nw',
        #                                                  image=self.obstacle_object)
        # self.obstacle49 = self.canvas_widget.create_image(pixels * 12, pixels * 13, anchor='nw',
        #                                                  image=self.garbage_object)
        self.obstacle50 = self.canvas_widget.create_image(pixels * 14, pixels * 13, anchor='nw',
                                                         image=self.garbage_object)
        # self.obstacle51 = self.canvas_widget.create_image(pixels * 0, pixels * 14, anchor='nw',
        #                                                  image=self.building_object)
        self.obstacle52 = self.canvas_widget.create_image(pixels * 14, pixels * 14, anchor='nw',
                                                         image=self.garbage_object)

        img_flag = Image.open("images/flag.png")
        self.flag_object = ImageTk.PhotoImage(img_flag)
        self.flag = self.canvas_widget.create_image(pixels * 13, pixels * 13, anchor='nw', image=self.flag_object)

        img_robot = Image.open("images/agent.png")
        self.robot = ImageTk.PhotoImage(img_robot)
        self.agent = self.canvas_widget.create_image(0, 0, anchor='nw', image=self.robot)

        self.canvas_widget.pack()

    def reset(self):
        self.update()
        self.canvas_widget.delete(self.agent)
        self.agent = self.canvas_widget.create_image(0, 0, anchor='nw', image=self.robot)
        self.comparison_dic = {}
        self.key_dic = 0
        return self.canvas_widget.coords(self.agent)  # agent's current state in the form of [120.0, 40.0]

    def refresh(self):
        self.update()

    def step(self, action):
        state = self.canvas_widget.coords(self.agent)
        base_action = np.array([0, 0])

        # Actions = {0:'up', 1:'down', 2:'right', 3:'left}
        if action == 0:
            if state[1] >= pixels:
                base_action[1] -= pixels
        elif action == 1:
            if state[1] < (env_height - 1) * pixels:
                base_action[1] += pixels
        elif action == 2:
            if state[0] < (env_width - 1) * pixels:
                base_action[0] += pixels
        elif action == 3:
            if state[0] >= pixels:
                base_action[0] -= pixels

        # moving the agent (add X amount = base_action[0] and Y amount to coordination of self.agent)
        self.canvas_widget.move(self.agent, base_action[0], base_action[1])
        self.comparison_dic[self.key_dic] = self.canvas_widget.coords(self.agent)  # storing new position of agent
        next_state = self.comparison_dic[self.key_dic]
        self.key_dic += 1  # add next key in dictionary

        if next_state == self.canvas_widget.coords(self.flag):
            reward = 900
            next_state = 'Goal'
            done = True

            # filling the dictionary first time
            if self.fake == True:
                for j in range(len(self.comparison_dic)):
                    self.path_dic[j] = self.comparison_dic[j]
                self.fake = False
                self.longest_path = len(self.comparison_dic)
                self.shortest_path = len(self.comparison_dic)

            # storing shortest path
            if len(self.comparison_dic) < len(self.path_dic):
                self.shortest_path = len(self.comparison_dic)
                self.path_dic = {}
                for j in range(len(self.comparison_dic)):
                    self.path_dic[j] = self.comparison_dic[j]

            # storing longest path
            if len(self.comparison_dic) > self.longest_path:
                self.longest_path = len(self.comparison_dic)

        elif next_state in [
                            # self.canvas_widget.coords(self.obstacle1),
        #                     self.canvas_widget.coords(self.obstacle2),
        #                     self.canvas_widget.coords(self.obstacle3),
        #                     self.canvas_widget.coords(self.obstacle4),
        #                     self.canvas_widget.coords(self.obstacle5),
        #                     self.canvas_widget.coords(self.obstacle6),
        #                     self.canvas_widget.coords(self.obstacle7),
        #                     self.canvas_widget.coords(self.obstacle8),
        #                     self.canvas_widget.coords(self.obstacle9),
        #                     self.canvas_widget.coords(self.obstacle10),
        #                     self.canvas_widget.coords(self.obstacle11),
        #                     self.canvas_widget.coords(self.obstacle12),
        #                     self.canvas_widget.coords(self.obstacle13),
        #                     self.canvas_widget.coords(self.obstacle14),
        #                     self.canvas_widget.coords(self.obstacle15),
        #                     self.canvas_widget.coords(self.obstacle16),
        #                     self.canvas_widget.coords(self.obstacle17),
        #                     self.canvas_widget.coords(self.obstacle19),
        #                     self.canvas_widget.coords(self.obstacle20),
        #                     self.canvas_widget.coords(self.obstacle21),
        #                     self.canvas_widget.coords(self.obstacle22),
        #                     self.canvas_widget.coords(self.obstacle23),
        #                     self.canvas_widget.coords(self.obstacle24),
        #                     self.canvas_widget.coords(self.obstacle25),
        #                     self.canvas_widget.coords(self.obstacle26),
        #                     self.canvas_widget.coords(self.obstacle27),
        #                     self.canvas_widget.coords(self.obstacle28),
        #                     self.canvas_widget.coords(self.obstacle30),
        #                     self.canvas_widget.coords(self.obstacle31),
        #                     self.canvas_widget.coords(self.obstacle32),
        #                     self.canvas_widget.coords(self.obstacle33),
        #                     self.canvas_widget.coords(self.obstacle34),
        #                     self.canvas_widget.coords(self.obstacle35),
        #                     self.canvas_widget.coords(self.obstacle36),
        #                     self.canvas_widget.coords(self.obstacle37),
        #                     self.canvas_widget.coords(self.obstacle38),
        #                     self.canvas_widget.coords(self.obstacle39),
        #                     self.canvas_widget.coords(self.obstacle40),
        #                     self.canvas_widget.coords(self.obstacle41),
        #                     self.canvas_widget.coords(self.obstacle42),
                            self.canvas_widget.coords(self.obstacle43),
                            self.canvas_widget.coords(self.obstacle44),
                            self.canvas_widget.coords(self.obstacle45),
        #                     self.canvas_widget.coords(self.obstacle46),
        #                     self.canvas_widget.coords(self.obstacle47),
        #                     self.canvas_widget.coords(self.obstacle48),
        #                     self.canvas_widget.coords(self.obstacle49),
                            self.canvas_widget.coords(self.obstacle50),
        #                     self.canvas_widget.coords(self.obstacle51),
                            self.canvas_widget.coords(self.obstacle52)]:
            reward = -5
            done = True
            next_state = 'Obstacle'
            self.comparison_dic = {}
            self.key_dic = 0

        # elif next_state in [self.canvas_widget.coords(self.obstacle29)]:
        #     reward = -1
        #     done = True
        #     next_state = 'Rubik'
        #     self.comparison_dic = {}
        #     self.key_dic = 0

        else:
            reward = 0
            done = False

        return next_state, reward, done

    def final_path(self):
        origin_point = np.array([20, 20])
        path_list = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point[0] - 12, self.path_dic[j][1] + origin_point[1] - 12,
                self.path_dic[j][0] + origin_point[0] + 12, self.path_dic[j][1] + origin_point[1] + 12,
                fill='black', outline='black')
            global_variable[j] = self.path_dic[j]  # putting the final route in a global variable
        print('The Shortest Path:', self.shortest_path)
        print('The Longest Path:', self.longest_path)
        print('Optimal Path:', path_list)


# using final path for plotting
def final_states():
    return global_variable
