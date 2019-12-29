import cv2


def click_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_COMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        strXY = "(" + str(x) + ", " + str(y) + ")"
        cv2.putText(img, strXY, (x, y), font, 0.6, (255, 0, 0))
    elif event == cv2.EVENT_RBUTTONDOWN:
        blue = img(y, x, 0)
        green = img(y, x, 1)
        red = img(y, x, 2)
        strBGR = "(" + str(blue) + ", " + str(green) + ", " + str(red) + ")"
        cv2.putText(img, strBGR, (x, y), font, 0.6, (255, 255, 0))

    cv2.imshow("image", img)


img = cv2.imread("images/lena.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback('image', click_event)
while(cv2.waitKey(0) != 27):
    pass

cv2.destroyAllWindows()
