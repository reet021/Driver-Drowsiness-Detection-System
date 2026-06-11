import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance
import pygame
import time

pygame.mixer.init()

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

LEFT_EYE = [33,160,158,133,153,144]
RIGHT_EYE = [362,385,387,263,373,380]

EAR_THRESHOLD = 0.22
DROWSY_SECONDS = 2

alarm_playing = False
closed_start = None

def eye_aspect_ratio(eye):

    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    return (A + B) / (2.0 * C)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:

        face = results.multi_face_landmarks[0]

        h, w, _ = frame.shape

        left_eye = []
        right_eye = []

        for idx in LEFT_EYE:

            x = int(face.landmark[idx].x * w)
            y = int(face.landmark[idx].y * h)

            left_eye.append((x,y))

        for idx in RIGHT_EYE:

            x = int(face.landmark[idx].x * w)
            y = int(face.landmark[idx].y * h)

            right_eye.append((x,y))

        leftEAR = eye_aspect_ratio(left_eye)
        rightEAR = eye_aspect_ratio(right_eye)

        ear = (leftEAR + rightEAR)/2

        cv2.putText(
            frame,
            f"EAR: {ear:.2f}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        if ear < EAR_THRESHOLD:

            if closed_start is None:
                closed_start = time.time()

            elapsed = time.time() - closed_start

            if elapsed > DROWSY_SECONDS:

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (80,100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3
                )

                if not alarm_playing:

                    pygame.mixer.music.load("alarm.wav")
                    pygame.mixer.music.play(-1)

                    alarm_playing = True

        else:

            closed_start = None

            if alarm_playing:

                pygame.mixer.music.stop()
                alarm_playing = False

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
