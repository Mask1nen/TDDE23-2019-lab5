import cv2
import numpy
import math
from cvlib import *

#Uppgift 5A1
def cvimg_to_list(img):
    '''the function converts the opencv datastructure to a regular 
    python list consisting of tuples'''

    tuplelist = []
    for i in range(len(img)):
        for r in range(len(img[0])):
            tuplelist.append((img[i][r][0], img[i][r][1], img[i][r][2]))
    return tuplelist

#5A2
def unsharp_mask(n):
    '''creates a 2d list consiting of the gausik blur that can be used 
    on images to make the image sharper'''

    nvalues = []
    value = n-1
    pos_value = value // 2 
    neg_value = -(value // 2 )

    nvalues = [[blur(column-pos_value,row+neg_value) for row in 
    range(n)] for column in range(n)]
    
    return nvalues           

def blur(x, y):
    '''creates a gausisk blur with the given math formula and special 
    case if x and y is 0'''

    if x == 0 and y == 0:
        return 1.5
    a1 = 2*math.pi*(4.5**2)
    a2 = math.e**-(((x**2)+(y**2))/(2*(4.5**2)))
    G = (-1/a1)*a2
    return G


