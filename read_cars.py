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

find_specific_year_car_models()
find_any_year_car_models()