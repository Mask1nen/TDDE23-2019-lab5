    
from la5B import *

def test_pixel_constraint():
    #test_cases = ((0,0,0,0,0,0), (0)),(())

    '''gör om test_cases till condition, pixel och expected outcome'''
    test_cases = ((50, 200, 50, 200, 50, 200),(100,100,100), 1,(50, 200, 50, 200, 50, 200),(255,255,255),0)



    
    for i in range(len(test_cases),3):
        h = pixel_constraint(test_cases[i][i],test_cases[0][1],test_cases[0][2],test_cases[0][3],test_cases[0][4],test_cases[0][5])
        assert h(test_cases[i+1]) == test_cases[i+2]
    
