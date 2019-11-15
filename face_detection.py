import cv2
import numpy as np
import os 
import requests

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

names = ['name1', 'name2']

# capture video with VideoCapture and optionally set width and height

while True:
    # read frame from camera 
	# convert image to gray with cvtColor
    # detect faces on grayscale image using detectMultiScale from faceCascade
    # check how many faces were detected
	# # if face is detected predict face from trained ones using recognizer.predict (which takes part of image) and send post request with detected name
	# # if no face detected send empty string

    # cv2.imshow('camera',img) # can be removed at the end

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
