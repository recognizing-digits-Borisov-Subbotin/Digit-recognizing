#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import cv2
import numpy as np

# built-in module
import sys

def split2d(img, cell_size, flatten=True):
    h, w = img.shape[:2]
    sx, sy = cell_size
    cells = [np.hsplit(row, w//sx) for row in np.vsplit(img, h//sy)]
    cells = np.array(cells)
    if flatten:
        cells = cells.reshape(-1, sy, sx)
    #print (cells)
    return cells

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

    gray = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY)
    #edge = cv2.Canny(gray, thrs1, thrs2, apertureSize=5)
    digits = split2d(gray, (50, 50))
    print (len(digits))
    h, w = gray.shape[:2]
    print (w)
    sx = 50
    x = w/sx
    mas_false = []
    for c in digits:
        edge = cv2.Canny(c, thrs1, thrs2, apertureSize=5)
        (cnts,a,b) = cv2.findContours(edge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        a = sorted(a, key = cv2.contourArea, reverse = True)[:1]
        area_test = cv2.arcLength(a[0],True)
        print (area_test)
        if (abs(area_test - area_1) <= 5 or abs(area_test - area_2) <= 5 or abs(area_test - area_3) <= 5 or abs(area_test - area_4) <= 5 or abs(area_test - area_5) <= 5):
            print ("true")
            mas_false.append(1)
        else:
            print ("false")
            mas_false.append(0)
    count = 0
    for i in mas_false:
        if count < x:
            print (i, end = ' ')
            #print (" ")
            count = count + 1
        else:
            count = 1
            print ('\n', end = '')
            print (i, end = ' ')
    print ('\n', end = '')
    cv2.imshow('edge', img_test)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
