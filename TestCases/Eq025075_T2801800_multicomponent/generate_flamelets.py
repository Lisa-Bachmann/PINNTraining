# Generate flamelet data for pre-mixed hydrogen-air problems 
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../../..'))
sys.path.append(os.path.join(root_dir, 'flameletAI_BitBucket', 'Common'))
sys.path.append(os.path.join(root_dir, 'flameletAI_BitBucket', 'FlameletGeneration'))

print("sys.path:", sys.path)
import numpy as np 
from FlameletGenerators import FlameletGenerator_Cantera
from FlameletAIConfig import FlameletAIConfig 
from joblib import Parallel, delayed

# Number of CPUs used for flamelet data computation
N_processors = 100

# Load FlameletAI configuration
Config = FlameletAIConfig("hydrogen_refined.cfg")
mix_bounds = Config.GetMixtureBounds()
Np_unb_mix = Config.GetNpMix()

# Generate a lean range of equivalence ratio values for which to generate flamelet data
mixture_range = np.linspace(mix_bounds[0], mix_bounds[1], Np_unb_mix)

# Distribute flamelet data computation over processors

def ComputeFlameletData(mix_input):

    F = FlameletGenerator_Cantera(Config)
    F.AddFuzz(False)

    # Set Cantera transport mechanism.
    F.SetTransportMechanism("multicomponent")
    #F.SetTransportMechanism("unity-Lewis-number")
    F.ComputeFlameletsOnMixStatus(mix_input)

Parallel(n_jobs=N_processors)(delayed(ComputeFlameletData)(mix_status) for mix_status in mixture_range)
