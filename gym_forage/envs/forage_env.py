import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.classic_control import rendering

import logging

from .state_space import *
from .render import *

class ForageEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      self.action_space = spaces.Discrete(9)
      self.state_space = random_binomial_distribution()
      self.curr_x = 0
      self.curr_y = 0
      self.curr_view = np.zeros(shape=(3, 3), dtype='int16')
      self.max_x = self.state_space.shape[0] - 1
      self.max_y = self.state_space.shape[1] - 1
      self.state = None
      self.viewer = None
      self.resources = 10

      self.steps_beyond_done = None
      self.move_cost = 0.333
      self.still_cost = 0.111

      self._seed()

  def _step(self, action):
      assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

      new_x, new_y = move(action, self.max_x, self.max_y,
                          self.curr_x, self.curr_y)

      if action != 4:
          self.resources -= self.move_cost
      else:
          self.resources -= self.still_cost

      done = self.resources <= 0

      self.curr_x = new_x
      self.curr_y = new_y
      print("curr_x: {}".format(self.curr_x))
      print("curr_y: {}".format(self.curr_y))

      update_curr_view(self.state_space, self.curr_view,
                       self.curr_x, self.curr_y,
                       self.max_x, self.max_y)
    #   print("view after mutate\n")
    #   print(self.curr_view)

      if not done:
          reward = self.state_space[new_x, new_y]
      elif self.steps_beyond_done is None:
          self.steps_beyond_done = 0
          reward = 0.0
      else:
            if self.steps_beyond_done == 0:
                logger.warning("You are calling 'step()' even though this environment has already returned done = True. You should always call 'reset()' once you receive 'done = True' -- any further steps are undefined behavior.")
            self.steps_beyond_done += 1
            reward = 0.0

      self.resources += reward

      return self.curr_view, reward, done, {}

  def _seed(self, seed=None):
      self.np_random, seed = seeding.np_random(seed)
      return [seed]


  def _reset(self):
      self.curr_x, self.curr_y = self.np_random.randint(low=0,
                                                        high=self.state_space.shape[0],
                                                        size=2)
      print("curr_location:    [{}, {}]".format(self.curr_x, self.curr_y))
      print("val at curr loc:  {}".format(self.state_space[self.curr_x, self.curr_y]))

  def _render(self, mode='human', close=False):
      if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

      screen_width = 600
      screen_height = 600
      cell_width = screen_width/3.0

      if self.viewer is None:
          self.viewer = rendering.Viewer(screen_width, screen_height)
      else:
        render(self.viewer, self.curr_view, cell_width)

      print(self.state_space)
      return self.viewer.render(return_rgb_array = mode=='rgb_array')
