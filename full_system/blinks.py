# import the necessary packages
from scipy.spatial import distance as dist
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import configuration as conf
import numpy as np

def euclidean(a, b):
	xa = a[0]*1.0
	xb = b[0]*1.0
	ya = a[1]*1.0
	yb = b[1]*1.0
	return np.sqrt((xa-xb)**2 + (ya-yb)**2)

def eye_aspect_ratio(eye):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates
	# A = dist.euclidean(eye[1], eye[5])
	A = euclidean(eye[1],eye[5])
 	B = euclidean(eye[2],eye[4])
	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
	C = euclidean(eye[0],eye[3])
 
	# compute the eye aspect ratio
	ear = (A + B) / (2.0 * C)
 
	# return the eye aspect ratio
	return ear


def mouth_aspect_ratio(mouth):
	# compute the euclidean distances between the two sets of
	# vertical eye landmarks (x, y)-coordinates

 	A = euclidean(mouth[2],mouth[8])
	# compute the euclidean distance between the horizontal
	# eye landmark (x, y)-coordinates
 	C = euclidean(mouth[0],mouth[7])
 
	# compute the eye aspect ratio
	mouth = (A ) / (1.0 * C)
 
	# return the eye aspect ratio
	return mouth
def eyes_ratio(leftEye, rightEye):
	leftEAR = eye_aspect_ratio(leftEye)
	rightEAR = eye_aspect_ratio(rightEye)
	ear = (leftEAR + rightEAR) / 2.0
	return ear

def blinking(ear, COUNTER, TOTAL):
	#  check to see if the eye aspect ratio is below the blink
	# threshold, and if so, increment the blink frame counter
	if ear < conf.AR_THRESHOLD['eye']:
		COUNTER += 1

	# otherwise, the eye aspect ratio is not below the blink
	# threshold
	else:
		# if the eyes were closed for a sufficient number of
		# then increment the total number of blinks
		if COUNTER >= conf.AR_CONSEC_FRAMES['eye']:
			TOTAL += 1

		# reset the eye frame counter
		COUNTER = 0
	return TOTAL, COUNTER

def cycle_key(key, ar, counter_asleep):
	ASLEEP = False
	val = counter_asleep.get(key,[])
	if ar < conf.AR_THRESHOLD[key]:
		if len(val) < conf.VALUES_CHECK:
			val.append(1)
		else:
			val.pop(0)
			val.append(1)
		if sum(val)/(1.0*len(val)) > conf.THRESHOLD[key]:
			ASLEEP = 1
	else:
		if len(val) < conf.VALUES_CHECK:
			val.append(0)
		else:
			val.pop(0)
			val.append(0)
	counter_asleep[key] = val
	return ASLEEP, counter_asleep

def eyes_asleep(dict_face, counter_asleep):
	ar = eyes_ratio(dict_face['leftEye'], dict_face['rightEye'])
	return cycle_key('eye', ar, counter_asleep)

def mouth_asleep(dict_face, counter_asleep):
	ar = mouth_aspect_ratio(dict_face['mouth'])
	return cycle_key('mouth', -ar, counter_asleep)

def check_asleep(dict_face, counter_asleep):
	ASLEEP_eye, counter_asleep = eyes_asleep(dict_face, counter_asleep)
	ASLEEP_mouth, counter_asleep = mouth_asleep(dict_face, counter_asleep)
	ASLEEP = ASLEEP_eye | ASLEEP_mouth
	return ASLEEP, counter_asleep


def initiate_asleep_detector(frames_count, counter_asleep, detector, predictor, vs):
	ASLEEP = 0
	# grab the indexes of the facial landmarks for the left and
	# right eye, respectively
	(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
	(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
	(nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]
	(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
	(jStart, jEnd) = face_utils.FACIAL_LANDMARKS_IDXS["jaw"]
	# start the video stream thread
	# print("[INFO] starting video stream thread...")
	fileStream = True
	# vs = VideoStream(src=0).start()
	# vs = VideoStream(usePiCamera=True).start()
	# fileStream = False
	# time.sleep(1.0)
	dict_face = {}

	# if this is a file video stream, then we need to check if
	# there any more frames left in the buffer to process
	# if fileStream and not vs.more():
	# 	break

	# grab the frame from the threaded video file stream, resize
	# it, and convert it to grayscale
	# channels)
	if conf.is_raspi == False:
		ret, frame = vs.read()
		if frame == None:
			return None, None, None, None
	else:
		camera.capture(vs, 'bgr', use_video_port=True)
		frame = vs.array
	frame = imutils.resize(frame, width=600)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces in the grayscale frame
	rects = detector(gray, 0)
	# loop over the face detections
	for rect in rects:
		# determine the facial landmarks for the face region, then
		# convert the facial landmark (x, y)-coordinates to a NumPy
		# array
		shape = predictor(gray, rect)
		shape = face_utils.shape_to_np(shape)

		# extract the left and right eye coordinates, then use the
		# coordinates to compute the eye aspect ratio for both eyes
		dict_face['leftEye'] = leftEye = shape[lStart:lEnd]
		dict_face['rightEye'] = rightEye = shape[rStart:rEnd]
		dict_face['nose'] = nose = shape[nStart:nEnd]
		dict_face['mouth'] = mouth = shape[mStart:mEnd]
		dict_face['jaw'] = jaw = shape[jStart:jEnd]

		# average the eye aspect ratio together for both eyes

		# compute the convex hull for the left and right eye, then
		# visualize each of the eyes
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		noseHull = cv2.convexHull(nose)
		mouthHull = cv2.convexHull(mouth)
		jawHull = cv2.convexHull(jaw)

		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [noseHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [jawHull], -1, (0, 255, 0), 1)
		if frames_count < 0:
			ear = eyes_ratio(leftEye, rightEye)
			mar = mouth_aspect_ratio(mouth)
			conf.AR_THRESHOLD['eye'] += conf.eye_factor_threshold*ear/conf.SET_INITIAL_VALUE
			conf.AR_THRESHOLD['mouth'] -= conf.mouth_factor_threshold*mar/conf.SET_INITIAL_VALUE
		else:
			ASLEEP, counter_asleep = check_asleep(dict_face, counter_asleep)
			ear = eyes_ratio(leftEye, rightEye)

			mouthAR = mouth_aspect_ratio(mouth)
			# TOTAL, COUNTER = blinking(ear, COUNTER, TOTAL)
			# draw the total number of blinks on the frame along with
			# the computed eye aspect ratio for the frame
			# cv2.putText(frame, "Blinks: {}".format(TOTAL), (10, 30),
			# 	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.putText(frame, "EAR: {:.2f}".format(ear), (440, 30),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.putText(frame, "MAR: {:.2f}".format(mouthAR), (440, 70),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			if ASLEEP == True  and frames_count>60:
				cv2.putText(frame, "ASLEEP", (250, 400),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
			break
	if len(rects) == 0:
		ASLEEP = True
		cv2.putText(frame, "TIRED", (250, 400),
				cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
	frames_count+=1


	return frame, frames_count, counter_asleep, ASLEEP