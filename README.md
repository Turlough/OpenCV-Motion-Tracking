# Motion Tracking using OpenCV (Python)
Detects motion in a removte video stream, and displays bounding rectangles around anything that is moving within the frame

## mjpg.py
Mjpg.py keeps the video stream parsing code separate from the motion detection code

## object_tracking.py
This is responsible for detection the contours around the moving elements of the stream, and their bounding rectangles.

Uncomment line 44 (`polygons.append(c)`) and comment line 45 (`polygons.append(rect)`) to show the original contour instead of the bounding rectangles.

Edit the variables at the top of the file to change stuff like trigger threshold etc.

## Video source
Replace the url at line 6 with a valid url from an mpeg video source, or edit the code to use a local camera instead.
