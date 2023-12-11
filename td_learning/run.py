'''This is the main file. When you run it, the agent start training process.'''

from environment import Environment
from algo_td0 import TemporalDifference
from plot_results import Plots


def main():
    total_steps = []
    total_rewards = []
    total_values = []
    episodes = 20000

    for episode in range(episodes):
        state = env.reset()
        step = 0
        value = 0
        reward_value = 0
        while True:
            env.refresh()
            action = env.policy(state)
            next_state, reward, done = env.step(action)
            value += RL.learning(str(state), reward, str(next_state))
            state = next_state
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
    RL.print_v_table()


if __name__ == "__main__":
    env = Environment()
    # RL = TemporalDifference(actions=list(range(env.num_actions)))
    RL = TemporalDifference()
    plot = Plots()
    env.after(10, main)
    env.mainloop()
