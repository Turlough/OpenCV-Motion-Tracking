import numpy as np
import cv2
import mjpg


url = 'http://172.16.92.210:8081' 

frameName = 'image'
threshold = 250             # Minimum area to trigger detection
boxColor = (0, 255, 255)    # Colour for bounding rectangle
borderThickness = 1         # Border thickness for bounding rectangle
background = 0.5            # Range 0 to 1 how faded the non-moving background should be

fgbg = cv2.createBackgroundSubtractorMOG2()

def callback(jpg):
    '''
        Callback for stream_reader. 
        What to do with each frame of the video stream.
    '''
    img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
    image_np = np.array(img)
    fgmask = fgbg.apply(image_np)

    polygons = []

    # The contours themselves are polgons, and could be used instead of bounding rectangle
    contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # But if we want bounding rectangles, this is how...
    
    for c in contours:
        if cv2.contourArea(c) < threshold:
            continue

        (x, y, w, h) = cv2.boundingRect(c) 
        corners = [ (x, y), (x+w, y), (x+w, y+h), (x, y+h) ]
        rect = np.array(corners)

        # Overlays each rectangle perimeter on the image
        cv2.rectangle(image_np, corners[0], corners[2], boxColor, borderThickness)
        
        # Use either the original contour or bounding rectangle. Comment out whichever.
        
        # polygons.append(c) # Use the original contour as mask
        polygons.append(rect) # Use the bounding rectangle as mask

    mask = np.zeros_like(image_np)   
    cv2.fillPoly(mask, polygons, (255, 255, 255))
    masked = cv2.bitwise_and(image_np, mask)

    merged = cv2.addWeighted(image_np, background, masked, 1, 1)

    cv2.imshow(frameName, cv2.resize(merged, (800, 600)))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        cap.release()



if __name__ == '__main__':
    '''
        Main...
    '''
    mjpg.get_frames(url, callback)