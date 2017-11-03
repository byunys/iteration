def sum_outside(numbers):
	min = numbers[0]
	max = numbers[1]
	total = 0
	for i in range(3, len(numbers)):
		total += numbers[i]

	print min, max