import pandas as pd
from env import *


class SARSA:
    def __init__(self, actions):
        self.actions = actions
        self.alpha = 0.9  # learning rate
        self.gamma = 0.9  # discount factor
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)  # Creating Q-table with actions as columns
        self.q_table_final = pd.DataFrame(columns=self.actions, dtype=np.float64)

    # exploration and exploitation
    def choose_action(self, observation, epsilon):
        self.check_state_exist(observation)
        #epsilon *= self.decay_factor  # epsilon greedy
        # print(epsilon)
        if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(self.actions)  # choice randomly
                #value = self.q_table.loc[observation, action]
                # print('action1: ', action)
        else:
                state_action = self.q_table.loc[observation, :]
                #state_action = state_action.reindex(np.random.permutation(state_action.index))
                action = state_action.idxmax()
                # print('action2: ', action)
                #value = self.q_table.loc[observation, action]
        return action

    # Function for learning and updating Q-table with new knowledge
    def learning(self, state, action, reward, next_state, next_action):
        self.check_state_exist(next_state)
        q_current = self.q_table.loc[state, action]  # current state and action for that state
        if next_state != 'Goal' or next_state != 'Obstacle' or next_state != 'Rubik':
            q_target = reward + self.gamma * self.q_table.loc[next_state, next_action]
        else:
            q_target = reward
        # updating Q-table
        self.q_table.loc[state, action] += self.alpha * (q_target - q_current)
        return self.q_table.loc[state, action]  # return a value that is Q-value

    # Adding to the Q-table new states (pd.series generate 1-dimensional array)
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(pd.Series([0]*len(self.actions), index=self.q_table.columns, name=state))

    def print_q_table(self):
        final_route = final_states()
        for i in range(len(final_route)):
            state = str(final_route[i])  # state = '[5.0, 40.0]'
            # Going through all indexes and checking
            for j in range(len(self.q_table.index)):
                if self.q_table.index[j] == state:
                    self.q_table_final.loc[state, :] = self.q_table.loc[state, :]

        f = open("data.txt", "a")
        f.write(f'Final Path Q-table: {str(self.q_table_final)} \n')
        f.write(f'Full Q-table:: {str(self.q_table)} \n')
        f.close()
