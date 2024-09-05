import sys, os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '../../'))
sys.path.append(root_dir)

from Common.DataDrivenConfig import FlameletAIConfig 

Config = FlameletAIConfig()
Config.SetConfigName("TableGeneration")

# Hydrogen-air flamelets with equivalence ratio between 0.3 and 0.7
Config.SetFuelDefinition(["H2"],[1.0])
Config.SetOxidizerDefinition(["O2","N2"],[1.0,3.76])
Config.SetReactionMechanism("/home/bal1dev/simulations/FlameletAI_with_LUT_new/flameletAI_BitBucket/TestCases/FINAL_FLAMELETS_eq025075_T2801800_multicomponent/curran_2017.yaml")
Config.SetMixtureBounds(mix_lower=0.25, mix_upper=0.75)
Config.SetNpMix(100)
Config.SetUnbTempBounds(T_unb_lower=280, T_unb_upper=880)
Config.SetNpTemp(12)

# Enable preferential diffusion through selecting the "multicomponent" transport model.
Config.SetTransportModel('multicomponent')
Config.EnablePreferentialDiffusion(True)

Config.SetConcatenationFileHeader("fluid_data")

# Setting the Efimov progress variable definition.
#Nithin PV definition
#Config.SetProgressVariableDefinition(pv_species=['H2', 'H', 'O2', 'O', 'H2O', 'OH', 'H2O2', 'HO2'],\
#                                     pv_weights=[-7.36, -23.01, -2.04, -4.8, 1.83, -15.31, -57.02, 24.55])
#Optimized PV
#Config.SetProgressVariableDefinition(pv_species=['H2', 'H', 'O2', 'O', 'H2O', 'OH', 'H2O2', 'HO2', 'NO'],\
#                                     pv_weights=[-7.3437772976472928e+00, -2.6586185178380442e+05, -2.9678757360734093e-01, 1.5748141593823846e+04, 2.8380771899971786e+00, 6.2063051014852476e+02, -1.0024190164706480e-01, 3.2564541343910941e-01, 3.0221198390913902e+04])

#Evert PV
Config.SetProgressVariableDefinition(pv_species=['H2', 'H', 'O2', 'O', 'H2O', 'OH', 'H2O2', 'HO2', 'NO'],\
                                     pv_weights=[-3.4835431652983716e-02,-2.1680618539486902e+00,-2.4210581285717764e-07,-6.3818926560982009e-02,+3.9195719065410288e+00,-5.6422279047723407e+00,-3.7788863142476425e-02,-6.6673034302141415e-02,+7.0819342449909795e-01])


flamelet_data_dir = os.getcwd() + "/flamelet_data/"
if not os.path.isdir(flamelet_data_dir):
    os.mkdir(flamelet_data_dir)
Config.SetOutputDir(flamelet_data_dir) 
 
Config.PrintBanner()
Config.SaveConfig()
