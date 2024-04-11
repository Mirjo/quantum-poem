# -----Step 1: Use VideoCapture in openCV-----
import cv2
import dlib
import random

line1 = "It's always dark"
line2 = "In the ancient glade"
line3 = "Across old bark"
line4 = "The quite shade"
prev_list = []
face_counter = 0
no_face_counter = 0


def print_new_poem():
    global prev_list
    poem_list = [line1, line2, line3, line4]
    while prev_list == poem_list:
        random.shuffle(poem_list)
    prev_list = poem_list

    print("\r\n")
    print("\r\n")
    print("A small quantum poem")
    print("\r\n")
    for entry in poem_list:
        print(entry)
    print("\r\n")
    print("\r\n")


# livestream from the webcam
cap = cv2.VideoCapture(0)

"""in case of a video
cap = cv2.VideoCapture("__path_of_the_video__")"""

# name of the display window in openCV
cv2.namedWindow("BlinkDetector")

# -----Step 3: Face detection with dlib-----
detector = dlib.get_frontal_face_detector()

print_new_poem()

while True:
    # capturing frame
    retval, frame = cap.read()

    # exit the application if frame not found
    if not retval:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # -----Step 2: converting image to grayscale-----
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -----Step 3: Face detection with dlib-----
    # detecting faces in the frame
    faces, _, _ = detector.run(image=frame, upsample_num_times=0, adjust_threshold=0.0)

    # -----Step 4: Detecting Eyes using landmarks in dlib-----
    if len(faces) == 0:
        face_counter = 0
        no_face_counter += 1
    else:
        face_counter += 1
        no_face_counter = 0

    if len(faces) == 0 and no_face_counter == 1:
        print_new_poem()


# releasing the VideoCapture object
cap.release()
cv2.destroyAllWindows()
