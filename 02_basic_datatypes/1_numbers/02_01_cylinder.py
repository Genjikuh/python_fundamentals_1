'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
from math import pi
radious = 3.14
height = 5
cylinder_area = 2 * pi * radious * (height + radious)
print(cylinder_area)
cylinder_volume = pi * radious**2 * height
print(cylinder_volume)