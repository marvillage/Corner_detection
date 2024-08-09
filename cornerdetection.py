# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:44:41 2024

@author: Kushagra
"""

import numpy as np
import cv2 

img = cv2.imread(r"C:\Users\Kushagra\Downloads\shapes.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#parameters (img,no.of corner,quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,100,0.01,5)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

cv2.imshow("res==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()