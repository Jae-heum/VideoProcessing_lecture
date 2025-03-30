"""
# 예제4 : 모폴로지
"""


import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('data/JohnHancocksSignature.png', cv.IMREAD_UNCHANGED)

# t, bin_img = cv.threshold(img[:, :, 3], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# 위 코드는 4채널 이미지만 사용할 수 있는 이미지어서 아래 코드로 수정함 ## jh

# 이미지에 알파 채널이 있는지 확인
if img.shape[2] == 4:
    print('알파 채널이 있습니다.')
    t, bin_img = cv.threshold(img[:, :, 3], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
else:
    print('알파 채널이 없습니다.')
    # 알파 채널이 없으면 이미지를 그레이스케일로 변환 후 임계값 적용
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    t, bin_img = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)



plt.imshow(bin_img, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b = bin_img[bin_img.shape[0]//2:bin_img.shape[0], 0:bin_img.shape[0]//2 + 1]
plt.imshow(b, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

se = np.uint8([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0]
])  # 구조 요소

b_dilation = cv.dilate(b, se, iterations=1) # 팽창
plt.imshow(b_dilation, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_erosion = cv.erode(b, se, iterations=1) # 침식
plt.imshow(b_erosion, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

b_closing = cv.erode(cv.dilate(b, se, iterations=1), se, iterations=1) # 닫기
plt.imshow(b_closing, cmap='gray'), plt.xticks([]), plt.yticks([])
plt.show()

