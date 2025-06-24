"""pickup rl environment.
"""
import os
import sys
sys.path.insert(0,"../")
import numpy as np
import random
import time
import math
import gym
from gym import spaces
from gym.utils import seeding

from bullet_envs.Rizon4_env import Rizon4Env

class RLPickEnv(gym.Env):
    def __init__(self,config):
        self.config = config
        self.env_client = Rizon4Env(config)

        self.terminated = False

    def set_limitations(self):
        # 机械臂移动范围限制
        self.x_low_obs = 0.2
        self.x_high_obs = 0.7
        self.y_low_obs = -0.3
        self.y_high_obs = 0.3
        self.z_low_obs = 0
        self.z_high_obs = 0.55

        # 机械臂动作范围限制
        self.x_low_action = -0.4
        self.x_high_action = 0.4
        self.y_low_action = -0.4
        self.y_high_action = 0.4
        self.z_low_action = -0.6
        self.z_high_action = 0.3

    def set_space(self):
        # 动作空间
        self.action_space = spaces.Box(
            low=np.array([self.x_low_action, self.y_low_action, self.z_low_action]),
            high=np.array([self.x_high_action, self.y_high_action, self.z_high_action]),
            dtype=np.float32)

        # 状态空间
        self.observation_space = spaces.Box(
            low=np.array([self.x_low_obs, self.y_low_obs, self.z_low_obs + self.gripper_length]),
            high=np.array([self.x_high_obs, self.y_high_obs, self.z_high_obs + self.gripper_length]),
            dtype=np.float32)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        # 初始化时间步计数器
        self.step_counter = 0
        # 重置环境
        self.env_client.reset()

    def step(self):
        self.env_client.step()