########################################
# This script creates a CustomAnt env object,
# and a baselines model object (PPO, A2C, etc)
# Evaluates (rolls out) the untrained model (random actions),
# then train the model and reevaulates it (rollout again).
# It saves both model rollouts with model.save.
########################################

import gym
import custom_ant
import numpy as np

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
from stable_baselines import A2C

import os

env = gym.make('InvertedPendulum-v2')

model = PPO2(MlpPolicy, env, verbose=1)

cumulative_reward_before = 0

#model.save(os.getcwd() + "/InvertedPendulum_model_untrained")

model.learn(total_timesteps=100000)

cumulative_reward_after = 0

#obs = env.reset()
#for i in range(1000):
#    action, _states = model.predict(obs)
#    obs, rewards, dones, info = env.step(action)
#    cumulative_reward_after += rewards

model.save(os.getcwd() + "/ant_model")

print("Total reward before learning:", cumulative_reward_before)
print("Total reward after learning:", cumulative_reward_after)