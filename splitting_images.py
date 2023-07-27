import cv2
import os

capture = cv2.VideoCapture(os.path.join(os.getcwd(), 'Content', 'bad_form.mp4'))
framenr = 1240

while(True):
    success, frame = capture.read()
    print("worked")

    if success:
        cv2.imwrite("/Users/Kalp/GitHubRepos/workout_app/server_side/Content/training/bad/%d.jpg" % framenr, frame)
        print("success")
    else:
        print('failed')
        break

    framenr = framenr+1
    print(framenr)

capture.release() 