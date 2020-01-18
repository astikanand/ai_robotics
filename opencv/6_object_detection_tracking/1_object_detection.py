import numpy as np
import cv2 as cv


def nothing(x):
    pass


# Create Trackbars for upper and lower value of HSV
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)


while(cv.waitKey(1) != 27):
    # Read an image and convert it to HSV format
    img = cv.imread("images/smarties.png")
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Get upper and lower range for color for objct detection
    # lower_blue = np.array([96, 116, 50])
    # upper_blue = np.array([130, 255, 255])
    l_h = cv.getTrackbarPos("LH", "Tracking")
    l_s = cv.getTrackbarPos("LS", "Tracking")
    l_v = cv.getTrackbarPos("LV", "Tracking")
    u_h = cv.getTrackbarPos("UH", "Tracking")
    u_s = cv.getTrackbarPos("US", "Tracking")
    u_v = cv.getTrackbarPos("UV", "Tracking")

    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue = np.array([u_h, u_s, u_v])

    # Create a mask image using upper and lower value of color
    mask_img = cv.inRange(hsv_img, lower_blue, upper_blue)

    # Create the resulting image using bitwise_and operator and mask
    result_img = cv.bitwise_and(img, img, mask=mask_img)

    cv.imshow("Initial Image", img)
    cv.imshow("Mask Image", mask_img)
    cv.imshow("Resulting Image", result_img)


cv.destroyAllWindows()
