import cv2, time
from datetime import datetime


first_frame = None
motion_list = [ None, None ]

# Capturing video
video = cv2.VideoCapture("check.mp4")

while True:
    check, frame = video.read()
    
    # Converting color image to gray_scale then to Gaussian blur 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    # Difference between first_frame and current_frame
    diff_frame = cv2.absdiff(first_frame, gray)

    # If change is greater than 30 it will show white color(255)
    thresh_frame = cv2.threshold(diff_frame, 50, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2)

    # Finding contour of moving object
    cnts,_ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue
        motion = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        # making rectangle around the moving object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # Displaying image in gray_scale
    # cv2.imshow("Gray Frame", gray)
    
    # Displaying the difference in the current_frame to first_frame
    # cv2.imshow("Difference Frame", diff_frame)
    
    # Displaying black and white frame 
    # cv2.imshow("Threshold Frame", thresh_frame)
    
    # Displaying color frame 
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
