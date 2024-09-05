# Optimize the progress variable definition and weights for hydrogen-air combustion
import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

from Common.DataDrivenConfig import FlameletAIConfig 
from Data_Processing.OptimizeProgressVariable import PVOptimizer


# Load FlameletAI configuration
Config = FlameletAIConfig("TableGeneration.cfg")

PVO = PVOptimizer(Config)


# Include additional variables in progress vector definition
PVO.SetAdditionalProgressVariables(["Temperature","Cp","Heat_Release","Y_dot_net-NO"])

# Set bounds for specific species
PVO.SetSpeciesBounds("H2",ub=0)
PVO.SetSpeciesBounds("O2",ub=0)
PVO.SetSpeciesBounds("H2O",lb=0)
PVO.SetSpeciesBounds("NO", lb=0)
PVO.SetCurveStepThreshold(1e-3)
PVO.SetNWorkers(1)
PVO.OptimizePV()

# Update config
Config.SetProgressVariableDefinition(PVO.GetOptimizedSpecies(),PVO.GetOptimizedWeights())
Config.SaveConfig("TableGeneration")

