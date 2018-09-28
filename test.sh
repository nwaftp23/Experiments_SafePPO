#!/bin/bash
#SBATCH --account=def-dpmeger
#SBATCH --gres=gpu:1        # request GPU "generic resource"
#SBATCH --cpus-per-task=6   # maximum CPU cores per GPU request: 6 on Cedar, 16 on Graham.
#SBATCH --mem=32000M        # memory per node
#SBATCH --time=0-00:03      # time (DD-HH:MM)
#SBATCH --output=%x-%j.out  # %N for node name, %j for jobID

module load cuda cudnn python/2.7.14
nvidia-smi
source /home/nwaftp23/SafePPO/bin/activate
echo 'Hi'
python --version
pip freeze
python ./test-tensoflow.py
echo 'Bye'
