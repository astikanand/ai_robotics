import cv2

img = cv2.imread("images/lena.jpg", 0)

print("Image in pixel matrix representation:\n{}".format(img))
cv2.imshow("image window", img)

key_pressed = cv2.waitKey(0)


if key_pressed == 27:  # ESC key
    cv2.destroyAllWindows()
elif key_pressed == ord('s'):
    cv2.imwrite("images/lena_copy.jpg", img)
    cv2.destroyAllWindows()
