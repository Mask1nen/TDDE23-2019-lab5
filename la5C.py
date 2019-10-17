    
from la5B import *

def test_pixel_constraint():

    testvalue = pixel_constraint(50,200,50,200,50,200)
    assert testvalue((100,100,100)) == 1
    assert testvalue((255,255,255)) == 0
    assert testvalue((0,0,0)) == 0

def test_generator_from_image():

    testvalue = ((0,0,0), (255,255,255), ())
    testgenerator1 = generator_from_image(testvalue)
    assert testgenerator1(0) == (0, 0, 0)
    assert testgenerator1(1) == (255,255,255)
    assert testgenerator1(2) == (())

def test_combine_images():
    
    constraint = pixel_constraint(50,200,50,200,50,200)
    testgenerator1 = generator_from_image(((0,0,0), (255,255,255), (100,100,100)))
    testgenerator2 = generator_from_image(((10,10,10), (245,245,245), (90,110,90)))

    assert combine_images((), constraint, testgenerator1, testgenerator2) == []

    assert combine_images(((50,50,50), (100,100,100)), \
    constraint ,testgenerator1, testgenerator2) == [(0,0,0), (245,245,245)]

    assert combine_images(((50,50,50), (100,100,100)), \
    gradient_condition,testgenerator1, testgenerator2) == [(1.9607843137254901, 1.9607843137254901, 1.9607843137254901), (251.07843137254906, 251.07843137254906, 251.07843137254906)]

def exception_pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    '''Defines a function that checks if the given pixel values is 
        in range of pixel_constraint values and returns 0 or 1.'''

    def compare(pixel):
        if not isinstance(pixel, tuple):
            raise TypeError("You have not input a tuple")
        elif len(pixel) != 3:
            raise ValueError("The tuple is not a pixel")

        for i in range(3):
            if isinstance(pixel[i], int):
                if not pixel[i] >= 0 and pixel[i] <= 255:
                    raise ValueError("The tuple does not have the correct values")
            else:
                raise TypeError("The tuple does not contain pixel values")

        (h,s,v) = pixel
        if h > hlow and h < hhigh and \
            s > slow and s < shigh and \
            v > vlow and v < vhigh:
            return 1
        else:
            return 0
    return compare


#5B2
def exception_generator_from_image(image_list):
    '''Defines a function that returns a tuple consisting of the color 
    values of a pixel in a specific index in a list of pixels.'''

    def pix_color(pixel):
        try:
            return image_list[pixel]
        except IndexError:
            raise IndexError("Index in image_list is out of range")
    return pix_color

#5B3 and #5B4
def exception_combine_images(bgr_list, condition, generator1, generator2):
    '''the function takes a mask, a condition, and two image
    generators then combines those two images depending on the condition
    and the mask and returns a list of the combined images'''
    
    result = []
    for i in range(len(bgr_list)):

        try:
            test1 = generator1(i)
        except:
            raise Exception("generator1 is out of index")

        try: 
            test2 = generator2(i)
        except:
            raise Exception("generator2 is out of index")

        try:
            test3 = condition(bgr_list[i])
        except:
            raise Exception("Something went wrong with condition")
        
        if condition(bgr_list[i]) == 1:
            result.append(generator2(i))

        elif condition(bgr_list[i]) == 0:
            result.append(generator1(i))

        else:     
            pixel1 = multiply_tuple(generator2(i),condition(bgr_list[i]))
            pixel2 = multiply_tuple(generator1(i),(1-condition(bgr_list[i])))

            result.append(add_tuples(pixel1,pixel2))
    return result

def exception_gradient_condition(seq):
    '''the function which when given a tuple consisting of color 
    values of a pixel on a gradient, returns a decimal value.'''

    value = seq[0] / 255
    return value 

def exception_tests():

    test1 = exception_generator_from_image([(0,0,0), (0,0,1)])
    test2 = exception_pixel_constraint(50,100,50,100,50,100)
    
    try:
        test1(2)
    except IndexError:
        print("IndexError")

    try:
        test1(0)
    except:
        print("Någon gick fel med rätt funktion!")

    try:
        test2("a")
    except TypeError:
        print("TypeError")

    try:
        test2((1,1))
    except ValueError:
        print("ValueError")

    try:
        test2((256,-1,256))
    except ValueError:
        print("ValueError")

    try:    
        test2((100,100,100))
    except:
        print("Något gick fel med rätt funktion!")