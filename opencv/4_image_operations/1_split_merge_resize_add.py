import cv2


img = cv2.imread("images/messi5.jpg")
print("Image Shape: {}".format(img.shape))  # returns tuple of no. of rows, columns, channels
print("Image Size: {}".format(img.size))  # returns total no. of pixels
print("Image DataType: {}".format(img.dtype))  # returns image data Type

# Split and merge the image
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

img2 = cv2.imread("images/opencv-logo.png")

# Resize the image for adding
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst_image = cv2.add(img, img2)
dst_image = cv2.addWeighted(img, 0.9, img2, 0.1, 0)
cv2.imshow("image", dst_image)

while(cv2.waitKey(0) != 27):
    pass

cv2.destroyAllWindows()
