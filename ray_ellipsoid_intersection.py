# ray_ellipsoid_intersection.py

# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Determines if there is an intersection point between the ray and the Earth reference ellipsoid and calculates it if it is valid.


# Parameters: 
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin

# Output:
# l_d[0] # x-component of intersection 
# l_d[1] # y-component of intersection 
# l_d[2] # z-component of intersection 


# Written by Vineet Keshavamurthy

# import math and sys modules
import math 
import sys

# constants
Earth_Radius = 6378.137 
eccentricity_const = 0.081819221456
# initialize input variables
d_l_x = float('nan') 
d_l_y = float('nan') 
d_l_z = float('nan') 
c_l_x = float('nan') 
c_l_y = float('nan') 
c_l_z = float('nan')  
# check for correct number of argument passed
if len(sys.argv) == 7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
   'Usage: '\
   'Incorrect number of input arguments passed. Recheck the command line passed.'\
    )
    exit()

#Define each vector for the final output
#l_d vector 
l_d = [float('nan'), float('nan'), float('nan')]
#d_l vector
d_l = [d_l_x, d_l_y, d_l_z] #d_l vector has the three x,y,and z components
#c_l vector
c_l = [c_l_x, c_l_y, c_l_z] #c_l vector has the three x,y, and z components

#calculation of intermediate vector term 1
x_term1 = d_l_x**2
y_term1 = d_l_y**2
z_term1 = d_l_z**2
term1 = z_term1/(-eccentricity_const**2+1)+y_term1+x_term1
#calculation of intermediate vector term 2
x_term2 = c_l_x*d_l_x
y_term2 = d_l_y*c_l_y
z_term2 = c_l_z*d_l_z
term2 = (x_term2 + y_term2 + (z_term2)/(1 - eccentricity_const**2))*2
#calculation of intermediate vector term 3
x_term3 = c_l_x**2
y_term3 = c_l_y**2
z_term3 = c_l_z**2
term3 = x_term3 + y_term3 + z_term3/(1 - eccentricity_const**2) - Earth_Radius**2

vect_dis =  - term3*term1*4.0 + term2*term2

# check for if the intersection point exists
if vect_dis >= 0.0:
    discriminant = (-term2 - math.sqrt(vect_dis))/(2*term1)
    if discriminant < 0.0:
        discriminant = (-term2 + math.sqrt(vect_dis))/(2*term1)
    if discriminant >= 0.0:
        l_d = [c_l_x + discriminant*d_l_x, c_l_y+discriminant*d_l_y, c_l_z+discriminant*d_l_z]
        # print final values
        #x-component
        print(l_d[0]) 
        #y-component
        print(l_d[1]) 
        #z-component
        print(l_d[2]) 