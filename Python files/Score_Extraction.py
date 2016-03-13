__author__ = 'Euan Cockburn'
'speech personality project'
'File for reading and processing personality scores'

import csv
import glob

def ExtractScore():
	# Retrieve all the files from which information is to be extracted
	filenames = []
	
	for files in glob.glob("/home/euan/Documents/university/year4/speech_personality/SSPNet-Speaker-Personality-Corpus/Personality_Scores/*.csv"):
		filenames.append(files)

	# Set up a list to hold all of the values from the indicated files
	Contents = []
	
	# Begin loop to extract content from all files
	for name in filenames:
		# Open the file for reading in a buffer
		with open(name, 'rb') as f:
			# Start itterating over each row in the file
			reader = csv.reader(f)
			for row in reader:
				# Skip the first row
				if row[0] == "Clip_ID":
					continue
				# Append the current row to the set of contents
				Contents.append(row)

	# Now that all contents have been extracted process them to find average values for clips
	ProcessedScores = []
	while len(Contents) > 0:
		# Move first entry to temporary list
		entry = Contents[0]
		entry[1] = int(float(entry[1]))
		entry[2] = int(float(entry[2]))
		entry[3] = int(float(entry[3]))
		entry[4] = int(float(entry[4]))
		entry[5] = int(float(entry[5]))

		# Remove entry from Contents
		del Contents[0]
		# For each other entry in the Contents look for those with the same name as the extracted value
		i = 0
		while i < len(Contents):

			# If the entry represents the same clip as the contents
			if Contents[i][0] == entry[0]:
				# Add the values from Contents to those in entry
				entry[1] += int(float(Contents[i][1]))
				entry[2] += int(float(Contents[i][2]))
				entry[3] += int(float(Contents[i][3]))
				entry[4] += int(float(Contents[i][4]))
				entry[5] += int(float(Contents[i][5]))
				# Remove entry from Contents list
				del Contents[i]
				# Reset the i value to prevent skipped entries
				i = 0

			# Otherwise increment i
			else:
				i += 1

		# Now that all values for an entry have been summed they are divided to give the mean value
		j = 1
		while j < len(entry):
			entry[j] = int(float(entry[j])) / 11
			j += 1

		# Store these averaged values in a dictionary
		ProcessedScores.append({'Name':entry[0], 'Extraversion':entry[1], 'Agreeableness':entry[2], 'Conscientiousness':entry[3], 'Neuroticism':entry[4], 'Openness':entry[5]})

	return ProcessedScores