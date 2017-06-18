from blinks import *

import cv2
import dlib
if conf.is_raspi:
    import picamera
from utils import *
from train_face import *
import Copilot.copilot as copi
def most_common(lst):
    return max(set(lst), key=lst.count)
def circle_list(circular, max_elmnts, element):
    if len(circular) >= max_elmnts:
        circular.pop(0)
        circular.append(element)
    else:
        circular.append(element)
    return circular
def main():
    # Create Copilot object.
    alicia = copi.copilot_obj()
    counter_asleep = {}
    COUNTER = 0
    TOTAL = 0
    frames_count = 0

    out = cv2.VideoWriter('./output.avi', -1, 20.0, (640,480))
    # initialize dlib's face detector (HOG-based) and then create
    # the facial landmark predictor
    print("[INFO] loading facial landmark predictor...")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(conf.shape_predictor)
    # vs = cv2.VideoCapture(1)
    # for i in range(200):
    X_pca, pca, y = train_pca()
    if conf.is_raspi:
        camera = picamera.PiCamera()
        stream = picamera.array.PiRGBArray(camera)
    else:
        stream = cv2.VideoCapture(0)
        # stream = cv2.VideoCapture('6.h264')
    no_faces = True
    detected_frames = 0
    # cv2.destroyAllWindows()
    id_person = []
    initial_val = 0
    while no_faces == True:
        ret, frame = stream.read()
        img, faces, coor = face_recognition_2(frame)
        out.write(img)

        
        if len(faces) != 0:
            detected_frames += 1
            if len(id_person) > 0:
                retrieved_id, dist = test_id(faces, X_pca, pca, y, img, coor, most_common(id_person))
                if dist < 8:
                    id_person.append(retrieved_id)
            else:
                retrieved_id, dist = test_id(faces, X_pca, pca, y, img, coor, '')
                if dist < 8:
                    id_person.append(retrieved_id)
        else:
            detected_frames = 0
        if detected_frames > 15:
            no_faces = False
        cv2.imwrite('gif/00'+str(initial_val)+'.jpg', frame)
        
        initial_val+=1
    i = 0
    if len(id_person) > 10:
        id_driver = most_common(id_person)
    else:
        id_driver = ''

    cv2.destroyAllWindows()
    key = cv2.waitKey(1) & 0xFF
    if id_driver == 'negative':
        id_driver = ''
        alicia.error_recognition()
        for i in range(100):
            ret, frame = stream.read()
            img, eyes, faces = face_recognition_train(frame, i, 'unknown')
            cv2.imshow('img',img)
            if cv2.waitKey(1) == 27: 
                    break  # esc to quit
    alicia.start(id_driver)
    list_asleep = []
    while stream.isOpened():
        print(most_common(id_person))
        frame, frames_count, counter_asleep, ASLEEP = initiate_asleep_detector(frames_count, counter_asleep, detector, predictor, stream)
        print(ASLEEP)
        ASLEEP = most_common(circle_list(list_asleep, 15, ASLEEP))
        if frame == None:
            break
        out.write(frame)
        # show the frame
        print(id_driver)
        cv2.putText(frame, id_driver, (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        cv2.imshow("Frame", frame)
        cv2.imwrite('gif/00'+str(i+initial_val)+'.jpg', frame)
        i += 1
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        # Check response for the server
        if ASLEEP and len(list_asleep)>10:
            cv2.putText(frame, "TIRED", (250, 400),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            print 'Driver is sleeping! '
            alicia.run()

        if conf.is_raspi:
            stream.seek(0)
            stream.truncate()
    # do a bit of cleanup
    # vs.stop()
    stream.release()
    out.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()
