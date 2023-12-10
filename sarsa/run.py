'''This is the main file. When you run it, the agent start training process.'''

from environment import Environment
from algo_sarsa import SARSA
from plot_results import Plots


def main():

    total_steps = []
    total_rewards = []
    total_values = []
    episodes = 10000

    for episode in range(episodes):
        state = env.reset()  # it returns the coordination of the agent
        step = 0
        value = 0
        reward_value = 0
        action = RL.choose_action(str(state))
        while True:
            env.refresh()
            next_state, reward, done = env.step(action)
            next_action = RL.choose_action(str(next_state))
            value += RL.learning(str(state), action, reward,
                                 str(next_state), next_action)
            state = next_state
            action = next_action
            reward_value += reward
            step += 1

            if done:
                total_steps += [step]
                total_rewards += [reward_value]
                total_values += [value]
                break

    env.final_path()
    plot.plot_reward(total_rewards)
    plot.plot_steps(total_steps)
    plot.plot_value(total_values)
    RL.print_q_table()


if __name__ == "__main__":
    env = Environment()
    RL = SARSA(actions=list(range(env.num_actions)))
    plot = Plots()
    env.after(10, main)
    env.mainloop()
