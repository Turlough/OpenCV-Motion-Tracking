# Motion Tracking using OpenCV (Python)
Detects motion in a removte video stream, and displays bounding rectangles around anything that is moving within the frame

## mjpg.py
Mjpg.py keeps the video stream parsing code separate from the motion detection code

## object_tracking.py
This is responsible for detection the contours around the moving elements of the stream, and their surrounding rectangles.
