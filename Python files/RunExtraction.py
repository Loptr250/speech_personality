__author__ = 'Euan Cockburn'
'speech personality project'
'File to run the openSMILe pitch configuration file'

import os

# Run the energy configuartion file
def FeatureExtract(files):
    # For each file
    for f in range(len(files)):
        # Create bash command
	bashCommand = "sudo SMILExtract -C /home/euan/Documents/university/year4/independant_project/speech_personality/MyConfig/gemaps/eGeMAPSv01a.conf -I " + files[f] + " -O /home/euan/Documents/university/year4/independant_project/speech_personality/CSVs/eGeMAPSv01a/" + os.path.basename(files[f]) + ".csv"
	# Run bash command
	os.system(bashCommand)