# inRange함수를 잘 설정하려면 trackBar기능이 필요하다.
import sys
import numpy as np
import cv2

# 트랙바 콜백 함수 생성
def on_trackbar(pos):
    hmin = cv2.getTrackbarPos('H_min', 'Trackbar')
    hmax = cv2.getTrackbarPos('H_max', 'Trackbar')
    
    # inRange함수에 적용
    dst = cv2.inRange(src_hsv, (hmin,150,0), (hmax,255,255))
    cv2.imshow('Trackbar', dst) # 트랙바 지정 된 값을 이미지에 적용

# 트랙바를 적용 할 이미지 지정하기
fileName = 'data2/red.jpg'
# fileName = 'data2/green.jpg'
# fileName = 'data2/yellow.jpg'

src = cv2.imread(fileName)

# 각 색에 마스크 입히기
mask = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)


if src is None: # 이미지 경로가 틀렸을 때
    sys.exit("Image Load failed!")
    
# 색상의 범위를 잘 지정하려면 bgr->hsv
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

# 창에 트랙바를 넣기 위해서는 창을 먼저 생성
cv2.namedWindow('Trackbar')
cv2.imshow('Trackbar', src)

# 트랙바 생성 : 'H_min' 트랙바의 이름, 범위 0~255,  
# on_trackbar : 트랙바를 움직일때 호출되는 함수(콜백함수)
cv2.createTrackbar('H_min', 'Trackbar', 0, 180, on_trackbar)
cv2.createTrackbar('H_max', 'Trackbar', 0, 180, on_trackbar)
on_trackbar(0) #창 위에 트랙바 띄우기

cv2.waitKey()
cv2.destroyAllWindows()