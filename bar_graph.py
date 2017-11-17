import plotly
import plotly.plotly as py
import plotly.graph_objs as go

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


each_color = []

def find_each_color():
	for i in range(0, len(car_colors)):
		if car_colors[i] not in each_color:
			each_color.append(car_colors[i])
	print each_color


count = []

def find_number_of_each_color():

	total = 0
	color_spot = 0
	
	for i in range(0, len(each_color)):
	
		for j in range(0, len(car_colors)):
			if each_color[i] == car_colors[j]:
				total += 1
	
		count.append(total)
		color_spot += 1
		total = 0
	
	print count

print each_color
print count

#data = [go.Bar(
#			x = each_color,
#			y = count
#
#	)]

#plotly.offline.plot(data, filename = 'car_bar_graph')
####################################################################