import cv2

video_capturer = cv2.VideoCapture(0)

# Getting height and Width of Camera using Name
print(video_capturer.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video_capturer.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Setting Height and Width of Camera using Numerical Value
video_capturer.set(3, 600)
video_capturer.set(4, 600)

print(video_capturer.get(3))
print(video_capturer.get(4))

while video_capturer.isOpened():
    ret, frame = video_capturer.read()
    frame = cv2.flip(frame, 1)  # Lateral inversion of the video frame

    if ret:
        gray_scaled_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("videocam", gray_scaled_video)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

video_capturer.release()
cv2.destroyAllWindows()
