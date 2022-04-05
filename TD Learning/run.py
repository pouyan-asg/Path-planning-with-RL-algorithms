from print_results import *


def main():
    total_steps = []
    total_rewards = []
    total_values = []
    episodes = 50000

    for episode in range(episodes):
        #print(episode)
        state = env.reset()  # return the coordination of the agent
        # print('state', str(state))
        step = 0
        value = 0
        reward_value = 0
        while True:
            env.refresh()
            action = env.policy(state)
            # print('action', action)
            next_state, reward, done = env.step(action)
            value += RL.learning(str(state), reward, str(next_state))
            state = next_state
            # print('next state', str(state))
            step += 1
            reward_value += reward

            if done:
                total_steps += [step]
                total_rewards += [reward_value]
                total_values +=[value]
                break

    env.final_path()
    plot.plot_reward(total_rewards)
    plot.plot_steps(total_steps)
    plot.plot_value(total_values)
    RL.print_v_table()


if __name__ == "__main__":
    env = Environment()
    RL = Temporal_Difference(actions=list(range(env.num_actions)))
    plot = Plot_Results()
    env.after(10, main)
    env.mainloop()
