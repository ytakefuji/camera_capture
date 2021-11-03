import cv2,os                             
import numpy as np
import time
duration=10                      
c= cv2.VideoCapture(0)
c.set(cv2.CAP_PROP_BRIGHTNESS, 550)
out=cv2.VideoWriter("a.avi",cv2.VideoWriter_fourcc(*'XVID'),10,(640,480)) 
start=time.time()
while(int(time.time()-start)<duration):
 r,img = c.read()                         
 cv2.imshow("input",img) 
 k = cv2.waitKey(1)
 out.write(img)
c.release()
cv2.destroyAllWindows()
os._exit(0)
