from print_results import *


def main():
    total_steps = []
    total_rewards = []
    total_values = []
    episodes = 50000
    epsilon = 0.5
    decay_factor = 0.99995

    for episode in range(episodes):
        print(episode)
        state = env.reset()  # return the coordination of the agent
        step = 0
        value = 0
        reward_value = 0
        epsilon *= decay_factor
        print(epsilon)
        action = RL.choose_action(str(state), epsilon)
        while True:
            env.refresh()
            next_state, reward, done = env.step(action)
            #print('next state:', next_state)
            next_action = RL.choose_action(str(next_state), epsilon)
            #if next_action != action:
            #print('next action:', next_action)
            value += RL.learning(str(state), action, reward, str(next_state), next_action)
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
    plot = Plot_Results()
    env.after(10, main)
    env.mainloop()
