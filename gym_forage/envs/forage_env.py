import gym
from gym import error, spaces, utils
from gym.utils import seeding

from .state_space import *

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

      self._seed()

  def _step(self, action):
      assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))

      new_x, new_y = move(action, self.max_x, self.max_y,
                          self.curr_x, self.curr_y)

      new_val = self.state_space[new_x, new_y]

      done = self.resources <= 0

      self.curr_x = new_x
      self.curr_y = new_y
      print("curr_x: {}".format(self.curr_x))
      print("curr_y: {}".format(self.curr_y))

      # I realize this is ugly and stupid.....just need to get something working
      if self.curr_x == 0:
          self.curr_view[0,:] = -1000
          if self.curr_y == 0:
              self.curr_view[:,0] = -1000
              self.curr_view[1,1] = self.state_space[self.curr_x, self.curr_y].copy()
              self.curr_view[2,1] = self.state_space[self.curr_x+1, self.curr_y].copy()
              self.curr_view[1,2] = self.state_space[self.curr_x, self.curr_y+1].copy()
              self.curr_view[2,2] = self.state_space[self.curr_x+1, self.curr_y+1].copy()
          elif self.curr_y == self.max_y:
              self.curr_view[:,2] = -1000
              self.curr_view[1, 1] = self.state_space[self.curr_x, self.curr_y].copy()
              self.curr_view[2, 1] = self.state_space[self.curr_x+1, self.curr_y].copy()
              self.curr_view[1, 0] = self.state_space[self.curr_x, self.curr_y-1].copy()
              self.curr_view[2, 0] = self.state_space[self.curr_x+1, self.curr_y-1].copy()
          else:
              self.curr_view[1,:] = self.state_space[self.curr_x,self.curr_y-1:self.curr_y+2].copy()
              self.curr_view[2,:] = self.state_space[self.curr_x+1,self.curr_y-1:self.curr_y+2].copy()
      elif self.curr_x == self.max_x:
         self.curr_view[0,:] = self.state_space[self.curr_x-1,self.curr_y-1:self.curr_y+2].copy()
         self.curr_view[1,:] = self.state_space[self.curr_x,self.curr_y-1:self.curr_y+2].copy()
         self.curr_view[2,:] = -1000
      elif self.curr_y == 0:
          self.curr_view[:,0] = -1000
          if self.curr_x == 0:
              self.curr_view[0,:] = -1000
              self.curr_view[1,1] = self.state_space[self.curr_x, self.curr_y].copy()
              self.curr_view[2,1] = self.state_space[self.curr_x+1, self.curr_y].copy()
              self.curr_view[1,2] = self.state_space[self.curr_x, self.curr_y+1].copy()
              self.curr_view[2,2] = self.state_space[self.curr_x+1, self.curr_y+1].copy()
          else:
              self.curr_view[:,1] = self.state_space[self.curr_x-1:self.curr_x+2,self.curr_y].copy()
              self.curr_view[:,2] = self.state_space[self.curr_x-1:self.curr_x+2,self.curr_y+1].copy()
      elif self.curr_y == self.max_y:
          self.curr_view[:,0] = self.state_space[self.curr_x-1:self.curr_x+2,self.curr_y-1].copy()
          self.curr_view[:,1] = self.state_space[self.curr_x-1:self.curr_x+2,self.curr_y].copy()
          self.curr_view[:,2] = -1000
      else:
          self.curr_view = self.state_space[self.curr_x-1:self.curr_x+2, self.curr_y-1:self.curr_y+2].copy()

      self.resources += new_val

      return self.curr_view, new_val, done, {}

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
      print(self.state_space)
