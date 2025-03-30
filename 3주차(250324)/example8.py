"""
# 예제8 : 영상 보간
# 예제에 필요한 사진이 제공되지 않아 임의로 구글링하여 사용헀습니다. (crop 좌표도 조정)
"""

import cv2 as cv

img = cv.imread('data/rose.png')
patch = img[215:315, 465:565, :]

img = cv.rectangle(img, (465, 215), (565, 315), (255, 0, 0), 3)
patch1 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_NEAREST)
patch2 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_LINEAR)
patch3 = cv.resize(patch, dsize=(0, 0), fx=5, fy=5, interpolation=cv.INTER_CUBIC)

cv.imshow('Original', img)
cv.imshow('Resize nearest', patch1)
cv.imshow('Resize bilinear', patch2)
cv.imshow('Resize bicubic', patch3)

cv.waitKey()
cv.destroyAllWindows()



