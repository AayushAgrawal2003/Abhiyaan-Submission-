from __future__ import print_function
import cv2 as cv
import numpy as np
import argparse
import random as rng
rng.seed(12345)
def thresh_callback(val):
    threshold = val
    
    canny_output = cv.Canny(src, threshold*0.5, threshold * 3)

    _, contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    minEllipse = [None]*len(contours)
    for i, c in enumerate(contours):
        if c.shape[0] > 900:
            minEllipse[i] = cv.fitEllipse(c)
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i, c in enumerate(contours):
        color = (255,255,255)
        
        if c.shape[0] > 40:
            cv.drawContours(drawing, contours, i, color)
            cv.ellipse(drawing, minEllipse[i], color, 2)

    #cv.imshow('Contours', drawing)
    cv.imshow('Contours',drawing)
    return canny_output

cap = cv.VideoCapture('test1.mp4')

if(cap.isOpened() == False):
    print("Nope")

while(cap.isOpened()):
    ret,frame = cap.read()        
    src = frame
    if ret == True:
        
        source_window = 'Source'
        cv.namedWindow(source_window)
        max_thresh = 255
        thresh = 255
        cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)
        sec = thresh_callback(thresh)

        #blob detection
        params = cv.SimpleBlobDetector_Params()
        

        params.filterByArea = True
        params.minArea = 300

        params.filterByCircularity = True
        params.minCircularity = 0.30

        params.filterByConvexity = True
        params.minConvexity = 0.65

        params.filterByInertia = True
        params.minInertiaRatio = 0.000001


        detector = cv.SimpleBlobDetector_create(params)
        keypoints = detector.detect(sec)
        blank = np.zeros((1, 1))
        blobs = cv.drawKeypoints(src, keypoints, blank, (0, 0, 255),
                                cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        number_of_blobs = len(keypoints)
        text = "Number of Circular Blobs: " + str(len(keypoints))
        cv.putText(blobs, text, (20, 550),cv.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
        
        # Show blobs
        cv.imshow("Filtering Circular Blobs Only", blobs)


        if cv.waitKey(25) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()