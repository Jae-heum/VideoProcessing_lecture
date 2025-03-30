"""
# 예제6 : 히스토그램 평홯화
# 예제에 필요한 사진이 제공되지 않아 임의로 강의자료 캠쳐하여 사용하였습니다.
"""


import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('mistryroad.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 명암 영상으로 변환하고 출력
plt.imshow(gray, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

h = cv.calcHist([gray], [0], None, [256], [0, 256])  # 히스토그램을 구해 출력
plt.plot(h, color='r', linewidth=1)
plt.show()

equal = cv.equalizeHist(gray)  # 히스토그램을 평활화하고 출력
plt.imshow(equal, cmap='gray')
plt.xticks([]), plt.yticks([])
plt.show()

h = cv.calcHist([equal], [0], None, [256], [0, 256])  # 히스토그램을 구해 출력
plt.plot(h, color='r', linewidth=1)
plt.show()



