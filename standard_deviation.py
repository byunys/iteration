def standard_deviation(scores):
	mean_value = mean(scores)
	for i in range(0, len(scores)):
		scores[i] -= mean_value
		scores[i] = scores[i] * scores[i]
		mean_value = sum(scores[i])/len(scores)
#		new_sum += scores[i]
		
	print mean_value

def mean(scores):
	mean = sum(scores)/len(scores)
	return mean
	#mean = 75

def sum(scores):
	total = 0
	for n in scores:
		total += n

	return total