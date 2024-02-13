import cv2
import numpy as np

img = cv2.imread('solar-system.jpg')
cv2.putText(img,'Sun',(20,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.putText(img,'Mercury',(120,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Venus',(220,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Earth',(320,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Mars',(420,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Jupiter',(620,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Saturn',(820,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Uranus',(1020,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,'Neptune',(1120,190),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))



cv2.imshow('display',img)


cv2.waitKey(20000)
