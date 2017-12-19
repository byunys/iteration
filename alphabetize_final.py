#!/usr/bin/env python
import sys

data = open("names.csv", 'r')
lines = data.readlines()

first_names = []
last_names = []
emails = []
genders = []

for column in range(1, len(lines)):
	info = lines[column].rstrip().split(",")
	first_names.append(info[1])
	last_names.append(info[2])
	emails.append(info[3])
	genders.append(info[4])


#separate boys and girls


def split_genders():
	boys = []
	girls = []

	for i in range(0, len(genders)):
		if genders[i] == "Male":
			boys.append(first_names[i] + " " + last_names[i])
		elif genders[i] == "Female":
			girls.append(first_names[i] + " " + last_names[i])
	return [boys, girls]

genders_full_name = split_genders()


def alphabetize_sorted_genders():
	boys_last_names = []
	girls_last_names = []

	for i in range(0, len(genders)):
		if genders[i] == "Male":
			boys_last_names.append(last_names[i] + ", " + first_names[i])
		elif genders[i] == "Female":
			girls_last_names.append(last_names[i] + ", " + first_names[i])
	return[sorted(boys_last_names), sorted(girls_last_names)]

alphabetized_genders_last_names = alphabetize_sorted_genders()




print """This function will alphabetize a list of names, splitting the boys and girls into two separate lists.

It will alphabetize by the last names but print the first and last name both.
"""

print "List of all last names: ", last_names, """

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

print "boys: ", genders_full_name[0]

print """
girls: """, genders_full_name[1]

print ""

print "Alphabetized list of boys (last name, first name): ", alphabetized_genders_last_names[0]
print ""
print "Alphabetized list of girls (last name, first name): ", alphabetized_genders_last_names[1]
