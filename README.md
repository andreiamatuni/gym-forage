# gym-forage

A foraging environment for OpenAI Gym.


### game mechanics

You're an agent in a 2D grid. Some of the cells in the grid have
resources, and others are empty. You need to move around and collect
food in order to survive. With each step, your energy level (i.e. currently
accumulated resources) will go down by some constant factor. Even if
you stay still, each step in the gym environment will deduct some
(smaller than if you make a move) amount from your accumulated resources.

You do not have perfect information. You can only see the cells that are
immediately surrounding you (i.e. POMDP's ftw).
