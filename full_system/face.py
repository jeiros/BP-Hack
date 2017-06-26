import cv2

import numpy as np
import cv2
import utils
import os
from train_face import *
# print(eye_cascade)

	# cv2.destroyAllWindows()
def most_common(lst):
    return max(set(lst), key=lst.count)
def circle_list(circular, max_elmnts, element):
    if len(circular) >= max_elmnts:
        circular.pop(0)
        circular.append(element)
    else:
        circular.append(element)
    return circular
video_capture = cv2.VideoCapture(0)
video_capture.release
cv2.destroyAllWindows()
# while True:
    # Capture frame-by-frame
name = 'hugo'
directory = './ids/'+name
if not os.path.exists(directory):
	os.makedirs(directory)
	for i in range(100):
		ret, frame = video_capture.read()
		img, eyes, faces = utils.face_recognition_train(frame, i, name)
		cv2.imshow('img',img)
		if cv2.waitKey(1) == 27: 
				break  # esc to quit
no_faces = True
id_person = []
stream = video_capture
detected_frames = 0
X_pca, pca, y = train_pca()
while no_faces == True:
    ret, frame = stream.read()
    img, faces, coor = utils.face_recognition_2(frame)

    
    if len(faces) != 0:
        detected_frames += 1
        if len(id_person) > 0:
            retrieved_id, dist = test_id(faces, X_pca, pca, y, img, coor, most_common(id_person))
            if dist < 8:
                circle_list(id_person, 15, retrieved_id)
        else:
            retrieved_id, dist = test_id(faces, X_pca, pca, y, img, coor, '')
            if dist < 8:
                circle_list(id_person, 15, retrieved_id)
    else:
        detected_frames = 0
        id_person = []

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()