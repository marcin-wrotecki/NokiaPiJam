import cv2
import numpy as np
import os
import requests


URL = "http://127.0.0.1:5000/"

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

names = ["Michal", "Marcin"]

# capture video with VideoCapture and optionally set width and height
cam = cv2.VideoCapture(0)

while True:
    # read frame from camera
    ret, img = cam.read()
    # convert image to gray with cvtColor
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces on grayscale image using detectMultiScale from faceCascade
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)
    # check how many faces were detected
    # if face is detected predict face from trained ones using
    # recognizer.predict (which takes part of image) and send post request with detected name
    result = "empty"
    if len(faces):
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            arg = gray[y : y + h, x : x + w]
            print("{}".format(recognizer.predict(arg)))
            result = names[recognizer.predict(arg)[0]-1]
    else:
        print("empty")
    requests.post("http://127.0.0.1:5000",data=result)
    # # if no face detected send empty string

    cv2.imshow('camera',img) # can be removed at the end

    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
#requests.post("http://127.0.0.1:5000", data=result)
cam.release()
cv2.destroyAllWindows()

