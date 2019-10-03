import cv2
import numpy
import math
"""övning 501"""
def imageturngrey():
    filename = "image.jpg"

    # Läser in bilden i gråskala till ett bildobjekt
    image = cv2.imread(filename, 0)

    # Visa bildobjektet
    cv2.imshow('Flowers turned grey', image)

    # Spara bildobjektet
    cv2.imwrite('grey_flowers.jpg', image)

    # Vänta på tangent
    cv2.waitKey(0)

    # Stäng ner alla OpenCV-fönster
    cv2.destroyAllWindows()
#Övning 501
def blue():
    
    src = cv2.imread('image.jpg', cv2.IMREAD_UNCHANGED)
    print(src)
    # assign blue channel to zeros
    src[:,:,0] = numpy.zeros([src.shape[0], src.shape[1]])
    print(src)
    #save image
    cv2.imwrite('image2.jpg',src) 
    cv2.imshow('image2.jpg', src)
    cv2.waitKey(0)

#Uppgift 5A1
def cvimg_to_list(img):
    tuplelist = []
    for i in range(len(img)):
        for r in range(len(img[0])):
            tuplelist.append((img[i][r][0], img[i][r][1], img[i][r][2]))
    return tuplelist

#5A2
def unsharp_mask(n):
    nvalues = []
    if n == 1:
        nvalues.append(0)
    elif 
    value=n-1


def blur(x, y):
    a1 = 2*math.pi*(4.5**2)
    a2 = math.e**-(((x**2)+(y**2))/(2*(4.5**2)))
    G = (-1/a1)*a2
    return G

