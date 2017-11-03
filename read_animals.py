#!/usr/bin/env python
import sys

data = open("animals.csv", 'r')
lines = data.readlines()

animal_names = []
animal_ratings = []
animal_countries = []

for row in range(1, len(lines)):
	info = lines[row].rstrip().split(",") # [Bird, 88]
	animal_names.append(info[0])
	animal_ratings.append(float(info[1]))
	animal_countries.append(info[2])
# animals = lines[0].split(",")

for row in range(0, len(animal_names)):
	print animal_names[row], " is rated ", animal_ratings[row], " and is like in ", animal_countries[row]