import pandas as pd
import numpy as np


class SARSA:
    def __init__(self, actions):
        '''
        SARSA inital parameters

        Parameters
        ----------
            actions : int
                all actions including up, down, left, right
            alpha : int
                learning rate
            gamma : int
                discount factor
            q_table : pandas Dataframe
                Q-table with actions as columns
            q_table_final : pandas Dataframe
                final Q-table
        '''
        self.actions = actions
        self.alpha = 0.9
        self.gamma = 0.9
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        self.q_table_final = pd.DataFrame(
            columns=self.actions, dtype=np.float64)

    # exploration and exploitation
    def choose_action(self, observation, epsilon):
        self.check_state_exist(observation)
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.choice(self.actions)
        else:
            state_action = self.q_table.loc[observation, :]
            action = state_action.idxmax()
        return action

    # Function for learning and updating Q-table with new knowledge
    def learning(self, state, action, reward, next_state, next_action):
        self.check_state_exist(next_state)
        # current state and action for that state
        q_current = self.q_table.loc[state, action]
        if next_state != 'Goal' or next_state != 'Obstacle':
            q_target = reward + self.gamma * \
                self.q_table.loc[next_state, next_action]
        else:
            q_target = reward
        # updating Q-table
        self.q_table.loc[state, action] += self.alpha * (q_target - q_current)
        # return a value that is Q-value
        return self.q_table.loc[state, action]

    # Adding to the Q-table new states (pd.series generate 1-dimensional array)
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(pd.Series(
                [0] * len(self.actions), index=self.q_table.columns, name=state))
