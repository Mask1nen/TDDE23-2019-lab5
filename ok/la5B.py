import cv2
from cvlib import *
import random
from la5A import *

#5B1
def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    '''Defines a function that checks if the given pixel values is 
        in range of pixel_constraint values and returns 0 or 1.'''

    def compare(pixel):
        
        (h,s,v) = pixel
        if h > hlow and h < hhigh and \
                s > slow and s < shigh and \
                v > vlow and v < vhigh:
            return 1
        else:
            return 0
    return compare

#5B2
def generator_from_image(image_list):
    '''Defines a function that returns a tuple consisting of the color 
    values of a pixel in a specific index in a list of pixels.'''

    def pix_color(pixel):

        return image_list[pixel]
    return pix_color

#5B3 and #5B4
def combine_images(bgr_list, condition, generator1, generator2):
    '''the function takes a mask, a condition, and two image
    generators then combines those two images depending on the condition
    and the mask and returns a list of the combined images'''
    
    result = []
    for i in range(len(bgr_list)):
        
        if condition(bgr_list[i]) == 1:
            result.append(generator2(i))

        elif condition(bgr_list[i]) == 0:
            result.append(generator1(i))

        else:     
            pixel1 = multiply_tuple(generator2(i),condition(bgr_list[i]))
            pixel2 = multiply_tuple(generator1(i),(1-condition(bgr_list[i])))

            result.append(add_tuples(pixel1,pixel2))
    return result

def gradient_condition(seq):
    '''the function which when given a tuple consisting of color 
    values of a pixel on a gradient, returns a decimal value.'''

    value = seq[0] / 255
    return value 

'''#5B3
# Läs in en bild
plane_img = cv2.imread("plane.jpg")

# Skapa ett filter som identifierar himlen
skypixels = pixel_constraint(100, 150, 50, 200, 100, 255)

# Omvandla originalbilden till en lista med HSV-färger
plane_list = cvimg_to_list(cv2.cvtColor(plane_img, cv2.COLOR_BGR2HSV))
plane_img_list = cvimg_to_list(plane_img)

# Skapa en generator som gör en stjärnhimmel
def star_generator(index):
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)

# Skapa en generator för den inlästa bilden
plane_generator = generator_from_image(plane_img_list)

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
result = combine_images(plane_list, skypixels, plane_generator, star_generator)

# Omvandla resultatet till en riktig bild och visa upp den
new_img = rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)
''''''
#5B4
image1 = cv2.imread("plane.jpg")
image1_list = cvimg_to_list(image1)
image_generator1 = generator_from_image(image1_list)

image2 = cv2.imread("flowers.jpg")
image2_list = cvimg_to_list(image2)
image_generator2 = generator_from_image(image2_list)

mask_image= cv2.imread("gradient.jpg")
mask_list = cvimg_to_list(mask_image)

result = combine_images(mask_list,gradient_condition,image_generator1,\
image_generator2)

new_img = rgblist_to_cvimg(result, image1.shape[0], image1.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)'''
