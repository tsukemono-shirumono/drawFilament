import cv2
import numpy as np#行列演算
def drawFilament(img,ps,color,line=2):
    for p1,p2 in zip(ps[:-1,:],ps[1:,:]):
        img=cv2.line(img, tuple(p1), tuple(p2), color, line)
    return img
