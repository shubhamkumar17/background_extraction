import cv2
import numpy as np

#Step Background Extraction
cap = cv2.VideoCapture('highway.mp4')
_,f=cap.read()
avg = np.float32(f)
i=400 #Variable used for no. of frames
#We got clear Background for highway.mp4 video by taking 400 frames,but this can vary video to video.
while(i):
    ret, img = cap.read()
    cv2.accumulateWeighted(img,avg,0.01)
    final = cv2.convertScaleAbs(avg)
    i-=1

cv2.imshow('Final', final) #final output
cv2.imwrite('BG1.jpg',final) #saving output image
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
