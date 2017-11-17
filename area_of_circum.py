import math


#find area of a square that circumscribes a circle

def diameter(circumference): #2 * pi * r
	diameter = circumference/math.pi
	return diameter

def square_area():
	area = diameter(16 * math.pi) * diameter(16 * math.pi)
	return area

print square_area()


#find area of a circle that cirumscribes a square, given one of the lengths

def diameter(side): #14
	diameter = math.sqrt(side**2 + side**2)
	return diameter

def circle_area(side):
	radius = diameter(side)/2
	area = math.pi * radius**2
	return area

print circle_area(14)


#find area of outside circle that circumscribes a triangle that circumscribes an inner circle
def radius(side):
	radius = (side/2)/math.cos(30)
	return radius

def outside_circle_area(side):
	area = math.pi * radius(side)**2
	return area

print outside_circle_area(13)