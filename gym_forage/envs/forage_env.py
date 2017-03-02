import gym
from gym import error, spaces, utils
from gym.utils import seeding

from .state_space import *

class ForageEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
      self.action_space = spaces.Discrete(9)
      self.landscape = random_binomial_distribution()
      self.curr_x = 0
      self.curr_y = 0
      self.max_x = self.landscape.shape[0] - 1
      self.max_y = self.landscape.shape[1] - 1
      self.state = None
      self.viewer = None
      self.resources = 10
    #   self.curr_view = np.zeros(shape=(3, 3), dtype=np.int8)

      self._seed()

  def _step(self, action):
      assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

      new_x, new_y = move(action, self.max_x, self.max_y,
                          self.curr_x, self.curr_y)

      new_val = self.landscape[new_x, new_y]

      done = self.resources <= 0

      self.curr_x = new_x
      self.curr_y = new_y
      print("curr_x: {}".format(self.curr_x))
      print("curr_y: {}".format(self.curr_y))

      self.curr_view = self.landscape[self.curr_x-1:self.curr_x+2, self.curr_y-1:self.curr_y+2]
      self.resources += new_val

      return self.curr_view, new_val, done, {}

  def _seed(self, seed=None):
      self.np_random, seed = seeding.np_random(seed)
      return [seed]


  def _reset(self):
      self.curr_x, self.curr_y = self.np_random.randint(low=0,
                                                        high=self.landscape.shape[0],
                                                        size=2)
      print("curr_location:    [{}, {}]".format(self.curr_x, self.curr_y))
      print("val at curr loc:  {}".format(self.landscape[self.curr_x, self.curr_y]))

  def _render(self, mode='human', close=False):
      print(self.landscape)
