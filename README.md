# Global Path Planning of WALL-E with Reinforcement Learning Algorithms to reach EVE!

## Introduction

This project aims to test various Reinforcement Learning (RL) algorithms for the global path planning of a mobile robot. The environment is designed based on the **WALL-E** animation, and the tested algorithms include Q-learning, SARSA, TD(0) learning, and Double Q-learning. Temporal Difference (TD) learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas. Like Monte Carlo methods, TD methods can learn directly from raw experience without modelling the environment’s dynamics. Like DP, TD methods update estimates based in part on other learned estimates without waiting for a final outcome (they bootstrap).

## Environment

<p align="justify">
The environment is created based on WALL-E's popular animation. In this environment, the WALL-E wants to reach the goal that is the EVE robot, but there are numerous obstacles in the path that it must avoid.
  </p>

<p align="justify">
The environment size is 15 * 15 in which each square is 40 * 40 pixels, and there are 52 obstacles inside it. Except for two robots (WALL-E and EVE), the obstacles are trees, buildings, garbage, road signs, a plant in the boot (based on animation) and a Rubik's Cube. The upside left corner (the agent starting position) is (0, 0) and going to the right and down is +X and +Y, respectively. For example, two steps to the right and one step to the down move the agent to [80, 40].
  </p>

In addition, the environment is designed with *Tkinter*, a standard Python interface to the Tcl/Tk GUI toolkit. Moreover, *Pandas* library for working with tables in algorithms, *Numpy* package for scientific computing and *Matplotlib* plotting library are used. Below figure shows an screenshot of the environment. The position of obstacles and the blocking area around the goal are considered in a way not to be easy for the agent to find an optimal path.

<img src="https://drive.google.com/uc?export=view&id=1K1erGU7y1feCwsHUE8XyMp5JHNlTXHOU" width="500" height="200" alt="RL process" align="middle">

This RL environment is modelled with the Markov decision process (MDP), in which state, action and reward sets are *S*, *A* and *R*. The environmental dynamics would be a set of probabilities *p(s', r | s, a)* for all states, actions and rewards. However, the testing environment is deterministic, and there are no stochastic actions.

<p align="justify">
The agent (WALL-E) can go up, down, right or left to reach the final goal in training mode. Each time the agent hits an obstacle, it will receive a -5 reward, and the system will reset to the initial point. If the robot reaches the goal, it will receive a massive reward of +100, and the reward is zero for other movements. According to animation, the interest of the WALL-E in a Rubik's cube is considered a motivation. It is not the goal, but it has a -1 reward. Solving this problem can be a good evaluation for some popular RL algorithms regarding the number of obstacles, especially around the goal, environment size and motivation between the path.
  </p>
