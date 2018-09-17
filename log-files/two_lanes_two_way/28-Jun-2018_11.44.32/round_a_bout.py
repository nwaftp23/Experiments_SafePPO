from monicars import Environment
from monicars.variables import global_var
import numpy as np

env = Environment("round_a_bout")

env.reset()

done = False
while not done:
	accel_rand = np.random.normal(0,0.05)
	obs, reward, done = env.step([0, 0], npc_action = [[accel_rand,0]])
	env.clock.tick(global_var.FPS)

env.quit()