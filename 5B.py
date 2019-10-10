import cv2
from cvlib import *

#5B1
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    '''defines a function that returns compare as a function'''

    def compare(pixel):
        '''defines a function that checks if the given pixel is in range of pixel_constraint values'''

        (h,s,v) = pixel
        if h > hlow and h < hhigh and \
                s > slow and s < shigh and \
                v > vlow and v < vhigh:
            return 1
        else:
            return 0
    return compare

#från labb 5A för 5B1
def cvimg_to_list(img):
    '''the function converts the opencv datastructure to a regular python list consisting of tuples'''

    tuplelist = []
    for i in range(len(img)):
        for r in range(len(img[0])):
            tuplelist.append((img[i][r][0], img[i][r][1], img[i][r][2]))
    return tuplelist

#5B2
def generator_from_image(image_list):
    '''defines a function that returns pix_color as a function'''

    def pix_color(pixel):
        '''the function returns the pixel of a specific index in a list of pixels'''

        return image_list[pixel]
    return pix_color

#5B3
# Importera nödvändiga bibliotek, inklusive lösningar från förra omgången
'''
import cv2
import random

def combine_images(hsv_list, condition, generator1, generator2): '''
#    '''gives each pixel a value depending on if it's in range of the pixel constraints and then converts them into thier respective BGR values'''
'''
    image_list = list(map(condition,hsv_list))
    for i in range(len(image_list)):
        if image_list[i] == 1:
            image_list[i] = generator1()
        elif image_list[i] == 0:
            image_list[i] = generator2(i)
    return image_list

# Läs in en bild
plane_img = cv2.imread("plane.jpg")

# Skapa ett filter som identifierar himlen
condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
hsv_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)

# Skapa en generator som gör en stjärnhimmel
def generator1():
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

# Skapa en generator för den inlästa bilden
generator2 = generator_from_image(plane_img_list)

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
result = combine_images(hsv_list, condition, generator1, generator2)

# Omvandla resultatet till en riktig bild och visa upp den
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)
'''

#5B4

def combine_images(mask, mask_function, image_generator1, image_generator2):
    
    result = []
    for i in range(len(image1_list)):
        
        if gradiant_condition(mask(i)) == 1:
            result.append(image_generator2(i))

        elif gradiant_condition(mask(i)) == 0:
            result.append(image_generator1(i))

        else:     
            pixel1 = multiply_tuple(image_generator2(i),gradiant_condition(mask(i)))
            pixel2 = multiply_tuple(image_generator1(i),(1-gradiant_condition(mask(i))))

            result.append(add_tuples(pixel1,pixel2))
    return result

def gradiant_condition(seq):
    value = seq[0] / 255
    return value 

image1 = cv2.imread("plane.jpg")
image1_list = cvimg_to_list(image1)
image_generator1 = generator_from_image(image1_list)

image2 = cv2.imread("flowers.jpg")
image2_list = cvimg_to_list(image2)
image_generator2 = generator_from_image(image2_list)

mask_image= cv2.imread("gradient.jpg")
mask_list = cvimg_to_list(mask_image)
mask = generator_from_image(mask_list)

result = combine_images(mask,gradiant_condition,image_generator1,image_generator2)

new_img = rgblist_to_cvimg(result, image1.shape[0], image2.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)