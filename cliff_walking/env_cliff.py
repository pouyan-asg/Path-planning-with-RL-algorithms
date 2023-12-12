import numpy as np
import tkinter as tk
from PIL import Image, ImageTk


global_variable = {}


class Environment(tk.Tk, object):
    def __init__(self):
        '''
        Constructs all the necessary attributes for the environment.

        Parameters
        ----------
            num_actions: all actions including up, down, left, right
            pixels: environment pixels for each location
            env_height: number of vertical grids for the environment
            env_width: number of horizontal grids for the environment
            title: Tkinter environment title
            geometry: environmet geometry which is (w*px)*(h*px)+offsets
            comparison_dic: storing agnet pathway for each iteration
            path_dic: saving final pathway of teh agent
            key_dic: a counter for stroing paths
            fake: fake variable for reaching final Goal for first time
            longest_path: logest path to reach the Goal
            shortest_path: shortest path to reach the Goal
        '''

        super(Environment, self).__init__()
        self.num_actions = 4
        self.title('Cliff Walking - Sutton Book')
        self.pixels = 80
        self.env_height = 4
        self.env_width = 12
        self.geometry(
            f'{self.env_width * self.pixels}x{self.env_height * self.pixels}+450+250')
        self.build_environment()
        self.comparison_dic = {}
        self.path_dic = {}
        self.key_dic = 0
        self.fake = True
        self.longest_path = 0
        self.shortest_path = 0

    def build_environment(self):
        '''
        environment creation by Tkinter
        '''

        self.canvas_widget = tk.Canvas(
            self,
            bg='white',
            height=self.env_height *
            self.pixels,
            width=self.env_width *
            self.pixels)
        for column in range(0, self.env_width * self.pixels, self.pixels):
            x0, y0, x1, y1 = column, 0, column, self.env_height * self.pixels
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')
        for row in range(0, self.env_height * self.pixels, self.pixels):
            x0, y0, x1, y1 = 0, row, self.env_width * self.pixels, row
            self.canvas_widget.create_line(x0, y0, x1, y1, fill='grey')

        img_cliff = Image.open("images/cliff.png")
        self.cliff_object = ImageTk.PhotoImage(img_cliff)

        self.obstacle1 = self.canvas_widget.create_image(
            self.pixels, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle2 = self.canvas_widget.create_image(
            self.pixels * 2, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle3 = self.canvas_widget.create_image(
            self.pixels * 3, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle4 = self.canvas_widget.create_image(
            self.pixels * 4, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle5 = self.canvas_widget.create_image(
            self.pixels * 5, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle6 = self.canvas_widget.create_image(
            self.pixels * 6, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle7 = self.canvas_widget.create_image(
            self.pixels * 7, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle8 = self.canvas_widget.create_image(
            self.pixels * 8, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle9 = self.canvas_widget.create_image(
            self.pixels * 9, self.pixels * 3, anchor='nw', image=self.cliff_object)
        self.obstacle10 = self.canvas_widget.create_image(
            self.pixels * 10, self.pixels * 3, anchor='nw', image=self.cliff_object)

        img_flag = Image.open("images/end.png")
        self.flag_object = ImageTk.PhotoImage(img_flag)
        self.flag = self.canvas_widget.create_image(
            self.pixels * 11, self.pixels * 3, anchor='nw', image=self.flag_object)

        img_robot = Image.open("images/robot.png")
        self.robot = ImageTk.PhotoImage(img_robot)
        self.agent = self.canvas_widget.create_image(
            self.pixels * 0, self.pixels * 3, anchor='nw', image=self.robot)

        img_start = Image.open("images/start.png")
        self.start_object = ImageTk.PhotoImage(img_start)
        self.start = self.canvas_widget.create_image(
            self.pixels * 0, self.pixels * 3, anchor='nw', image=self.start_object)

        self.canvas_widget.pack()

    def reset(self):
        '''
        reset the environment and all parameters
                Return:
                     the agent's current state in the format of [120.0, 40.0]
        '''

        self.update()
        self.canvas_widget.delete(self.agent)
        self.agent = self.canvas_widget.create_image(
            0, self.pixels * 3, anchor='nw', image=self.robot)
        self.comparison_dic = {}
        self.key_dic = 0
        return self.canvas_widget.coords(self.agent)

    def refresh(self):
        '''
        update and refresh the environment before training
        '''
        self.update()

    def step(self, action):
        '''
        Moving the agent one pixel and update reward, action and next step regarding the agent next location

                Parameters:
                        action: Actions = {0:'up', 1:'down', 2:'right', 3:'left}

                Returns:
                        reward, next step and done flag
        '''

        state = self.canvas_widget.coords(self.agent)
        base_action = np.array([0, 0])

        if action == 0:
            if state[1] >= self.pixels:
                base_action[1] -= self.pixels
        elif action == 1:
            if state[1] < (self.env_height - 1) * self.pixels:
                base_action[1] += self.pixels
        elif action == 2:
            if state[0] < (self.env_width - 1) * self.pixels:
                base_action[0] += self.pixels
        elif action == 3:
            if state[0] >= self.pixels:
                base_action[0] -= self.pixels

        self.canvas_widget.move(self.agent, base_action[0], base_action[1])
        self.comparison_dic[self.key_dic] = self.canvas_widget.coords(
            self.agent)
        next_state = self.comparison_dic[self.key_dic]
        self.key_dic += 1

        if next_state == self.canvas_widget.coords(self.flag):
            reward = 900
            next_state = 'Goal'
            done = True

            # filling the dictionary first time
            if self.fake:
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
        '''
        saving final path of Q-learning algorithm
        '''

        origin_point1 = np.array([40, 40])
        path_list1 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list1.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point1[0] - 30,
                self.path_dic[j][1] + origin_point1[1] - 30,
                self.path_dic[j][0] + origin_point1[0] + 30,
                self.path_dic[j][1] + origin_point1[1] + 30,
                fill='#0C4A75',
                outline='#00DCFF')
        self.path_dic = {}
        self.fake = True
        f = open("cliff_data.txt", "w")
        f.write(f'Q-Learning: {str(path_list1)} \n')
        f.close()
        print('Path:', path_list1)

    def final_path_SARSA(self):
        '''
        saving final path of SARSA algorithm
        '''

        origin_point2 = np.array([40, 40])
        path_list2 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list2.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point2[0] - 22,
                self.path_dic[j][1] + origin_point2[1] - 22,
                self.path_dic[j][0] + origin_point2[0] + 22,
                self.path_dic[j][1] + origin_point2[1] + 22,
                fill='#FF5885',
                outline='#FF5885')
        self.path_dic = {}
        self.fake = True
        f = open("cliff_data.txt", "a")
        f.write(f'SARSA: {str(path_list2)} \n')
        f.close()
        print('Path:', path_list2)

    def final_path_DQL(self):
        '''
        saving final path double Q-learning algorithm
        '''

        origin_point3 = np.array([40, 40])
        path_list3 = []
        self.canvas_widget.delete(self.agent)
        for j in range(len(self.path_dic)):
            path_list3.append(self.path_dic[j])
            self.track = self.canvas_widget.create_oval(
                self.path_dic[j][0] + origin_point3[0] - 15,
                self.path_dic[j][1] + origin_point3[1] - 15,
                self.path_dic[j][0] + origin_point3[0] + 15,
                self.path_dic[j][1] + origin_point3[1] + 15,
                fill='#FF8E23',
                outline='#00DCFF')
        self.path_dic = {}
        self.fake = True
        with open("cliff_data.txt", "a") as f:
            f.write(f'Double Q-Learning: {str(path_list3)} \n')
        print('Path:', path_list3)
