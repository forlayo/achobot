# USAGE
# python magiceye.py

# import the necessary packages
import win32api

import keyboard as keyboard
import pygame as pygame
import pythoncom
import win32con
from PIL import ImageGrab
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import cv2
import pyautogui

# construct the argument parse and parse the arguments
from keyboard._mouse_event import RIGHT

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=False,
                help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=False,
                help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.6,
                help="minimum probability to filter weak detections")
args = vars(ap.parse_args())
prott1 = 'MobileNetSSD_deploy.prototxt.txt'
prott2 = 'MobileNetSSD_deploy.caffemodel'
# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(prott1, prott2)

# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
# time.sleep(2.0)
# fps = FPS().start()

# loop over the frames from the video stream
HSX = 100;
LSX = 1000;
HSY = 100;
LSY = 1000;
HEX = 100;
LEX = 1000;
HEY = 100;
LEY = 1000;

while True:
    # grab the frame from the threaded video stream and resize it
    # to have a maximum width of 400 pixels

    frame = np.array(ImageGrab.grab(bbox=(0, 40, 1820, 1240)))
    # frame = imutils.resize(frame, width=400)

    # grab the frame dimensions and convert it to a blob
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                                 0.007843, (300, 300), 127.5)

    # pass the blob through the network and obtain the detections and
    # predictions
    net.setInput(blob)
    detections = net.forward()

    # loop over the detections
    for i in np.arange(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the `confidence` is
        # greater than the minimum confidence
        if confidence > args["confidence"]:
            # extract the index of the class label from the
            # `detections`, then compute the (x, y)-coordinates of
            # the bounding box for the object
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # draw the prediction on the frame
            label = "{}: {:.2f}%".format(CLASSES[idx],
                                         confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                          COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
            if 'person' in label:
                pygame.init()
                pygame.event.get()
                if pygame.mouse.get_pressed():
                    print
                    'pressing'
                    # tried to detect my character's offset and add the best way to exclude it, failed most tests.
                    if startX > 369 & startX < 1402 & startY > -1 & startY < 725 & endX > 339 & endX < 1805 & endY > 806 & endY < 1017:
                        print
                        'found myself'
                    else:
                        # print 'found somebody else'
                        nosum = int(round(startX * 1)) + int(round(startX * 0.06))
                        nosum2 = int(round(y * 1)) + int(round(y * 0.7))
                        halfX = (endX - startX) / 2
                        halfY = (endY - startY) / 2
                        finalX = startX + halfX
                        finalY = startY + halfY
                        #pyautogui.moveTo(finalX, finalY)
                        # win32api.SetCursorPos((finalX, finalY))
                        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, int(finalX), int(finalY), 0, 0)
                        #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, int(finalX), int(finalY), 0, 0)
                        # print 'Pressed L'
                    if 'HSX' not in locals():
                        HSX = startX
                    if 'LSX' not in locals():
                        LSX = startX
                    if 'HSY' not in locals():
                        HSY = startY
                    if 'LSY' not in locals():
                        LSY = startY

                    if 'HEX' not in locals():
                        HEX = endX
                    if 'LEX' not in locals():
                        LEX = endX
                    if 'HEY' not in locals():
                        HEY = endY
                    if 'LEY' not in locals():
                        LEY = endY

                    if startX > HSX:
                        HSX = startX
                    if startX < LSX:
                        LSX = startX
                    if startY > HSY:
                        HSY = startY
                    if startY < LSY:
                        LSY = startY

                    if endX > HEX:
                        HEX = endX
                    if endX < LEX:
                        LEX = endX
                    if endY > HEY:
                        HEY = endY
                    if endY < LEY:
                        LEY = endY

                    print
                    'HStartX: ' + str(HSX)
                    print
                    'LStartX: ' + str(LSX)
                    print
                    'HStartY: ' + str(HSY)
                    print
                    'LStartY: ' + str(LSY)
                    print
                    'HendX: ' + str(HEX)
                    print
                    'LendX: ' + str(LEX)
                    print
                    'HendY: ' + str(HEY)
                    print
                    'LendY: ' + str(LEY)

                # print args["confidence"]

    #             click(10,10)

    # show the output frame
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    # update the FPS counter

# stop the timer and display FPS information


# do a bit of cleanup
cv2.destroyAllWindows()