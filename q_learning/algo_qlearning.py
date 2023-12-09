import pandas as pd
import numpy as np
from environment import final_states


class QLearning:

    def __init__(self, actions):
        '''
        Q leanring inital parameters

        Parameters
        ----------
            actions : int
                all actions including up, down, left, right
            alpha : int
                learning rate
            gamma : int
                discount factor
            epsilon : int
                probability
            decay_factor : int
            q_table : pandas Dataframe
                Q-table with actions as columns
            q_table_final : pandas Dataframe
                final Q-table
        '''
        self.actions = actions
        self.alpha = 0.9
        self.gamma = 0.9
        self.epsilon = 0.5
        self.decay_factor = 0.9999
        self.q_table = pd.DataFrame(columns=self.actions,
                                    dtype=np.float64)
        self.q_table_final = pd.DataFrame(columns=self.actions,
                                          dtype=np.float64)

    def choose_action(self, observation):
        '''
        Returns an action through exploration and exploitation

                Parameters:
                        observation: current state of
                        the agent in the format of state = '[5.0, 40.0]'

                Returns:
                        action number
        '''
        self.check_state_exist(observation)
        self.epsilon *= self.decay_factor  # epsilon greedy
        if np.random.random() < self.epsilon:
            action = np.random.choice(self.actions)
        else:
            # access a group of rows and columns [row , column]
            state_action = self.q_table.loc[observation, :]
            # reindex: based on previous DataFrame, regenerate new indexes
            state_action = state_action.reindex(
                np.random.permutation(state_action.index))
            action = state_action.idxmax()  # return index of first occurrence of maximum value
        return action

    def learning(self, state, action, reward, next_state):
        '''
        Function for learning and updating Q-table with new data

                Parameters:
                        state: current state of the agent
                        action: chosen action
                        reward: received reward
                        next_state: next state that the agent will move

                Returns:
                        update Q-table
        '''
        self.check_state_exist(next_state)
        q_current = self.q_table.loc[state, action]
        if next_state != 'Goal' or next_state != 'Obstacle' or next_state != 'Rubik':
            q_target = reward + self.gamma * \
                self.q_table.loc[next_state, :].max()
        else:
            q_target = reward

        self.q_table.loc[state, action] += self.alpha * \
            (q_target - q_current)  # updating Q-table
        return self.q_table.loc[state, action]

    def check_state_exist(self, state):
        '''
        Adding new states to the Q-table
        (pd.series generate 1-dimensional array)
        '''
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(pd.Series(
                [0] * len(self.actions), index=self.q_table.columns, name=state))

    def print_q_table(self):
        '''
        Saving final Q-table
        '''
        final_route = final_states()
        for i in range(len(final_route)):
            state = str(final_route[i])
            for j in range(len(self.q_table.index)):
                if self.q_table.index[j] == state:
                    self.q_table_final.loc[state,
                                           :] = self.q_table.loc[state, :]

        with open('data.txt', 'a') as f:
            f.write(f'Final Path Q-table: {str(self.q_table_final)} \n')
            f.write(f'Full Q-table:: {str(self.q_table)} \n')
