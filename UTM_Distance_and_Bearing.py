# UTM Distance and Bearing Calculator
# (c) Ailuropodling, August 2021

import math

utm1 = [float(input("Enter 1st Easting:\t")), 
	float(input("Enter 1st Northing:\t"))]
utm2 = [float(input("Enter 2nd Easting:\t")), 
	float(input("Enter 2nd Northing:\t"))]


def calcDist(utm1, utm2):
	distance = math.dist(utm1, utm2)
	return distance
    
def calcBear(utm1, utm2):
	dEast = (utm2[0] - utm1[0]) # Delta East
	dNorth = (utm2[1] - utm1[1]) # Delta North
	bearing = math.degrees(math.atan2(dEast, dNorth)) # CW
  
	if (bearing < 0): bearing += 360 # Angle between 0 and 360°
	return bearing
 
distance = round(calcDist(utm1, utm2), 2)
bearing = round(calcBear(utm1, utm2))

print ("\nYour distance and bearing: " + 
	str(distance) + "m at " + str(bearing) + "°")
