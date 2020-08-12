# Little description about how it works.

Packages used:
opencv-python 4.2.0.32, numpy 1.19.1
 
 1. First we start the webcam. And stores the starting frame in background variable.
 2. After that we convert our normal RGB video frames to HSV so that we detect the color of the cloth.
 3. After color detection we will get color range of our cloth.
 4. We store lower values Hue, Saturation and Value in lower variable and higher values in upper variable. For making the mask.
 5. Now we make mask. After that we open the mask and Dilate the mask.
 6. Inverting the mask for front video frames.
 7. Now masking the front video with 'inverted mask' and background frame with normal mask.
 8. Adding both the result of video mask and background mask.
 9. We will get the required output.

 Tutorial related to concepts of opencv: https://youtu.be/WQeoO7MI0Bs


