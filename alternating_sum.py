def alternating_sum(numbers):
	total = 0
	for i in range(0, len(numbers)):
		if i == 0 or i%2 == 1:
			total += numbers[i]
		else:
			total -= numbers[i]
	print "The alternating sum is ", total
	return total