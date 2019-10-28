    
from la5B import *

##### 5C1 ######
def test_pixel_constraint():
    '''Tests and compares the result given by pixel_constraint to the
    expected result with diffrent input data.'''

    testvalue = pixel_constraint(50,200,50,200,50,200)
    assert testvalue((100,100,100)) == 1
    assert testvalue((255,255,255)) == 0
    assert testvalue((0,0,0)) == 0

def test_generator_from_image():
    '''Tests and compares the result given by generator_from_image to 
    the expected result with diffrent input data.'''

    testvalue = ((0,0,0), (255,255,255), ())
    testgenerator = generator_from_image(testvalue)
    assert testgenerator(0) == (0, 0, 0)
    assert testgenerator(1) == (255,255,255)
    assert testgenerator(2) == (())

def test_combine_images():
    '''Tests and compares the result given by combine_images to the
    expected result with diffrent input data. '''

    constraint = pixel_constraint(50,200,50,200,50,200)
    testgenerator1 = generator_from_image(((0,0,0), (255,255,255), (100,100,100)))
    testgenerator2 = generator_from_image(((10,10,10), (245,245,245), (90,110,90)))
    test_bgr_list = ((50,50,50), (100,100,100))

    assert combine_images((), constraint, testgenerator1, testgenerator2) == []

    assert combine_images(test_bgr_list, constraint ,testgenerator1, \
    testgenerator2) == [(0,0,0), (245,245,245)]

    assert combine_images(test_bgr_list, gradient_condition, \
    testgenerator1, testgenerator2) == [(1.9607843137254901, 1.9607843137254901, \
    1.9607843137254901), (251.07843137254906, 251.07843137254906, 251.07843137254906)]

def run_5C1():
    '''A function that runs test_pixel_constraint, 
    test_generator_from_image and test_combine_images.'''

    test_pixel_constraint()
    test_generator_from_image()
    test_combine_images()
    print("It passed all the tests in 5C1!")

#### 5C2 ######

def exception_pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    '''Defines a function that checks if the given pixel values is 
        in range of pixel_constraint values and returns 0 or 1 along 
        with testcases where errors could occur.'''

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


def exception_generator_from_image(image_list):
    '''Defines a function that returns a tuple consisting of the color 
    values of a pixel in a specific index in a list of pixels along 
    with testcases where errors could occur.'''

    def pix_color(pixel):

        try:
            return image_list[pixel]
        except IndexError:
            raise IndexError("Index in image_list is out of range")
        
    return pix_color

def exception_combine_images(bgr_list, condition, generator1, generator2):
    '''The function takes a mask, a condition, and two image
    generators then combines those two images depending on the condition
    and the mask and returns a list of the combined images, along 
    with testcases where errors could occur.'''
    
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

def exception_tests():
    '''Some predetermined testcases where the testcases checks that 
    the code opperates as it should.'''

    test1 = exception_generator_from_image([(0,0,0), (0,0,1)])
    test2 = exception_pixel_constraint(50,100,50,100,50,100)
    generator1 = exception_generator_from_image([(0,0,0), (0,0,1)])
    generator2 = exception_generator_from_image([(2,2,2), (1,1,1)])
    
    try:
        test1(2)
    except IndexError:
        print("IndexError from generator_from_image.")

    try:
        test1(0)
    except:
        print("Something went wrong with generator_from_image!")

    try:
        test2("a")
    except TypeError:
        print("TypeError in pixel_constraint.")

    try:
        test2((1,1))
    except ValueError:
        print("ValueError in pixel_constraint.")

    try:
        test2((256,-1,256))
    except ValueError:
        print("ValueError in pixel_constraint.")

    try:    
        test2((100,100,100))
    except:
        print("Something went wrong with pixel_constraint!")

    try:
        exception_combine_images(((0,0,0)), test2, generator1, generator2)
    except:
        print("IndexError in combine_images.")
    
    try:
        exception_combine_images(((0,0,0), (1,1,1)), test2, generator1, generator2)
    except:
        print("Something went wrong with combine_images!")

def run_5C2():
    '''A function that runs exception_pixel_constraint, 
    exception_generator_from_image, exception_combine_images, and
    exception_tests.'''

    variable1 = exception_pixel_constraint(50,200,50,200,50,200)
    variable1((50,50,50))

    variable2 = exception_generator_from_image(((10,10,10), (245,245,245), (90,110,90)))
    variable2(1)

    test_bgr_list = ((50,50,50), (100,100,100))
    constraint = pixel_constraint(50,200,50,200,50,200)
    generator1 = generator_from_image(((100,100,100),(200,200,200)))
    generator2 = generator_from_image(((50,50,50),(150,150,150)))
    
    exception_combine_images(test_bgr_list,constraint,generator1,generator2)

    exception_tests()  #should give errors
    
    print("It passed all the tests in 5C2!")