__author__ = 'Euan Cockburn'
'Speech personality project'
'Extract the file names for analysis'

import glob

# Function to retrieve all file names
def getfilenames():
    # Initialise list of files
    files = []

    # Retrieve all .wav files
    for f in glob.glob('/home/euan/Documents/Speech_personality/speech_personality/SSPNet-Speaker-Personality-Corpus/Audio_clips/*.wav'):
        files.append(f)
    
    return files

