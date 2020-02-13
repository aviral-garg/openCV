import cv2

img = cv2.imread("opencv-logo.png")             # img handler
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)     # window handler
cv2.imshow("Image", img)                        # load
cv2.waitKey(0)                                  # wait for user input
cv2.imwrite("output.jpg", img)                  # save to new file
