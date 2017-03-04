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

    if action == 0:
        if old_x > 0:
            new_x = old_x - 1
        if old_y > 0:
            new_y = old_y - 1
    elif action == 1:
        if old_x > 0:
            new_x = old_x - 1
    elif action == 2:
        if old_x > 0:
            new_x = old_x - 1
        if old_y < max_y:
            new_y = old_y + 1
    elif action == 3:
        if old_y > 0:
            new_y = old_y - 1
    elif action == 5:
        if old_y < max_y:
            new_y = old_y + 1
    elif action == 6:
        if old_x < max_x:
            new_x = old_x + 1
        if old_y > 0:
            new_y = old_y - 1
    elif action == 7:
        if old_x < max_x:
            new_x = old_x + 1
    elif action == 8:
        if old_x < max_x:
            new_x = old_x + 1
        if old_y < max_y:
            new_y = old_y + 1

    return new_x, new_y

def update_curr_view(space, view, x, y, max_x, max_y):
    if x == 0:
        view[0,:] = -1000
        if y == 0:
            view[:,0] = -1000
            view[1,1] = space[x, y].copy()
            view[2,1] = space[x+1, y].copy()
            view[1,2] = space[x, y+1].copy()
            view[2,2] = space[x+1, y+1].copy()
        elif y == max_y:
            view[:,2] = -1000
            view[1, 1] = space[x, y].copy()
            view[2, 1] = space[x+1, y].copy()
            view[1, 0] = space[x, y-1].copy()
            view[2, 0] = space[x+1, y-1].copy()
        else:
            view[1,:] = space[x,y-1:y+2].copy()
            view[2,:] = space[x+1,y-1:y+2].copy()
    elif x == max_x:
        view[2,:] = -1000
        if y == max_y:
            view[:,2] = -1000
            view[1, 1] = space[x, y].copy()
            view[0, 1] = space[x-1, y].copy()
            view[0, 0] = space[x-1, y-1].copy()
            view[1, 0] = space[x, y-1].copy()
        elif y == 0:
            view[:,0] = -1000
            view[1, 1] = space[x, y].copy()
            view[0, 1] = space[x-1, y].copy()
            view[0, 2] = space[x-1, y+1].copy()
            view[1, 2] = space[x, y+1].copy()
        else:
            view[0,:] = space[x-1,y-1:y+2].copy()
            view[1,:] = space[x,y-1:y+2].copy()
    elif y == 0:
        view[:,0] = -1000
        if x == 0:
            view[0,:] = -1000
            view[1,1] = space[x, y].copy()
            view[2,1] = space[x+1, y].copy()
            view[1,2] = space[x, y+1].copy()
            view[2,2] = space[x+1, y+1].copy()
        else:
            view[:,1] = space[x-1:x+2,y].copy()
            view[:,2] = space[x-1:x+2,y+1].copy()
    elif y == max_y:
        view[:,0] = space[x-1:x+2,y-1].copy()
        view[:,1] = space[x-1:x+2,y].copy()
        view[:,2] = -1000
    else:
        view[:] = space[x-1:x+2, y-1:y+2].copy()
    # print('final view: \n\n')
    # print(view)
    # print("\n")


def random_binomial_distribution(p=0.4, shape=(10, 10)):
    return np.random.binomial(1, p, size=shape)

def rand_distribution(shape=(10, 10), sigma=0.5, mu=0):
    return sigma * np.random.randn(*shape) + mu
