import numpy as np
import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 6, (0, 0, 255), -1)
        points.append((x, y))
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255, 255, 0), 5)
            points.clear()
    cv2.imshow("image", img)


img = np.zeros([512, 512, 3], np.uint8)
cv2.imshow("image", img)
points = []
cv2.setMouseCallback('image', click_event)
while(cv2.waitKey(0) != 27):
    pass

cv2.destroyAllWindows()
