from monicars import Environment
from monicars.variables import global_var
import numpy as np
import sys
sys.path.insert(0, '/home/adaptation/lberry/Documents/HUAWEI_scenarios/ppo_monicars/src')
from train import * 


def rew_func(obs):
	if obs[-1] == 1:
		rew = -1000
	elif obs[1] <= 10:
		rew = -1000
	else:
		rew = -1
	return rew

env_name = "two_lanes_two_way"
obs_dim = 4
act_dim = 1  
batch_size = 20
num_episodes = 1e5
gamma = 0.9995
lam = 0.98
HL1_mult = 10
Kl_targ = 0.003
make_plots = True
policy_log_var = 1

main(env_name, num_episodes, gamma, lam, Kl_targ, batch_size, HL1_mult, policy_log_var, make_plots, act_dim, obs_dim, obstacle = True, reward_function = rew_func, render = False)



test = False

if test:
	env = Environment(env_name, obstacle = True, reward_function = rew_func, render = False)


	env.reset()  

	# test env
	done = False
	while not done:
		accel_rand = np.random.normal(0,0.05)
		obs, reward, done = env.step([0, 0], npc_action = [[accel_rand,0]])
		agent_cord = np.array([obs[0],obs[1]])
		obstacle_cord = np.array([obs[4],obs[5]])
		distance = np.linalg.norm(obstacle_cord - agent_cord)

	env.quit()



def move(self, acc, heading):
    # Since this is one timestep, we do not need to multiply by time.
    self._speed += acc
    self._heading += heading
    self._heading = normalize_angle(self._heading)

    # Since this is one timestep, the speed is equal to the displacement.
    delta_x = self._speed * math.sin(self._heading)
    delta_y = self._speed * math.cos(self._heading)

    self._x += delta_x
    self._y += delta_y

    return (delta_x, delta_y, heading)


