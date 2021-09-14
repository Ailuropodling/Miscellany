# Rainfall Interpolation
# (c) Ailuropodling, September 2021

import math


#original measurements with -1 at missing values.
rainfall = [0, 0.4, 0.6, -1, -1, 1.3, 1.7, 2.1, 2.9, -1, 3.4, 3.55, 3.7, -1, -1, 3.9]

#extrapolating measurements
for x in range(0,16):
    if(rainfall[x] == -1):
        prevIndex = x - 1
        nextIndex = x + 1
        while(rainfall[nextIndex] == -1): nextIndex += 1
        
        #intermediate values for testing
        rainfall[x] = (x - prevIndex)
        rainfall[x] *= (rainfall[nextIndex] - rainfall[prevIndex]) 
        rainfall[x] /= (nextIndex - prevIndex) 
        rainfall[x] += rainfall[prevIndex]
        #print(rainfall[x])

rainTime = float(input("Enter time to measure rainfall between 0 and 15: "))
rainVal = 0

#intermediate values for testing
x1 = rainfall[int(rainTime)] #truncated index value
x2 = rainTime % 1 #decimal portion of the value
x3 = rainfall[math.ceil(rainTime)] #next higher index value

#interpolated value
rainVal = x1 + x2 * (x3 - x1)

print("Rainfall at " + str(rainTime) + " hours: " + str(round(rainVal,2)) + " inches")
