import matplotlib.pyplot as plt
import numpy as np


class Plots:

    def plot_reward(self, reward1, reward2, reward3):
        plt.close()
        plt.plot(np.arange(len(reward1)), reward1, 'b')
        plt.plot(np.arange(len(reward2)), reward2, 'r')
        plt.plot(np.arange(len(reward3)), reward3, 'g')
        plt.xlabel('Episodes')
        plt.ylabel('Reward')
        plt.legend(['q-learning', 'sarsa', 'double q-learning'])
        plt.grid()
        plt.savefig('rewardcliff.png')
        plt.show()

    def plot_steps(self, steps1, steps2, steps3):
        plt.close()
        plt.plot(np.arange(len(steps1)), steps1, 'b')
        plt.plot(np.arange(len(steps2)), steps2, 'r')
        plt.plot(np.arange(len(steps3)), steps3, 'g')
        plt.xlabel('Episodes')
        plt.ylabel('Steps')
        plt.legend(['q-learning', 'sarsa', 'double q-learning'])
        plt.grid()
        plt.savefig('stepscliff.png')
        plt.show()

    def plot_value(self, value1, value2, value31, value32):
        plt.close()
        plt.plot(np.arange(len(value1)), value1, 'b')
        plt.plot(np.arange(len(value2)), value2, 'r')
        plt.plot(np.arange(len(value31)), value31, 'g')
        plt.plot(np.arange(len(value32)), value32, 'black')
        plt.xlabel('Episodes')
        plt.ylabel('Q-Values')
        plt.legend(['q-learning',
                    'sarsa',
                    'double q-learning 1',
                    'double q-learning 2'])
        plt.grid()
        plt.savefig('valuescliff.png')
        plt.show()
