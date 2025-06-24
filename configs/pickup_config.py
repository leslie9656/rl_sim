from easydict import EasyDict as edict

pickup_config = edict()

pickup_config.render = True  # 是否渲染
pickup_config.robot_urdf = "/home/wang/workspace/rl_sim/assets/flexiv/flexiv.urdf"