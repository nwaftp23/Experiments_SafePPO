from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
sys.path.insert(0, '/home/adaptation/lberry/Documents/HUAWEI_scenarios/ppo_monicars/src')
from train import * 


def rew_func(obs):
	if obs[1] <= 10:
		rew = -10000
	else:
		rew = -1
	return rew

env_name = "two_lanes"
obs_dim = 9
act_dim = 2  
batch_size = 20
num_episodes = 4000
gamma = 0.9995
lam = 0.98
HL1_mult = 10
Kl_targ = 0.003
make_plots = True
policy_log_var = 1


main(env_name, num_episodes, gamma, lam, Kl_targ, batch_size, HL1_mult, policy_log_var, make_plots, act_dim, obs_dim, obstacle = True, reward_function = rew_func, render = True)



test = True

if test:
	env = Environment(env_name, obstacle = True, reward_function = rew_func, render = True)


	env.reset()  

	# test env
	done = False
	while not done:
		accel_rand = np.random.normal(0,0.05)
		obs, reward, done = env.step([0, .1], npc_action = [[accel_rand,0]])
		agent_cord = np.array([obs[0],obs[1]])
		obstacle_cord = np.array([obs[4],obs[5]])
		distance = np.linalg.norm(obstacle_cord - agent_cord)
		print(env.on_road())
	env.quit()
