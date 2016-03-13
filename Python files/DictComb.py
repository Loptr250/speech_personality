__author__ = 'Euan Cockburn'
'speech personality project'
'main file for interacting with the program'

def CombineDict(features, scores, meta):
	
	i = 0
	Data = []
	sample_size = 640
	# For each individual recorded (a fixed number of 640)
	while i < sample_size:
		# Copy content of features dictionary at i
		Entry = features[i].copy()
		j = 0
		while j < sample_size:
			# When dictionary keys match in scores
			
			if scores[j]['Name'] == Entry['Name']:
				
				# Update Entry and remove item from list to speed future searches
				Entry.update(scores[j])
				del scores[j]
				break
			j += 1
		k = 0
		# Similar process to above
		while k < sample_size:
			
			if meta[k]['Name'] == Entry['Name']:
				
				Entry.update(meta[k])
				del meta[k]
				break

			k += 1
		# Place new combined dictionary on the list
		Data.append(Entry)
		i += 1

	return Data