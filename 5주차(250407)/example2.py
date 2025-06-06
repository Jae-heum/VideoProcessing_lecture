"""
# 예제2 : SIFT 기술자
"""

import cv2 as cv

img = cv.imread('data/mot_color70.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray, None)

gray = cv.drawKeypoints(gray, kp, None, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('SIFT', gray)

k = cv.waitKey()
cv.destroyAllWindows()

