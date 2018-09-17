from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
sys.path.insert(0, '/home/adaptation/lberry/Documents/HUAWEI_scenarios/ppo_monicars/src')
from train import * 


def rew_func(obs, crash):
	if crash:
		rew = -1000
	elif obs[1]<= 10:
		rew = -1000
	else:
		rew = -1
	return rew

main("two_lanes_two_way", 200, 0.9995, 0.98, 0.003, 20, 10, 1.0, False, 1, 8, obstacle = True, reward_function = rew_func)


env = Environment("two_lanes_two_way", obstacle = True, reward_function = rew_func)


env.reset()
obs_dim = 8
act_dim = 1  

done = False
while not done:
	accel_rand = np.random.normal(0,0.05)
	obs, reward, done = env.step([0, 0], npc_action = [[-1,0]])
	agent_cord = np.array([obs[0],obs[1]])
	obstacle_cord = np.array([obs[4],obs[5]])
	distance = np.linalg.norm(obstacle_cord - agent_cord)
	print obs
	print done
	#print 'distance is'
	#print distance
	#print obs
	env.clock.tick(global_var.FPS)

env.quit()
