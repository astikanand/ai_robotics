import numpy as np
import cv2 as cv


def nothing(x):
    pass


video_capturer = cv.VideoCapture(0)

# Create Trackbars for upper and lower value of HSV
cv.namedWindow("Tracking")
cv.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv.createTrackbar("US", "Tracking", 255, 255, nothing)
cv.createTrackbar("UV", "Tracking", 255, 255, nothing)


while(cv.waitKey(1) != 27):
    # Read every frame from video and convert it to HSV format
    _, frame = video_capturer.read()
    frame = cv.flip(frame, 1)  # Lateral inversion of the video frame
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

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

    # Create a mask frame using upper and lower value of color
    mask_frame = cv.inRange(hsv_frame, lower_blue, upper_blue)

    # Create the resulting frame using bitwise_and operator and mask
    result_frame = cv.bitwise_and(frame, frame, mask=mask_frame)

    cv.imshow("Resulting frame", result_frame)


video_capturer.release()
cv.destroyAllWindows()
