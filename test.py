import cv2
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

webcam = cv2.VideoCapture(0)

while True:
    stream_ok, frame = webcam.read()

    if stream_ok:
        cv2.imshow('Webcam',frame)

    # write to video file
    ## video.write(frame)

    
    if cv2.waitKey(1) and  0xFF == 27:
        break

cv2.destroyAllWindows()

webcam.release()

# save video

video = VideoWriter('Webcam.avi', VideoWriter_fourcc(*'MP42'), 25.0 ,(640,480))

#video.release()

#https://www.youtube.com/watch?v=frYotHLJ-Rc

