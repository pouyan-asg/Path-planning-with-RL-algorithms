from print_results import *


env = Environment()
QL = QLearning(actions=list(range(env.num_actions)))
SARSA = SARSA(actions=list(range(env.num_actions)))
DQL = Double_QLearning(actions=list(range(env.num_actions)))
plt = Plot_Results()


total_steps1 = []
total_rewards1 = []
total_values1 = []
total_steps2 = []
total_rewards2 = []
total_values2 = []
episodes = 500
epsilon1 = 0.1
decay_factor1 = 0.999
epsilon2 = 0.1
decay_factor2 = 0.999
epsilon3 = 0.8
decay_factor3 = 0.999


print('Q-learning')
for episode in range(episodes):
    state1 = env.reset()  # return the coordination of the agent
    step1 = 0
    value1 = 0
    reward_value1 = 0
    epsilon1 *= decay_factor1
    while True:
        env.refresh()
        action1 = QL.choose_action(str(state1), epsilon1)
        next_state1, reward1, done1 = env.step(action1)
        value1 += QL.learning(str(state1), action1, reward1, str(next_state1))
        state1 = next_state1
        step1 += 1
        reward_value1 += reward1

        if done1:
            total_steps1 += [step1]
            total_rewards1 += [reward_value1]
            total_values1 += [value1]
            break
env.final_path_Q()

print()
print('SARSA')
for episode in range(episodes):
    state2 = env.reset()  # return the coordination of the agent
    step2 = 0
    value2 = 0
    reward_value2 = 0
    epsilon2 *= decay_factor2
    action2 = SARSA.choose_action(str(state2), epsilon2)
    while True:
        env.refresh()
        next_state2, reward2, done2 = env.step(action2)
        next_action2 = SARSA.choose_action(str(next_state2), epsilon2)
        value2 += SARSA.learning(str(state2), action2, reward2, str(next_state2), next_action2)
        state2 = next_state2
        action2 = next_action2
        reward_value2 += reward2
        step2 += 1

        if done2:
            total_steps2 += [step2]
            total_rewards2 += [reward_value2]
            total_values2 += [value2]
            break
env.final_path_SARSA()

print()
print('Double Q-learning')
total_steps3 = []
total_rewards3 = []
total_values13 = []
total_values23 = []
value13 = 0
value23 = 0
for episode in range(episodes):
    state3 = env.reset()  # return the coordination of the agent
    step3 = 0
    reward_value3 = 0
    epsilon3 *= decay_factor3
    while True:
        env.refresh()
        action3 = DQL.choose_action(str(state3), epsilon3)
        next_state3, reward3, done3 = env.step(action3)
        value13, value23 = DQL.learning(str(state3), action3, reward3, str(next_state3))
        value13 += value13
        value23 += value23
        state3 = next_state3
        step3 += 1
        reward_value3 += reward3

        if done3:
            total_steps3 += [step3]
            total_rewards3 += [reward_value3]
            total_values13 += [value13]
            total_values23 += [value23]
            break

env.final_path_DQL()

plt.plot_reward(total_rewards1, total_rewards2, total_rewards3)
plt.plot_steps(total_steps1, total_steps2, total_steps3)
plt.plot_value(total_values1, total_values2, total_values13, total_values23)


env.after(1000)
env.mainloop()
