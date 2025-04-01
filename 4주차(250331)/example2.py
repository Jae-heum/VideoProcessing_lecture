"""
# 예제2 : 캐니 에지
"""

import cv2 as cv

img=cv.imread('data/soccer.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# Canny 엣지 검출
canny1 = cv.Canny(gray, 50, 150) # T_low = 50, T_high = 150으로 설정
canny2 = cv.Canny(gray, 100, 200) # T_low = 100, T_high = 200으로 설정

cv.imshow('Original', img)
cv.imshow('Canny 1', canny1)
cv.imshow('Canny 2', canny2)

cv.waitKey(0)
cv.destroyAllWindows()




