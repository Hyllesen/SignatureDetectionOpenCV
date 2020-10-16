import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def insertFullName(img, x, y):
    b,g,r,a = 0,0,0,0
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x, y), "Klamydia Jensen Petersen", font = font, fill = (b, g, r, a))
    img = np.array(img_pil)
    return img

fontPath = "C:\\tnr400.ttf"
font = ImageFont.truetype(fontPath, 200)

imagePath = "C:\\sig3.jpg"
imgColor = cv2.imread(imagePath)
imgColor = cv2.medianBlur(imgColor,9)
imgGray = cv2.cvtColor(imgColor, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 133, 33)

contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(imgColor, contours, -1, (0,255,0), 3)
print("Number of contours" + str(len(contours)))
x, y, w, h = 0,0,0,0
for c in contours:
    rect = cv2.boundingRect(c)
    if rect[2] < 200 or rect[3] < 200: continue    
    x,y,w,h = rect
    # print(x,y,w,h)
    # cv2.rectangle(imgColor,(x,y),(x+w,y+h),(0,0,255),5)

imgColor = cv2.bitwise_and(imgColor, imgColor, mask=thresh)
imgColor[thresh == 255] = (255, 0, 0)
imgColor[thresh == 0] = (255, 255, 255)
imgColor = insertFullName(imgColor, x, y+h/2)
fontsize = font.getsize("Klamydia Jensen Petersen")
print(fontsize[0])
print(w)
w if w > fontsize[0] else fontsize[0] 
print(w)
imgColor = imgColor[y:y+h, x:x+w]
# imgS = cv2.resize(imgColor, (800, 600))
cv2.imshow("image", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()