# from .state import *
# from .memory import *
# from .reward import *

from gym.envs.registration import register

register(
    id='forage-v0',
    entry_point='gym_forage.envs:ForageEnv',
)
