from blinks import *

import cv2
import dlib
if conf.is_raspi:
    import picamera
from utils import *

def main():
    # construct the argument parse and parse the arguments
    counter_asleep = {}
    COUNTER = 0
    TOTAL = 0
    frames_count = 0
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(conf.shape_predictor)
    # vs = cv2.VideoCapture(1)
    # for i in range(200):
    if conf.is_raspi:
        camera = picamera.PiCamera()
        stream = picamera.array.PiRGBArray(camera)
    else:
        stream = cv2.VideoCapture(1)
    no_faces = True
    detected_frames = 0
    while no_faces == True:
        ret, frame = stream.read()
        img, eyes, faces = face_recognition(frame)
        print(faces)
        if len(faces) != 0:
            detected_frames += 1
        else:
            detected_frames = 0
        if detected_frames > 5:
            no_faces = False

    while 1:

        frame, frames_count, counter_asleep, ASLEEP = initiate_asleep_detector(frames_count, counter_asleep, detector, predictor, stream)

        # show the frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        # Check response for the server
        response = False #
        if response is True and ASLEEP:
            print 'Asleep !!!!! '
            send = True# send_trigger()

        if response:
            break
        if conf.is_raspi:
            stream.seek(0)
            stream.truncate()
    # do a bit of cleanup
    cv2.destroyAllWindows()
    # vs.stop()


# Entry point of the script
if __name__ == "__main__":
    main()
