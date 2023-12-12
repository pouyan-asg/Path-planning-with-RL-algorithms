import random
import pandas as pd
import numpy as np
from operator import add


class Double_QLearning:
    def __init__(self, actions):
        self.actions = actions
        self.alpha = 0.9  # learning rate
        self.gamma = 0.9  # discount factor
        self.probability = 0.5  # fix
        self.q_table1 = pd.DataFrame(columns=self.actions, dtype=np.float64)
        self.q_table2 = pd.DataFrame(columns=self.actions, dtype=np.float64)
        self.q_table_final = pd.DataFrame(
            columns=self.actions, dtype=np.float64)

    # exploration and exploitation
    def choose_action(self, state, epsilon):
        self.check_state_exist1(state)
        self.check_state_exist2(state)
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(self.actions)
        else:
            state_action1 = list(self.q_table1.loc[state, :])
            state_action2 = list(self.q_table2.loc[state, :])
            state_action = random.shuffle(
                list(map(add, state_action1, state_action2)))
            action = np.argmax(state_action)
        return action

    # Function for learning and updating Q-table with new knowledge
    def learning(self, state, action, reward, next_state):
        self.check_state_exist1(next_state)
        self.check_state_exist2(next_state)
        q_current1 = self.q_table1.loc[state, action]
        q_current2 = self.q_table2.loc[state, action]
        arg1 = self.q_table1.loc[next_state, :].idxmax()
        arg2 = self.q_table2.loc[next_state, :].idxmax()
        if np.random.random() < self.probability:
            if next_state != 'Goal' or next_state != 'Obstacle':
                q_target1 = reward + self.gamma * \
                    self.q_table2.loc[next_state, arg1]
            else:
                q_target1 = reward
            self.q_table1.loc[state, action] += self.alpha * \
                (q_target1 - q_current1)
        else:
            if next_state != 'Goal' or next_state != 'Obstacle':
                q_target2 = reward + self.gamma * \
                    self.q_table1.loc[next_state, arg2]
            else:
                q_target2 = reward
            self.q_table2.loc[state, action] += self.alpha * \
                (q_target2 - q_current2)

        return self.q_table1.loc[state,
                                 action], self.q_table2.loc[state, action]

    # Adding to the Q-table new states (pd.series generate 1-dimensional array)
    def check_state_exist1(self, state):
        if state not in self.q_table1.index:
            self.q_table1 = self.q_table1.append(pd.Series(
                [0] * len(self.actions), index=self.q_table1.columns, name=state))

    def check_state_exist2(self, state):
        if state not in self.q_table2.index:
            self.q_table2 = self.q_table2.append(pd.Series(
                [0] * len(self.actions), index=self.q_table2.columns, name=state))
