from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
sys.path.insert(0, '/home/adaptation/lberry/Documents/HUAWEI_scenarios/ppo_monicars/src')
from train import * 

main("two_lanes_two_way", 100, 0.9995, 0.98, 0.003, 20, 10, 1.0, False, 1, 8, obstacle = True)


env = Environment("two_lanes_two_way", obstacle = True)


env.reset()
obs_dim = 8
act_dim = 1  

done = False
while not done:
	accel_rand = np.random.normal(0,0.05)
	obs, reward, done = env.step([0, 0], npc_action = [[accel_rand,0]])
	agent_cord = np.array([obs[0],obs[1]])
	obstacle_cord = np.array([obs[4],obs[5]])
	distance = np.linalg.norm(obstacle_cord - agent_cord)
	print(obs)
	print 'distance is'
	print distance
	print obs
	env.clock.tick(global_var.FPS)

env.quit()
