import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_recording('1.h264')
    camera.wait_recording(5)
    camera.stop_recording()