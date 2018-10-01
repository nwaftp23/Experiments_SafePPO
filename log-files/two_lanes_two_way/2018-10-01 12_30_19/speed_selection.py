import sys
sys.path.append('')
from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
# nicer than specifying the exact parent directory regardless of the computer
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
# python 2 annoyance
ppo_path = '/ppo/src'
sys.path.insert(0,parentdir)
sys.path.insert(0,(parentdir+ppo_path)) 
from train import * 



def rew_func(obs):
	if obs[1] <= 10:
		rew = -500
	else:
		rew = -1
	return rew

env_name = "two_lanes_two_way"
obs_dim = 8
act_dim = 1  
batch_size = 20
num_episodes = 2000
gamma = 0.995
lam = 0.98
HL1_mult = 10
Kl_targ = 0.003
make_plots = True
policy_log_var = 1
render_decision = True


main(env_name, num_episodes, gamma, lam, Kl_targ, batch_size, HL1_mult, policy_log_var, make_plots, act_dim, 
	obs_dim, obstacle = True, reward_function = rew_func, render = render_decision)



test = False

if test:
	env = Environment(env_name, obstacle = True, reward_function = rew_func, render = True)


	env.reset()  

	# test env
	done = False
	while not done:
		accel_rand = np.random.normal(0,0.05)
		obs, reward, done = env.step([0, 0], npc_action = [[accel_rand,0]])
		agent_cord = np.array([obs[0],obs[1]])
		obstacle_cord = np.array([obs[4],obs[5]])
		distance = np.linalg.norm(obstacle_cord - agent_cord)
		print(obs)
		print(obs[4:6])
	env.quit()



