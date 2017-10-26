# Make a local change
# Make another local change

# iteration pattern

# [1, 5, 7 , 8, 4, 3]

#test to see if I know how to commit
# Make a new change

def iterate(list):
	# standard for loop with range
	for i in range(0, len(list)):
	 	print list[i] #print the list at spot i
	 	# i = spot

	# for each loop
	for item in list:
		print item
		# item = value

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

def sum(scores):
	total = 0
	for n in scores:
		total += n

	return total			

def min(scores):
	current_min = scores[0]
	for n in scores:
		if n < current_min:
			current_min = n
	return current_min


def find_average(scores):
	average = sum(scores)
	for i in range(0, len(list)):
		print average/i

def find_filtered_average(scores):
	average = sum(scores) - (current_min + current_min)
	for i in range(0, len(list)):
		print average/i
