import cv2

# ########## Pixel Data ###########

img = cv2.imread("opencv-logo.png", 1)  # 1 = default; 0 = black and white
img             # show each pixel value
type(img)       # `<class 'numpy.ndarray'>`
len(img)        # num. of rows `739`
len(img[0])     # num. of vertical column `600`
len(img[0][0])  # num. of channels; `3` (RGB); 4 = RGBA(/T) - alpha/transparency
img.shape       # show(rows cols channels) `(739, 600, 3)`
img.dtype       # dtype(uint8: unsigned integer value 8) max(2**8 values in each pixel) `dtype('uint8')`
img[10, 5]      # `array([255, 255, 255], dtype=uint8)`
img[:, :, 0]    # only 1 channels values for all pixels (R or G or B or A)
#                   array([
#                             [255, 255, 255, ..., 255, 255, 255],
#                             [255, 255, 255, ..., 255, 255, 255],
#                             [255, 255, 255, ..., 255, 255, 255],
#                             ...,
#                             [255, 255, 255, ..., 255, 255, 255],
#                             [255, 255, 255, ..., 255, 255, 255],
#                             [255, 255, 255, ..., 255, 255, 255]
#                         ], dtype=uint8)
img.size        # # of pixels in the image `1330200`

# Cheatsheet so far

# ########## Load Save ###########
# import cv2
#
# img = cv2.imread("opencv-logo.png")             # img handler
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)     # window handler
# cv2.imshow("Image", img)                        # load
# cv2.waitKey(0)                                  # wait for user input
# cv2.imwrite("output.jpg", img)                  # save to new file
