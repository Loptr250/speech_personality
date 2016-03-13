__author__ = 'Euan Cockburn'
'speech personality project'
'File for reading and processing meta data'

import csv
import glob

def ExtractMeta():

	# Retrieve the name of the file with data to be extracted.
	filename = "/home/euan/Documents/university/year4/speech_personality/SSPNet-Speaker-Personality-Corpus/Metadata/Metadata.csv"
	
	# List to hold contents of files
	content = []

	# Open file to extract content
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			# Skip the first row
			if row[0] == "Clip_ID":
				continue

			content.append({'Name':row[0], 'Speak_ID':row[1], 'Gender':row[2], 'Role':row[3]})
	
	return content
