import pandas as pd
from env import *


class Temporal_Difference:
    def __init__(self, actions):
        self.actions = actions
        self.alpha = 0.9  # learning rate
        self.gamma = 0.9  # discount factor
        self.epsilon = 0.5  # probability
        self.decay_factor = 0.99995
        self.v_table = pd.DataFrame(columns=['state value'], dtype=np.float64)
        self.v_table_final = pd.DataFrame(columns=['state value'], dtype=np.float64)

    # exploration and exploitation
    # def choose_action(self, observation):
    #     self.check_state_exist(observation)
    #     self.epsilon *= self.decay_factor  # epsilon greedy
    #     if np.random.random() < self.epsilon:
    #         action = np.random.choice(self.actions)
    #         print('action1: ', action)
    #     else:
    #         state_value = self.v_table.loc[observation]
    #         # state_value = state_value.reindex(np.random.permutation(state_value.index))
    #         # action = state_value.idxmax()
    #         # print('action2: ', action)
    #     return action

    # Function for learning and updating V-table with new knowledge
    def learning(self, state, reward, next_state):
        self.check_state_exist(next_state)
        v_current = self.v_table.loc[state]  # current state and action for that state
        if next_state != 'Goal' or next_state != 'Obstacle' or next_state != 'Rubik':
            v_target = reward + self.gamma * self.v_table.loc[next_state]
        else:
            v_target = reward
        self.v_table.loc[state] += self.alpha * (v_target - v_current)
        return self.v_table.loc[state]  # return a value that is Q-value

    def check_state_exist(self, state):
        if state not in self.v_table.index:
            self.v_table = self.v_table.append(pd.Series([0]*1, index=self.v_table.columns, name=state))

    def print_v_table(self):
        final_route = final_states()
        for i in range(len(final_route)):
            state = str(final_route[i])  # state = '[5.0, 40.0]'
            # Going through all indexes and checking
            for j in range(len(self.v_table.index)):
                if self.v_table.index[j] == state:
                    self.v_table_final.loc[state] = self.v_table.loc[state]

        f = open("data.txt", "a")
        f.write(f'Final Path V-table: {str(self.v_table_final)} \n')
        f.write(f'Full V-table:: {str(self.v_table)} \n')
        f.close()
