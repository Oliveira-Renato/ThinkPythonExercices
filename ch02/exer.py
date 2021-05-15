# 1 - The volume of a sphere with radius r is 4/3 πr**3. What is the volume of a sphere with radius 5?
#V = 4.pi.r**3/3
import math

radius = 5

#usando a formula para calcular o volume
volume_sphere = 4 * math.pi * (math.pow(radius,3))/3

print('The volume is {:.2f}.'.format(volume_sphere))

