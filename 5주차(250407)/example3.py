"""
# 예제3 : FLANN을 이용한 특징점 매칭
"""

import cv2 as cv
import numpy as np
import time

img1 = cv.imread('data/mot_color70.jpg')[190:350, 440:560] # 버스를 크롭하여 모델 영상으로 사용
gray1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
img2 = cv.imread('data/mot_color83.jpg') ## 장면 영상
gray2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

sift = cv.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray1, None)
kp2, des2 = sift.detectAndCompute(gray2, None)
print("특징점 개수 : ", len(kp1), len(kp2))


start = time.time()
flann_matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_FLANNBASED)
knn_match = flann_matcher.knnMatch(des1, des2, 2)

T = 0.7
good_match = []
for nearest1, nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance) < T:
        good_match.append(nearest1)
print("FLANN 매칭 시간 : ", time.time() - start)


img_match = np.empty((max(img1.shape[0], img2.shape[0]), img1.shape[1] + img2.shape[1], 3), dtype=np.uint8)
cv.drawMatches(img1, kp1, img2, kp2, good_match, img_match, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imshow('Good Matches', img_match)

k = cv.waitKey()
cv.destroyAllWindows()



