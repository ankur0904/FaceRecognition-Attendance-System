import cv2
import os
import face_recognition
import numpy as np
from datetime import datetime

path = 'images'

images = []
classNames = []

myImages = os.listdir(path)
for image in myImages:
    currentImage = cv2.imread(f'{path}/{image}')
    images.append(currentImage)
    classNames.append(image.split('.')[0])

def findEncoding(images):
    encodingList = []
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoding = face_recognition.face_encodings(image)[0]
        encodingList.append(encoding)

    return encodingList

def mark_attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()[1:]
        print(myDataList)
        nameList = []
        date_now = datetime.now().strftime('%d/%m/%Y')
        for line in myDataList:
            presentName, _, CSV_date = line.split(',')
            CSV_day, CSV_month, CSV_year = CSV_date.split('/')
            now_day, now_month, now_year = date_now.split('/')
            if now_day == CSV_day and now_month == CSV_month and now_year == CSV_year:
                nameList.append(presentName)
        
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString},{date_now}')

encodeListKnown = findEncoding(images)
print("Encoding completed...")

cam = cv2.VideoCapture(0)

while True:
    success, img = cam.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesInFrame = face_recognition.face_locations(imgS)
    encodedCurrentFrame = face_recognition.face_encodings(imgS, facesInFrame)

    for encodeFace, faceLoc in zip(encodedCurrentFrame, facesInFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        print(matches)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        print(matchIndex)
        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
        if matches[matchIndex] == True:
            name = classNames[matchIndex].upper()
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            mark_attendance(name)
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)


