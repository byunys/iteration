#!/usr/bin/env python
import sys

data = open("names.csv", 'r')
lines = data.readlines()

first_names = []
last_names = []
emails = []
genders = []
ip_address = []


for column in range(1, len(lines)):
	info = lines[column].rstrip().split(",")
	first_names.append(info[0])
	last_names.append(info[1])
	emails.append(info[2])
	genders.append(info[3])
	ip_address.append(info[4])


def split_genders():
	boys = []
	girls = []

	for gender in range(0, len(genders)):
		if genders[gender] == "Male":
			boys.append(first_names[gender])
	return boys


print split_genders()
#def test_data():
#	for i in range(0, len(names)):
#		print 


#Alphabetitize names

#Use each of these computing concepts:
#variables
#conditionals
#functions
#lists
#iteration (cycling)
#abstraction -> Read the answer to this Stack Overflow discussion for an explanation