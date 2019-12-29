import cv2


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        ball = img[280:340, 330:390]  # Copy the ball from here - ROI
        img[273:333, 100:160] = ball   # Paste it here
    cv2.imshow("image", img)


img = cv2.imread("images/messi5.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback('image', click_event)
while(cv2.waitKey(0) != 27):
    pass

cv2.destroyAllWindows()
