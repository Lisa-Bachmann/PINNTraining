# Generate flamelet data for pre-mixed hydrogen-air problems 
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

from Common.DataDrivenConfig import FlameletAIConfig 
from Data_Generation.DataGenerator_FGM import ComputeFlameletData

# Load FlameletAI configuration
Config = FlameletAIConfig("TableGeneration.cfg")

# Distribute flamelet data generation process over 20 cores.
ComputeFlameletData(Config, run_parallel=True, N_processors=50)