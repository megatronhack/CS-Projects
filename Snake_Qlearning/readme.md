AI term project learns how to play snake game
================================

The solution uses Reinforcement Learning (Q-learning) approach.


Q-formula:
------ 
![formula](readme_images/Qequation.png)

Introduction of Q learning
------ 
* Observation of the environment
* Deciding how to act using some strategy
* Acting accordingly
* Receiving a reward or penalty
* Learning from the experiences and refining our strategy




Input
---------
- The Q matrix is filled wThe Q table updated 
- The Q table updated every time that the agent makes the move as an example below:
![Example](Qtable.png)
- Training phase, the agent will choose either max Q value or a random action


Training phase and output()
---------
- The process is iterated until the game is finished.
- The Q matrix is updated with games with the games that have played.


Reward table
------------

- +1 for finding red dot target
- -1 for hitting wall or tail

Network settings
----------------

Param | Value | Info
--- | --- | ---
LEARNING_RATE | 0.01 |
GAMMA | 0.95 | Discount rate
EPSILON | 0.01 | Exploration rate


Result
-------------

![Visualisation](snake.gif)

------

Agent is following shortest path towards goal after training using the most updated Q table.

