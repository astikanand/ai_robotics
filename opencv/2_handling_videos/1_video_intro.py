import cv2

video_capturer = cv2.VideoCapture(0)
# List of available codes - http://www.fourcc.org/codecs.php
# Define the codec and create VideoWriter object
fourcc_codec = cv2.VideoWriter_fourcc(*'XVID')
frame_per_second = 20.0
capture_size = (int(video_capturer.get(3)), int(video_capturer.get(4)))
video_writer = cv2.VideoWriter("videos/output.avi", fourcc_codec, frame_per_second, capture_size)

while video_capturer.isOpened():
    ret, frame = video_capturer.read()
    frame = cv2.flip(frame, 1)  # Lateral inversion of the video frame

    if ret:
        print("Width of Video Frame:\n{}".format(video_capturer.get(cv2.CAP_PROP_FRAME_WIDTH)))
        print("Height of Video Frame:\n{}".format(video_capturer.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        # Write this frame into a file : out is an instance of video writer
        video_writer.write(frame)

        gray_scaled_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("videocam", gray_scaled_video)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

video_capturer.release()
video_writer.release()
cv2.destroyAllWindows()
