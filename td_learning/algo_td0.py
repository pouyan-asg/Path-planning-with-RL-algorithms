import pandas as pd
import numpy as np
from environment import final_states


class TemporalDifference:

    def __init__(self):
        '''
        TD inital parameters

        Parameters
        ----------
            alpha : int
                learning rate
            gamma : int
                discount factor
            epsilon : int
                probability
            decay_factor : int
            q_table : pandas Dataframe
                V-table with state values as columns
            q_table_final : pandas Dataframe
                final V-table
        '''

        self.alpha = 0.9
        self.gamma = 0.9
        self.epsilon = 0.5
        self.decay_factor = 0.99995
        self.v_table = pd.DataFrame(columns=['state value'], dtype=np.float64)
        self.v_table_final = pd.DataFrame(
            columns=['state value'], dtype=np.float64)

    def learning(self, state, reward, next_state):
        '''
        Function for learning and updating V-table with new data

                Parameters:
                        state: current state of the agent
                        action: chosen action
                        reward: received reward
                        next_state: next state that the agent will move

                Returns:
                        update V-table
        '''
        self.check_state_exist(next_state)
        v_current = self.v_table.loc[state]
        if next_state != 'Goal' or next_state != 'Obstacle' or next_state != 'Rubik':
            v_target = reward + self.gamma * self.v_table.loc[next_state]
        else:
            v_target = reward
        self.v_table.loc[state] += self.alpha * (v_target - v_current)
        return self.v_table.loc[state]

    def check_state_exist(self, state):
        '''
        Adding new states to the V-table
        '''
        if state not in self.v_table.index:
            self.v_table = self.v_table.append(
                pd.Series([0] * 1, index=self.v_table.columns, name=state))

    def print_v_table(self):
        '''
        Saving final Q-table
        '''
        final_route = final_states()
        for i in range(len(final_route)):
            state = str(final_route[i])
            for j in range(len(self.v_table.index)):
                if self.v_table.index[j] == state:
                    self.v_table_final.loc[state] = self.v_table.loc[state]

        with open('data.txt', 'a') as f:
            f.write(f'Final Path V-table: {str(self.v_table_final)} \n')
            f.write(f'Full V-table:: {str(self.v_table)} \n')
