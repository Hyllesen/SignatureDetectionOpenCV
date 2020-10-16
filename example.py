import numpy as np
import cv2

image = cv2.imread("C:\\sig1.jpg")
result = image.copy()
grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(grayScale, 110, 255, cv2.THRESH_BINARY)[1]
lower = np.array([155, 38, 0])
upper = np.array([145, 255, 255])
mask = cv2.inRange(image, lower, upper)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
close = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

cnts = cv2.findContours(close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cv2.drawContours(image, cnts, -1, (0,255,0), 3)

imgS = cv2.resize(mask, (800, 600))
cv2.imshow('image', imgS)
cv2.waitKey()

# boxes = []
# for c in cnts:
#     (x, y, w, h) = cv2.boundingRect(c)
#     boxes.append([x,y, x+w,y+h])

# boxes = np.asarray(boxes)
# left = np.min(boxes[:,0])
# top = np.min(boxes[:,1])
# right = np.max(boxes[:,2])
# bottom = np.max(boxes[:,3])

# result[close==0] = (255,255,255)
# ROI = result[top:bottom, left:right].copy()
# cv2.rectangle(result, (left,top), (right,bottom), (36, 255, 12), 2)

# cv2.imshow('result', result)
# cv2.imshow('ROI', ROI)
# cv2.imshow('close', close)
# cv2.imwrite('result.png', result)
# cv2.imwrite('ROI.png', ROI)
# cv2.waitKey()