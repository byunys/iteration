# Make a local change
# Make another local change

# iteration pattern

# [1, 5, 7 , 8, 4, 3]

#test for git pull

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


