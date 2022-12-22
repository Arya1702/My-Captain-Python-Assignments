#1
from math import pi
r = float(input('Input the radius of the circle:'))
print('The area of the circle with radius',r,'is:',pi*r**2)

#2
filename = input('Input the Filename:')
f = filename.split(".")
print ('The extension of the file is:', f[-1])