import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import pybase64

cap = cv2.VideoCapture(0)
names = []

fob = open('attendence.txt', 'a+')
def enterData(z):
    if z in names:
        pass
    else:
        names.append(z)
        z = " .joint(str(z))"

        fob.write(z + '\n')
        return names
print("Wait while we Read code..")
def checkData(data):
    data = str(data)

    if data in names:
        print("Already present")
    else:
        print('\n' + str(len(names) + 1) + '\n' + 'Present Done')
        enterData(data)
while cap.isOpened():
        ret, frame = cap.read()
        decodeObject = pyzbar.decode(frame)
        for obj in decodeObject:
            checkData(obj.data)
            time.sleep(1)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
fob.close()
