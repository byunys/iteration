#!/usr/bin/env python
import sys

data = open("cars.csv", 'r')
lines = data.readlines()

car_ids = []
car_makes = []
car_models = []
car_years = []
car_colors = []



for column in range(1, len(lines)):
	info = lines[column].rstrip().split(",")
	car_ids.append(info[0])
	car_makes.append(info[1])
	car_models.append(info[2])
	car_years.append(info[3])
	car_colors.append(info[4])

#for column in range(0, len(car_years)):
#	print car_ids[column], car_makes[column], car_models[column], car_years[column], car_colors[column]


def find_specific_year_car_models():
	car_models_2006 = []
	for i in range(0, len(car_years)):
		if float(car_years[i]) == 2006:
			car_models_2006.append(car_models[i])
	
	print car_models_2006
	return car_models_2006

def find_any_year_car_models():
	any_year = 2005
	car_models_years = []
	for i in range(0, len(car_years)):
		if float(car_years[i]) == any_year:
			car_models_years.append(car_models[i])
	print car_models_years
	return car_models_years

def find_toyotas_since_2000():
	total = 0
	for i in range(0, len(car_makes)):
		if float(car_years[i]) > 2000 and car_makes[i] == "Toyota":
			total += 1
	print total
	return total

#def find_most_popular_color():
	#total = 0
	#for i in range(0, len(car_colors)):
	#	if car_colors[i] > total:
	#		total += 1
	#print total
#	count_list = []

#	for i in range(0, len(car_colors)):
	#	i != 0
#		count = 0
#		each_color = car_colors[0]
#		if each_color == car_colors[i]:
			#count.car_colors[i] += 1
			#count += 1
#			count_list.append(each_color)
#			print len(count_list)
#	print count_list

	#for i in range(0, len(car_colors)):
	#	each_color = car_colors[i]
	#	count = 0
	#	if each_color in range(0, len(car_colors)):
	#		count += 1
	#	else:
	#		count = 1
	#print each_color



def find_most_popular_color():
	each_color = []
	for i in range(0, len(car_colors)):
		if car_colors[i] not in each_color:
			each_color.append(car_colors[i])
	print each_color
	
	total = 0
	count = []
	color_spot = 0
	
	for i in range(0, len(each_color)):
	
		for j in range(0, len(car_colors)):
			if each_color[i] == car_colors[j]:
				total += 1
	
		count.append(total)
		color_spot += 1
		total = 0
	
	print count

	current_maximum = count[0]
	for n in count:
		if n > current_maximum:
			current_maximum = n
	print current_maximum

	
	

#find_specific_year_car_models()
#find_any_year_car_models()
#find_toyotas_since_2000()
find_most_popular_color()