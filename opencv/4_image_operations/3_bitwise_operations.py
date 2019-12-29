import numpy as np
import cv2

# img1: Make an image with left half black and right half white
img = np.zeros((200, 500, 3), np.uint8)
img1 = cv2.rectangle(img, (250, 0), (500, 200), (255, 255, 255), -1)

# img2: Draw a white rectangle on the balck image
img = np.zeros((200, 500, 3), np.uint8)
img2 = cv2.rectangle(img, (200, 0), (300, 100), (255, 255, 255), -1)

bitAndImg = cv2.bitwise_and(img1, img2)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAndImg", bitAndImg)

while(cv2.waitKey(0) != 27):
    pass
cv2.destroyAllWindows()
