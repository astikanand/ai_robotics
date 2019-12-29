import cv2
from datetime import datetime, timedelta
from time import time

video_capturer = cv2.VideoCapture(0)
start_time = time()

fourcc_codec = cv2.VideoWriter_fourcc(*'XVID')
frame_per_second = 20.0
capture_size = (int(video_capturer.get(3)), int(video_capturer.get(4)))
video_writer = cv2.VideoWriter("videos/video_with_date_time.avi", fourcc_codec, frame_per_second, capture_size)

while video_capturer.isOpened():
    ret, frame = video_capturer.read()
    frame = cv2.flip(frame, 1)  # Lateral inversion of the video frame

    if ret:
        font = cv2.FONT_HERSHEY_COMPLEX
        recorded_time= "Rec: "+ str(timedelta(seconds=(time() - start_time)))
        cv2.putText(frame, recorded_time, (20, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)

        date_time = datetime.now().strftime("%d %b %Y %I:%M:%S %p")
        cv2.putText(frame, date_time, (920, 30), font, 0.8, (255, 0, 255), 2, cv2.LINE_AA)

        text = "Width: " + str(video_capturer.get(3)) + " Height: " + str(video_capturer.get(4))
        cv2.putText(frame, text, (980, 710), font, 0.6, (255, 255, 0), 1, cv2.LINE_AA)

        video_writer.write(frame)

        cv2.imshow("videocam", frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

video_capturer.release()
cv2.destroyAllWindows()
