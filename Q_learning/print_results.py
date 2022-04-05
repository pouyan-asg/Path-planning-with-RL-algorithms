import matplotlib.pyplot as plt
from algo_Q_learning import *

class Plot_Results:
    def plot_reward(self, reward):
        plt.close()
        plt.plot(np.arange(len(reward)), reward, 'b')
        plt.title('Episodes vs Reward')
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.grid()
        plt.savefig('reward.png')
        plt.show()

    def plot_steps(self, steps):
        plt.close()
        plt.plot(np.arange(len(steps)), steps, 'r')
        plt.title('Episodes vs Steps')
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.grid()
        plt.savefig('steps.png')
        plt.show()

    def plot_value(self, value):
        plt.close()
        plt.plot(np.arange(len(value)), value, 'g')
        plt.title('Episodes vs Values')
        plt.xlabel('Episodes')
        plt.ylabel('Q-Values')
        plt.grid()
        plt.savefig('value.png')
        plt.show()

    # def __init__(self, actions):
    #     self.q_table_final = pd.DataFrame(columns=actions, dtype=np.float64)
    #     self.RL = QLearning(actions)
    #
    # def print_q_table(self):
    #     self.q_table = self.RL.q_table()
    #     final_route = final_states()
    #     # selecting final states and actions from Q table by final route in 'env.py'
    #     for i in range(len(final_route)):
    #         state = str(final_route[i])  # state = '[5.0, 40.0]'
    #         for j in range(len(self.q_table.index)):
    #             if self.q_table.index[j] == state:  # q_table.index[j] return the state with index j (row)
    #                 self.q_table_final.loc[state, :] = self.q_table.loc[state, :]
    #     print()
    #     print('Final Q-table:')
    #     print(self.q_table_final)
    #     print()
    #     print('Full Q-table:')
    #     print(self.q_table)