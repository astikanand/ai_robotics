import numpy as np
import cv2 as cv


def nothing(x):
    pass


# Create a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# Create different Trackbars
cv.createTrackbar('B:', 'image', 0, 255, nothing)
cv.createTrackbar('G:', 'image', 0, 255, nothing)
cv.createTrackbar('R:', 'image', 0, 255, nothing)

# Create a swith Trackbar
switch = "OFF/ON:"
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(cv.waitKey(1) != 27):
    cv.imshow('image', img)

    b = cv.getTrackbarPos('B:', 'image')
    g = cv.getTrackbarPos('G:', 'image')
    r = cv.getTrackbarPos('R:', 'image')

    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()
