import matplotlib.pyplot as plt
import numpy as np


class Plots:

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