# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:43:17 2020

@author: Satyanarayana
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d")

# For plotting the 3 lines
def plot_lines(x,y,z,k):

   ax.plot3D(x, y, z, k)


# direction of line1 and line2   
line1 = np.array([3, -16, 7])
line2 = np.array([3, 8, -5])

#compute cross product for perpendicular
output1 = np.cross(line1, line2)
line3 = output1/np.linalg.norm(output1)

#point through which the line passes
point = np.array([1,2,-4])


#x1,y1,z1 are points on line1   
#x2,y2,z2 are points on line2 
#x3,y3,z3 are points on line3
x1 = []
y1 = []
z1 = []
x2 = []
y2 = []
z2 = []
x3 = []
y3 = []
z3 = []

#Compute points on 3 lines for plotting
for i in range(-10,20):
    
    x1 +=[line1[0]*i+8]
    y1 +=[line1[1]*i-19]
    z1 +=[line1[2]*i+10]
    x2 +=[line2[0]*i+15]
    y2 +=[line2[1]*i+29]
    z2 +=[line2[2]*i+5]
    x3 +=[line3[0]*i*10+1]
    y3 +=[line3[1]*i*10+2]
    z3 +=[line3[2]*i*10-4]
    
plot_lines(x1,y1,z1,'gray')
plot_lines(x2,y2,z2,'green')
plot_lines(x3,y3,z3,'red')
    
ax.scatter(point[0],point[1],point[2])

plt.show()