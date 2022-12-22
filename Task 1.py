#1 Python program which accepts the radius of a circle from the user and computes area

from math import pi
r = float(input('Input the radius of the circle:'))
print('The area of the circle with radius',r,'is:',pi*r**2)

#2 Python program to accept a filename from the user and print the extension of that

filename = input('Input the Filename:')
f = filename.split(".")
print ('The extension of the file is:', f[-1])
