import subprocess
import os, csv




folder_path = '/home/bal1dev/simulations/FlameletAI_with_LUT_new/flameletAI_BitBucket/TestCases/FINAL_FLAMELETS_eq025075_T2801800_multicomponent'  # Replace with the actual path to your scripts folder


scripts = ['generate_config.py', 'generate_flamelets.py','collect_flamelet_data.py', 'generate_LUT.py'] 
for script in scripts:
 script_path = folder_path + '/' + script
 subprocess.run(['python', script_path])
 print(f"The script {scripts} has been run.")
script_path = folder_path + '/generate_config.py'
