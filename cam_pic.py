import cv2,os
import numpy as np
from time import sleep

c= cv2.VideoCapture(0)
#c.set(cv2.CAP_PROP_FRAME_WIDTH,160)
#c.set(cv2.CAP_PROP_FRAME_HEIGHT,160)
c.set(cv2.CAP_PROP_BRIGHTNESS, 550)
sleep(1)
r,img = c.read()
cv2.imwrite('a.png',img)
k = cv2.waitKey(0)
c.release()
cv2.destroyAllWindows()
os._exit(0)
