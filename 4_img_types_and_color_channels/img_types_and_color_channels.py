import cv2
import numpy as np

color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)
print(color.shape)
height, width, channels = color.shape

b, g, r = cv2.split(color)
rgb_split = np.empty([height, width * 3, 3], 'uint8')

rgb_split[:, 0:width] = cv2.merge([b, b, b])
rgb_split[:, width:width * 2] = cv2.merge([g, g, g])
rgb_split[:, width * 2:width * 3] = cv2.merge([r, r, r])

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
hsv_split = np.concatenate((h, s, v), axis=1)   # same as rgb_split concat (but more efficient)
cv2.imshow("Split HSV", hsv_split)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit(0)
# Cheatsheet so far
#
# # ########## 3. Data Types and Color Channels ###########
# import cv2
# import numpy as np
#
# black = np.zeros([150, 200, 1], 'uint8')  # [h, w, ch] & type = 'uint8' i.e allowed values from 0 to 255
# cv2.imshow("Black", black)  # window name, variable passed
# print(f'first pixel (black)\n'
#       f'actual: {black[0, 0, :]}\n'
#       f'expected: [0]\n')
#
# ones = np.ones([150, 200, 3], 'uint8')
# cv2.imshow("Ones - Almost black", ones)
# print(f'first pixel (ones for B G R i.e. almost black)\n'
#       f'actual: {ones[0, 0, :]}\n'
#       f'expected: [1 1 1]\n')
#
# white = np.ones([150, 200, 3], 'uint16')
# white *= (2 ** 16 - 1)
# cv2.imshow("White", white)
# print(f'first pixel (white i.e. MAX_VALUES for B G R)\n'
#       f'actual: {white[0][0][:]}\n'
#       f'expected: [6553 65535 65535]\n')
#
# color = ones.copy()  # deep copy
# color[:, :] = (255, 0, 0)  # BGR format
# cv2.imshow("Blue", color)
# print(color[0, 0, :])
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit(0)

# # ########## 1. Pixel Data ###########
# img = cv2.imread("opencv-logo.png", 1)  # 1 = default; 0 = black and white
# img             # show each pixel value
# type(img)       # `<class 'numpy.ndarray'>`
# len(img)        # num. of rows `739`
# len(img[0])     # num. of vertical column `600`
# len(img[0][0])  # num. of channels; `3` (RGB); 4 = RGBA(/T) - alpha value/transparency
# img.shape       # show(rows cols channels) `(739, 600, 3)`
# img.dtype       # dtype(uint8: unsigned integer value 8) max(2**8 values in each pixel) `dtype('uint8')`
# img[10, 5]      # `array([255, 255, 255], dtype=uint8)`
# img[:, :, 0]    # only 1 channels values for all pixels (R or G or B or A)
#                   array([[255, 255, 255, ..., 255, 255, 255], ..., [255, 255, 255, ..., 255, 255, 255] ]
#                             , dtype=uint8)
# img.size        # # of pixels in the image `1330200`

# ########## 2. Load Save ###########
# img = cv2.imread("opencv-logo.png")             # img handler
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)     # window handler
# cv2.imshow("Image", img)                        # load
# cv2.waitKey(0)                                  # wait for user input
# cv2.imwrite("output.jpg", img)                  # save to new file
