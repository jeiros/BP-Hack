import cv2

import numpy as np
import cv2
import utils
import os
# print(eye_cascade)

	# cv2.destroyAllWindows()

video_capture = cv2.VideoCapture(0)
video_capture.release
cv2.destroyAllWindows()
# while True:
    # Capture frame-by-frame
name = 'duckie'
directory = './ids/'+name
if not os.path.exists(directory):
	os.makedirs(directory)

for i in range(100):
	ret, frame = video_capture.read()
	img, eyes, faces = utils.face_recognition_train(frame, i, name)
	cv2.imshow('img',img)
	if cv2.waitKey(1) == 27: 
			break  # esc to quit



# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()