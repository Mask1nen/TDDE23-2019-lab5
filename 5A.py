import cv2
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
