#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

# relative module
import video

# built-in module
import sys


if __name__ == '__main__':
    print(__doc__)

    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cv2.namedWindow('edge')
    cv2.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
    cv2.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

    img_1 = cv2.imread('../data/digit_1.png',1)
    img_2 = cv2.imread('../data/digit_2.png',1)
    img_3 = cv2.imread('../data/digit_3.png',1)
    img_4 = cv2.imread('../data/digit_4.png',1)
    img_5 = cv2.imread('../data/digit_5.png',1)
    img_test = cv2.imread('../data/4_6.png',1)
    
    thrs1 = cv2.getTrackbarPos('thrs1', 'edge')
    thrs2 = cv2.getTrackbarPos('thrs2', 'edge')
    
    gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    
    (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
    area_1 = cv2.arcLength(a[0],True)
    print (area_1)
    
    gray = cv2.cvtColor(img_2, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    
    (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
    area_2 = cv2.arcLength(a[0],True)
    print (area_2)
    
    gray = cv2.cvtColor(img_3, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    
    (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
    area_3 = cv2.arcLength(a[0],True)
    print (area_3)
    
    gray = cv2.cvtColor(img_4, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    
    (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
    area_4 = cv2.arcLength(a[0],True)
    print (area_4)
    
    gray = cv2.cvtColor(img_5, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    
    (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
    area_5 = cv2.arcLength(a[0],True)
    print (area_5)
