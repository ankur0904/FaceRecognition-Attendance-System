import cv2
import numpy as np
import face_recognition

img_foo = face_recognition.load_image_file('foo1.jpg')
img_foo = cv2.cvtColor(img_foo, cv2.COLOR_BGR2RGB)

img_foo_test = face_recognition.load_image_file('foo3.jpg')
img_foo_test = cv2.cvtColor(img_foo_test, cv2.COLOR_BGR2RGB)  

faceLocation = face_recognition.face_locations(img_foo)[0]
encoded_foo_image = face_recognition.face_encodings(img_foo)[0]
cv2.rectangle(img_foo, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (255, 0, 255), 2)

faceLocation_test = face_recognition.face_locations(img_foo_test)[0]
encoded_foo_image_test = face_recognition.face_encodings(img_foo_test)[0]
cv2.rectangle(img_foo_test, (faceLocation_test[3], faceLocation_test[0]), (faceLocation_test[1], faceLocation_test[2]), (255, 0, 255), 2)

result = face_recognition.compare_faces([encoded_foo_image], encoded_foo_image_test)
face_dis = face_recognition.face_distance([encoded_foo_image], encoded_foo_image_test)
print(face_dis)
cv2.putText(img_foo_test, f'{result} {round(face_dis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('foo', img_foo) 
cv2.imshow('foo Test', img_foo_test)
cv2.waitKey(0)
