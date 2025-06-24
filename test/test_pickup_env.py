import sys
sys.path.insert(0, "../")
import time
from rl_envs.pickup_env import RLPickEnv
from configs.pickup_config import pickup_config

if __name__ == "__main__":
    # 创建环境
    env = RLPickEnv(pickup_config)
    
    while True:
        env.step()
        time.sleep(0.01)
    # # 设置限制
    # env.set_limitations()
    
    # # 设置动作空间和状态空间
    # env.set_space()
    
    # # 重置环境
    # obs = env.reset()
    
    # print("Initial Observation:", obs)
    
    # # 进行一次随机动作
    # action = env.action_space.sample()
    # print("Random Action:", action)
    
    # # 执行动作并获取新的观察结果
    # obs, reward, done, info = env.step(action)
    
    # print("New Observation:", obs)
    # print("Reward:", reward)
    # print("Done:", done)
    # print("Info:", info)