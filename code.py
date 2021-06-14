import cv2

def take_snapshot():
    # Initialising CV2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while (result):
        # Read The Frames while the camera is ON
        ret,frame = videoCaptureObject.read()
        print(ret)
        # CV2.imwrite(): method is used to save an image to any storage device.
        cv2.imwrite("NewPicture1.jpg" , frame)
        result = False
    # Releasing the Camera
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()