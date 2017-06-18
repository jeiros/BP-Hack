import cv2

import numpy as np
import cv2

def face_recognition(img, i = 1):
	face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./haarcascade_eye_tree_eyeglasses.xml')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	eyes = None

	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		# img = roi_gray
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv2.imshow('img',img)
	key = cv2.waitKey(1) & 0xFF
	# cv2.imwrite('ids/axel/'+str(i)+'.jpg', img)
	return img, eyes, faces

def face_recognition_2(img):
	face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./haarcascade_eye_tree_eyeglasses.xml')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	eyes = None
	print(faces)
	face = []
	coor = []
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		face.append(roi_color)
		coor.append((x,y,w,h))
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		break
	return img, face, coor

def face_recognition_train(img, i = 1, name = 'unknown'):
	face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('./haarcascade_eye_tree_eyeglasses.xml')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	eyes = None
	roi_gray = None
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		img = roi_gray
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		break
	cv2.imshow('img',img)
	key = cv2.waitKey(1) & 0xFF
	if roi_gray is not None:
		cv2.imwrite('ids/'+name+'/'+str(i)+'.jpg', img)
	return img, eyes, faces