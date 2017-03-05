import numpy as np

def move(action, max_x, max_y,
         old_x, old_y):
    """
    the action space for
    the next step (agent
    is currently at 4):

         |0|1|2|
         |3|4|5|
         |6|7|8|

    """
    new_x = old_x
    new_y = old_y

    if action < 3 and old_x > 0:
        new_x -= 1
    elif action > 5 and old_x < max_x:
        new_x += 1

    if action % 3 == 0 and old_y > 0:
        new_y -= 1
    elif action % 3 == 2 and old_y < max_y:
        new_y += 1

    return new_x, new_y

def update_curr_view(space, view, x, y, max_x, max_y):
    for i in xrange(0, 3):
        for j in xrange(0, 3):
            if y == 0 and j == 0 or y == max_y and j == 2 or x == 0 and i == 0 or x == max_x and i == 2:
                view[i, j] = -1000
            else:
                view[i, j] = space[x+i-1, y+j-1].copy()


def random_binomial_distribution(p=0.3, shape=(5, 5)):
    return np.random.binomial(1, p, size=shape)

def rand_distribution(shape=(10, 10), sigma=0.5, mu=0):
    return sigma * np.random.randn(*shape) + mu
