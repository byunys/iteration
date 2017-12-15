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
	first_names.append(info[1])
	last_names.append(info[2])
	emails.append(info[3])
	genders.append(info[4])
	ip_address.append(info[5])


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

genders = split_genders()


'''
if sentence[i] == " ":
			new_sentence += (new_word + " ")
			new_word = ""
		else:
			new_word += sentence[i]
			if new_word == first_word:
				new_word = ""
				new_sentence += second_word
			elif new_word == second_word:
				new_word = ""
				new_sentence += first_word
'''

#alphabetitize
def alphabetitize():
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# dont need	i = 0
# dont need	j = 0
	x = 0
	letter_a = []
	letter_b = []
	letter_c = []
	letter_d = []
	letter_e = []
	letter_f = []
	letter_g = []
	letter_h = []
	letter_i = []
	letter_j = []
	letter_k = []
	letter_l = []
	letter_m = []
	letter_n = []
	letter_o = []
	letter_p = []
	letter_q = []
	letter_r = []
	letter_s = []
	letter_t = []
	letter_u = []
	letter_v = []
	letter_w = []
	letter_x = []
	letter_y = []
	letter_z = []
	for i in range(0, len(last_names)):
		each_last_name = last_names[i] #works
		new_last_name = "" #works
			
		#print each_last_name #works
		
		for j in range(0, len(each_last_name)):
			
			if each_last_name[j] == "'": #might not need
				new_last_name += each_last_name[j] + "'" #might not need
				new_last_name = ""
			else:
				new_last_name += each_last_name[j]
				
				for x in range(0, len(alphabet)):
					if each_last_name[j] == alphabet[x]:
						letter_a.append(last_names[i])
					else:
						x +=1


				if new_last_name == each_last_name:
					new_last_name = ""
		return new_last_name
			#for x in range(0, len(alphabet)):

			#	if each_last_name[j] == alphabet[x]:
			#		new_last_name += each_last_name[j]
			#		j += 1
			#		print new_last_name

			#	else:
			#		j += 1
#					x += 1
#					i += 1
					#if i > len(each_last_name):
					#	i -=1

	'''for i in range(0, len(last_names)):

		each_last_name = last_names[i]
		print each_last_name

		for j in each_last_name:

			if each_last_name[j] == "a":
			
				print "true"
			
			else:
				j += 1'''








'''
print """Alphabetitize a list of names, splitting the boys and girls into two separate lists.
"""

print "boys: ", genders[0]
print """
girls: """, genders[1]
'''
print last_names, """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
print alphabetitize()

#def test_data():
#	for i in range(0, len(names)):
#		print 


#Alphabetitize names

#variables
#conditionals         DONE
#functions            DONE
#lists                DONE
#iteration (cycling)  DONE
#abstraction