

"""
# 강 의 : 영상처리 실제
# 날 짜 : 2025년 3월 17일 수업
# 학 번 : 2022154002
# 성 명 : 이재흠
"""


# ##### Example 1 (이미지 읽고 표시하기) p.31 #####
# import cv2 as cv
# import sys
#
# img = cv.imread('soccer.jpg')
#
# if img is None:
#     sys.exit("파일을 찾을 수 없습니다.")
#
# cv.imshow('Image Display', img)
#
# cv.waitKey(0)
# cv.destroyAllWindows()




# ##### Example 2 (이미지 변환하기) p.34 #####
# import cv2 as cv
# import sys
#
# img = cv.imread('soccer.jpg')
#
# if img is None:
#     sys.exit("파일을 찾을 수 없습니다.")
#
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# gray_small = cv.resize(gray, dsize=(0, 0), fx=0.5, fy=0.5)
#
# cv.imshow("Color Image", img)
# cv.imshow("Gray Image", gray)
# cv.imshow("Gray Image small", gray_small)
#
# cv.waitKey(0)
# cv.destroyAllWindows()




# ##### Example 3 (웹캠 활용하기 - 웹 캠에서 비디오 읽기) p.36 #####
# import cv2 as cv
# import sys
#
# cap = cv.VideoCapture(0, cv.CAP_DSHOW)
#
# if not cap.isOpened():
#     sys.exit("카메라를 연결 실패")
#
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         sys.exit("프레임 획득에 실패하여 루프를 나갑니다.")
#         break
#
#     cv.imshow("Video display", frame)
#
#     key = cv.waitKey(1)
#     if key == ord('q'):
#         break
#
# cap.release()
# cv.destroyAllWindows()




# ##### Example 4 (웹캠 활용하기 - 비디오에서 영상 수집하기) p.37 #####
# import cv2 as cv
# import numpy as np
# import sys
#
# cap = cv.VideoCapture(0, cv.CAP_DSHOW)
#
# if not cap.isOpened():
#     sys.exit("카메라를 연결 실패")
#
# frames=[]
# while True:
#     ret, frame = cap.read()
#
#     if not ret:
#         print("프레임 획득에 실패하여 루프를 나갑니다.")
#         break
#
#     cv.imshow("Video display", frame)
#
#     key = cv.waitKey(1)
#     if key == ord('c'):
#         frames.append(frame)
#     elif key == ord('q'):
#         break
#
# cap.release()
# cv.destroyAllWindows()
#
# if len(frames) > 0:
#     imgs = frames[0]
#     for i in range(1, min(3, len(frames))):
#         imgs = np.hstack((imgs, frames[i]))
#
#     cv.imshow("collected images", imgs)
#
#     cv.waitKey(0)
#     cv.destroyAllWindows()





# ##### Example 5 (영상에 도형을 그리고 글씨 쓰기) p.42 #####
# import cv2 as cv
# import sys
# img= cv.imread('girl_laughing.jpg')
#
# if img is None:
#     sys.exit("파일을 찾을 수 없습니다.")
#
# cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)
# cv.putText(img, 'laugh', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#
# cv.imshow("Draw", img)
#
# cv.waitKey()
# cv.destroyAllWindows()





# ##### Example 6 (마우스를 통한 상호작용) p.45 #####
# import cv2 as cv
# import sys
#
# img= cv.imread('girl_laughing.jpg')
#
# if img is None:
#     sys.exit("파일을 찾을 수 없습니다.")
#
#
# def draw(event, x, y, flags, param):
#     if event == cv.EVENT_LBUTTONDOWN:
#         cv.rectangle(img, (x, y), (x+200, y+200), (0, 0, 255), 2)
#     elif event == cv.EVENT_RBUTTONDOWN:
#         cv.rectangle(img, (x, y), (x+100, y+100), (255, 0, 0), 2)
#
#     cv.imshow("Drawing", img)
#
# cv.namedWindow("Drawing")
# cv.imshow("Drawing", img)
#
#
# cv.setMouseCallback("Drawing", draw)
#
# while(True):
#     if cv.waitKey(1)== ord('q'):
#         cv.destroyAllWindows()
#         break






# #### Example 7 (마우스 드래그로 도형 크기 조절하기) p.47 #####
# import cv2 as cv
# import sys
#
# img= cv.imread('girl_laughing.jpg')
#
# if img is None:
#     sys.exit("파일을 찾을 수 없습니다.")
#
#
# def draw(event, x, y, flags, param):
#     global ix, iy
#
#     if event == cv.EVENT_LBUTTONDOWN:
#         ix, iy = x, y
#     elif event == cv.EVENT_LBUTTONUP:
#         cv.rectangle(img, (ix, iy), (x, y), (255, 0, 0), 2)
#
#     cv.imshow("Drawing", img)
#
# cv.namedWindow("Drawing")
# cv.imshow("Drawing", img)
#
# cv.setMouseCallback("Drawing", draw)
#
# while(True):
#     if cv.waitKey(1)== ord('q'):
#         cv.destroyAllWindows()
#         break





#### Example 8 (페인팅 기능 사용하기) p.49 #####
import cv2 as cv
import sys
img = cv.imread("soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

BrushSize = 5
LColor, RColor = (255, 0, 0), (0, 0, 255)

def painting(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), BrushSize, LColor, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        cv.circle(img, (x, y), BrushSize, RColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_LBUTTON:
        cv.circle(img, (x, y), BrushSize, LColor, -1)
    elif event == cv.EVENT_MOUSEMOVE and flags == cv.EVENT_FLAG_RBUTTON:
        cv.circle(img, (x, y), BrushSize, RColor, -1)

    cv.imshow("Painting", img)

cv.namedWindow("Painting")
cv.imshow("Painting", img)

cv.setMouseCallback("Painting", painting)

while True:
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break















