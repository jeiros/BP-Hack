from sklearn.decomposition import RandomizedPCA
import numpy as np
import glob
import cv2
import math
import os.path
import string


#function to get ID from filename
def ID_from_filename(filename):
    part = string.split(filename, '/')
    return part[1].replace("s", "")
 

#function to convert image to right format
def prepare_image_2(img_color):
    # img_color = cv2.imread(filename)
    # print(filename)
    img_color = cv2.resize(img_color, (92, 112), interpolation = cv2.INTER_CUBIC)
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    return img_gray.flat 
#function to convert image to right format
def prepare_image(filename):
    img_color = cv2.imread(filename)
    img_color = cv2.resize(img_color, (92, 112), interpolation = cv2.INTER_CUBIC)
    img_gray = cv2.cvtColor(img_color, cv2.cv.CV_RGB2GRAY)
    img_gray = cv2.equalizeHist(img_gray)
    return img_gray.flat

def face_recognition(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	eyes = None
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
	# cv2.imshow('img',img)
	# cv2.imwrite('test/adrian/'+str(i)+'.jpg', img)
	return img, face, coor

def retrieve_id(X, X_pca, pca, y):
	# run through test images (usually one)
	for j, ref_pca in enumerate(pca.transform(X)):
	    distances = []
	    # Calculate euclidian distance from test image to each of the known images and save distances
	    for i, test_pca in enumerate(X_pca):
	        dist = math.sqrt(sum([diff**2 for diff in (ref_pca - test_pca)]))
	        distances.append((dist, y[i]))
	 
	    found_ID = min(distances)[1]
	    dist = min(distances)[0]
	    print "Identified (result: "+ str(found_ID) +" - dist - " + str(min(distances)[0])  + ")"
	    return found_ID, dist


def train_pca():
	IMG_RES = 92 * 112 # img resolution
	NUM_EIGENFACES = 50 # images per train person
	NUM_TRAINIMAGES = 700 # total images in training set

	#loading training set from folder train_faces
	folders = glob.glob('ids/*')
	 
	# Create an array with flattened images X
	# and an array with ID of the people on each image y
	NUM_TRAINIMAGES = 0
	for x, folder in enumerate(folders):
	    train_faces = glob.glob(folder + '/*')
	    for i, face in enumerate(train_faces):
	        NUM_TRAINIMAGES += 1
	print(NUM_TRAINIMAGES)
	X = np.zeros([NUM_TRAINIMAGES, IMG_RES], dtype='int8')
	y = []

	# Populate training array with flattened imags from subfolders of train_faces and names
	c = 0
	for x, folder in enumerate(folders):
	    train_faces = glob.glob(folder + '/*')
	    for i, face in enumerate(train_faces):
	        X[c,:] = prepare_image(face)
	        y.append(ID_from_filename(face))
	        c = c + 1
	        if c >= NUM_TRAINIMAGES:
	        	break
	    if c >= NUM_TRAINIMAGES:
        	break
	# perform principal component analysis on the images
	pca = RandomizedPCA(n_components=NUM_EIGENFACES, whiten=True).fit(X)
	X_pca = pca.transform(X)
	return X_pca, pca, y
# load test faces (usually one), located in folder test_faces
# test_faces = glob.glob('test/*')





# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# print(eye_cascade)
# 	# cv2.destroyAllWindows()

# video_capture = cv2.VideoCapture(1)
# video_capture.release
# cv2.destroyAllWindows()
# # while True:
#     # Capture frame-by-frame
# TEST_IMG = 1
# X = np.zeros([TEST_IMG, IMG_RES], dtype='int8')

def test_id(faces, X_pca, pca, y, img, coor, most_common):
	c = 0	
	IMG_RES = 92 * 112 # img resolution
	NUM_EIGENFACES = 50 # images per train person
	NUM_TRAINIMAGES = 700 # total images in training set
	X = np.zeros([len(faces), IMG_RES], dtype='int8')
	for l,face in enumerate(faces):
		print(face)
		X[c,:] = prepare_image_2(face)
		c += 1
		if c >= 1:
			c = 0
			found_id, dist = retrieve_id(X, X_pca, pca, y)

			cv2.putText(img, most_common, (coor[l][0]-10, coor[l][1]-10),
				cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
			cv2.imshow('img',img)
			if cv2.waitKey(1) == 27: 
					break  # esc to quit1
	return found_id, dist



# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()



# # Create an array with flattened images X





 
