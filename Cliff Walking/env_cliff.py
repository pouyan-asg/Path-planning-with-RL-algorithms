import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

pixels = 80   # pictures pixels
env_height = 4  # grid height
env_width = 12  # grid width
global_variable = {}  # for the final route coordination


class Environment(tk.Tk, object):
    def __init__(self):
        super(Environment, self).__init__()
        self.num_actions = 4  # actions = ['up', 'down', 'right', 'left']
        self.title('Cliff Walking - Sutton Book')
        self.geometry(f'{env_width * pixels}x{env_height * pixels}+450+250')
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
            x0, y0, x1, y1 = 0, row, env_width * pixels, row
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

        img_cliff = Image.open("images/cliff.png")
        self.cliff_object = ImageTk.PhotoImage(img_cliff)

        self.obstacle1 = self.canvas_widget.create_image(pixels, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle2 = self.canvas_widget.create_image(pixels * 2, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle3 = self.canvas_widget.create_image(pixels * 3, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle4 = self.canvas_widget.create_image(pixels * 4, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle5 = self.canvas_widget.create_image(pixels * 5, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle6 = self.canvas_widget.create_image(pixels * 6, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle7 = self.canvas_widget.create_image(pixels * 7, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle8 = self.canvas_widget.create_image(pixels * 8, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle9 = self.canvas_widget.create_image(pixels * 9, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)
        self.obstacle10 = self.canvas_widget.create_image(pixels * 10, pixels * 3, anchor='nw',
                                                         image=self.cliff_object)

        img_flag = Image.open("images/end.png")
        self.flag_object = ImageTk.PhotoImage(img_flag)
        self.flag = self.canvas_widget.create_image(pixels * 11, pixels * 3, anchor='nw', image=self.flag_object)

        img_robot = Image.open("images/robot.png")
        self.robot = ImageTk.PhotoImage(img_robot)
        self.agent = self.canvas_widget.create_image(pixels * 0, pixels * 3, anchor='nw', image=self.robot)

        img_start = Image.open("images/start.png")
        self.start_object = ImageTk.PhotoImage(img_start)
        self.start = self.canvas_widget.create_image(pixels * 0, pixels * 3, anchor='nw', image=self.start_object)

        self.canvas_widget.pack()

    def reset(self):
        self.update()
        self.canvas_widget.delete(self.agent)
        self.agent = self.canvas_widget.create_image(0, pixels * 3, anchor='nw', image=self.robot)
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

        self.canvas_widget.move(self.agent, base_action[0], base_action[1])
        self.comparison_dic[self.key_dic] = self.canvas_widget.coords(self.agent)
        next_state = self.comparison_dic[self.key_dic]
        self.key_dic += 1

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

            # # storing longest path
            # if len(self.comparison_dic) > self.longest_path:
            #     self.longest_path = len(self.comparison_dic)

        elif next_state in [self.canvas_widget.coords(self.obstacle1),
                            self.canvas_widget.coords(self.obstacle2),
                            self.canvas_widget.coords(self.obstacle3),
                            self.canvas_widget.coords(self.obstacle4),
                            self.canvas_widget.coords(self.obstacle5),
                            self.canvas_widget.coords(self.obstacle6),
                            self.canvas_widget.coords(self.obstacle7),
                            self.canvas_widget.coords(self.obstacle8),
                            self.canvas_widget.coords(self.obstacle9),
                            self.canvas_widget.coords(self.obstacle10)]:
            reward = -100
            next_state = 'Obstacle'
            self.comparison_dic = {}
            self.key_dic = 0
            done = True

        else:
            reward = -1
            done = False

        return next_state, reward, done

    def final_path_Q(self):
        origin_point1 = np.array([40, 40])
        path_list1 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list1.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point1[0] - 30, self.path_dic[j][1] + origin_point1[1] - 30,
                self.path_dic[j][0] + origin_point1[0] + 30, self.path_dic[j][1] + origin_point1[1] + 30,
                fill='#0C4A75', outline='#00DCFF')
        self.path_dic = {}
        self.fake = True
        f = open("cliff_data.txt", "w")
        f.write(f'Q-Learning: {str(path_list1)} \n')
        f.close()
        print('Path:', path_list1)

    def final_path_SARSA(self):
        origin_point2 = np.array([40, 40])
        path_list2 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list2.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point2[0] - 22, self.path_dic[j][1] + origin_point2[1] - 22,
                self.path_dic[j][0] + origin_point2[0] + 22, self.path_dic[j][1] + origin_point2[1] + 22,
                fill='#FF5885', outline='#FF5885')
        self.path_dic = {}
        self.fake = True
        f = open("cliff_data.txt", "a")
        f.write(f'SARSA: {str(path_list2)} \n')
        f.close()
        print('Path:', path_list2)

    def final_path_DQL(self):
        origin_point3 = np.array([40, 40])
        path_list3 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list3.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point3[0] - 15, self.path_dic[j][1] + origin_point3[1] - 15,
                self.path_dic[j][0] + origin_point3[0] + 15, self.path_dic[j][1] + origin_point3[1] + 15,
                fill='#FF8E23', outline='#00DCFF')
        self.path_dic = {}
        self.fake = True
        f = open("cliff_data.txt", "a")
        f.write(f'Double Q-Learning: {str(path_list3)} \n')
        f.close()
        print('Path:', path_list3)


