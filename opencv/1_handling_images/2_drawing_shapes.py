import numpy as np
import cv2


# img = cv2.imread("images/lena.jpg", 1)
img = np.zeros([512, 512, 3], np.uint8) # Black image of size 512*512

img = cv2.line(img, (0, 0), (280, 280), (255, 0, 0), 10, cv2.LINE_AA, 0)

img = cv2.arrowedLine(img, (0, 280), (280, 280), (0, 255, 0), 10, 4, 0, 0.1)

img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

img = cv2.circle(img, (447, 63), 63, (123, 50, 55), -1)

img = cv2.ellipse(img, (250, 50), (100, 80), 0, 0, 180, (155, 78, 105), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 255, 255), 2)

img = cv2.putText(img, 'OpenCV', (10, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("image window", img)
cv2.waitKey(5000)

cv2.imwrite("images/geometric_shapes_on_image.jpg", img)
cv2.destroyAllWindows()
