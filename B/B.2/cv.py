import cv2
import numpy as np
cap = cv2.VideoCapture('test2.mp4')

if(cap.isOpened() == False):
    print("Nope")

while(cap.isOpened()):
    ret,frame = cap.read()

    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0,0,168])
        upper_white = np.array([172,111,255])
        mask = cv2.inRange(hsv, lower_white, upper_white)
        res = cv2.bitwise_and(frame,frame, mask= mask)
        grayFrame = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)


        #params
        params = cv2.SimpleBlobDetector_Params()
        params.minThreshold = 10
        params.maxThreshold = 200

        params.filterByArea = True
        params.minArea = 150

        params.filterByCircularity = True
        params.minCircularity = 0.3
        params.blobColor = 255

        params.filterByConvexity = True
        params.minConvexity = 0.87

        params.filterByInertia = True
        params.minInertiaRatio = 0.001
        params.maxInertiaRatio = 1

        detector = cv2.SimpleBlobDetector_create(params)
        keypoints = detector.detect(res)
        blank = np.zeros((1, 1))
        blobs = cv2.drawKeypoints(res, keypoints, blank, (0, 0, 255),
                                cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        
        number_of_blobs = len(keypoints)
        text = "Number of Circular Blobs: " + str(len(keypoints))
        cv2.putText(blobs, text, (20, 550),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
        
        # Show blobs
        cv2.imshow("Filtering Circular Blobs Only", blobs)
                                
        #cv2.imshow('grayscale',grayFrame)
            #cv2.imshow('res',res)

        if cv2.waitKey(25) == ord('q'):
            break
    else:
        break 



cap.release()
cv2.destroyAllWindows()


