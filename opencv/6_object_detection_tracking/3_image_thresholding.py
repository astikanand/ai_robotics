# import numpy as np
import cv2 as cv

img = cv.imread("images/gradient.png")


cv.imshow("image", img)

while(cv.waitKey(0) != 27):
    pass
cv.destroyAllWindows()
