"""
# 예제2 : 이진화
"""

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('soccer.jpg')
h = cv.calcHist([img], [2], None, [256], [0, 256]) # 2번 채널(R) 히스토그램 계산
plt.plot(h,color='r',linewidth=1)

## 출력 안되고 종료 되어서 추가함 #jh
plt.show()