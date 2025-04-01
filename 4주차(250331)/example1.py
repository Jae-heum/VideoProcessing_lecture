"""
# 예제1 : 에지 검출
"""


import cv2 as cv


img = cv.imread('data/soccer.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

grad_x = cv.Sobel(gray, cv.CV_32F, 1, 0, ksize=3)
grad_y = cv.Sobel(gray, cv.CV_32F, 0, 1, ksize=3)

sobel_x = cv.convertScaleAbs(grad_x)
sobel_y = cv.convertScaleAbs(grad_y)

edge_strength = cv.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv.imshow('Original', img)
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Edge Strength', edge_strength)

cv.waitKey(0)
cv.destroyAllWindows()

