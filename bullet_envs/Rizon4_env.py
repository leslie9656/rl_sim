"""Bullet environments for flexiv Rizon4.

"""

import pybullet as p
import pybullet_data
import numpy as np
import os
import math
import random

class Rizon4Env():
    def __init__(self,config):
        self.config = config

        self.connect()
        self.robot_id = self.load_robot()

    def connect(self):
        if self.config.render:
            p.connect(p.GUI)
        else:
            p.connect(p.DIRECT)

        # 设置重力
        p.setGravity(0, 0, -9.81)
    
    def load_robot(self):
        # 加载机械臂模型
        robot_id = p.loadURDF(
            fileName=self.config.robot_urdf,
            basePosition=[0.0, 0.0, 0.0],
            baseOrientation=p.getQuaternionFromEuler([0.0, 0.0, 0.0]),
            globalScaling=1.0)
        
        return robot_id

    def get_joint_index(self):
        pass

    def get_link_index(self):
        pass
    
    def get_joint_pose(self):
        pass

    def get_flange_pose(self):
        pass

    def set_joints(self):
        pass

    def set_tcp_pose(self):
        pass

    def set_camera_pose(self):
        pass

    def step(self):
        p.stepSimulation()
        pass

    def reset(self):
        p.resetSimulation()

    def visual_workspace(self):
        # 状态空间的限制空间可视化，以白线标识
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_low_obs, self.config.y_low_obs, 0],
            lineToXYZ=[self.config.x_low_obs, self.config.y_low_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_low_obs, self.config.y_high_obs, 0],
            lineToXYZ=[self.config.x_low_obs, self.config.y_high_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_high_obs, self.config.y_low_obs, 0],
            lineToXYZ=[self.config.x_high_obs, self.config.y_low_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_high_obs, self.config.y_high_obs, 0],
            lineToXYZ=[self.config.x_high_obs, self.config.y_high_obs, self.config.z_high_obs])

        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_low_obs, self.config.y_low_obs, self.config.z_high_obs],
            lineToXYZ=[self.config.x_high_obs, self.config.y_low_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_low_obs, self.config.y_high_obs, self.config.z_high_obs],
            lineToXYZ=[self.config.x_high_obs, self.config.y_high_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_low_obs, self.config.y_low_obs, self.config.z_high_obs],
            lineToXYZ=[self.config.x_low_obs, self.config.y_high_obs, self.config.z_high_obs])
        p.addUserDebugLine(
            lineFromXYZ=[self.config.x_high_obs, self.config.y_low_obs, self.config.z_high_obs],
            lineToXYZ=[self.config.x_high_obs, self.config.y_high_obs, self.config.z_high_obs])

    def add_object(self,urdf_path,pose_6d):
        # 添加障碍物
        p.loadURDF(urdf_path,
                   basePosition=pose_6d[:3],
                   baseOrientation=p.getQuaternionFromEuler(pose_6d[3:]),
                   globalScaling=1.0)
    
