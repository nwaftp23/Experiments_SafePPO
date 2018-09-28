#!/bin/bash
#SBATCH --account=def-dpmeger
#SBATCH --gres=gpu:2              # Number of GPUs (per node)
#SBATCH --cpus-per-task=12         # CPU cores/threads
#SBATCH --mem=64000M               # memory (per node)
#SBATCH --time=0-04:30            # time (DD-HH:MM)
#SBATCH --output=speed_selection_%j.out

module load cuda cudnn
source /home/nwaftp23/SafePPO/bin/activate
python /home/nwaftp23/SafePPO/Experiments/speed_selection.py
