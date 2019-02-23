import cv2
import numpy as np

#Step Background Extraction
cap = cv2.VideoCapture('highway.mp4')
_,f=cap.read()
avg = np.float32(f)
i=200 #Variable taken for number of frames
while(i):
    ret, img = cap.read()
    cv2.accumulateWeighted(img,avg,0.01)
    final = cv2.convertScaleAbs(avg)
    cv2.imshow('RES1',final)
    i-=1

cv2.imshow('Final', final) #final output
cv2.imwrite('BG1.jpg',final) #saving output image
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
