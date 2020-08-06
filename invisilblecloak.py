# Imported all the required Library
import cv2 as cv
import numpy as np


# Turning on Webcam.
cam = cv.VideoCapture(0) # 0 for default Webcam of Laptop. 0 is the port number.

# Looping the for capturing the starting frames for background. 
for i in range(50): # it depends on us how much we want to loop.
    success, background = cam.read() # success variable stores True boolean and background variable stores frames for background which we will be using letter.
background = cv.flip(background, 1) # background variable stores last frame.

# Webcam loop
while True:
    success, img = cam.read() # success variable stores True boolean and img variable stores frames.
    mirror_img = cv.flip(img, 1) # fliping the frames for getting output in mirror image format.
    hsv = cv.cvtColor(mirror_img, cv.COLOR_BGR2HSV) # Converting the frames into hsv. For getting the color range of blue cloth by using color detection 
   
    lower = np.array([97, 146, 91]) # Lower value of Hue, Saturation, Value respectively
    upper = np.array([104, 255, 255]) # Upper value of Hue, Saturation, Value respectively

    mask = cv.inRange(hsv, lower, upper) # Making a mask
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, np.ones((3, 3), np.uint8)) # Opening th Mask
    mask = cv.morphologyEx(mask, cv.MORPH_DILATE, np.ones((3, 3), np.uint8)) # Dilating the mask
    
    mask_not = cv.bitwise_not(mask) # Inverting the mask
    
    result_img = cv.bitwise_and(mirror_img, mirror_img, mask=mask_not) # Bitwise and operation for front img and using mask_not for mask
    result_background = cv.bitwise_and(background, background, mask=mask) # Bitwise and opertaion for background and using mask for mask

    final_result = cv.addWeighted(result_img, 1, result_background, 1, 0) # Adding both front and background ouput to get final result.
    
    cv.imshow('invisible_cloak', final_result) # Showing the output 
    cv.imshow('original', mirror_img) # Showind the original recording


# Press 'q' for terminating the program
    if cv.waitKey(1) == ord('q'): 
        break
