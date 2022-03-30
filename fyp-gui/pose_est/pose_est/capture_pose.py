import os
import cv2
import mediapipe as mp
import pandas as pd

# Capture Pose stands for Camara stuff

op_path = './output/Upload'


def start_capture(path=0, save_output=False):
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    cap = cv2.VideoCapture(path)

    pose_at_frame = []
    calc_timestamps = []
    offset = 0.0
    landmark_dict = {
        0: 'Head_end',
        11: 'UpperArmL',
        12: 'UpperArmR',
        13: 'LoweArmL',
        14: 'LoweArmR',
        15: 'HandL',
        16: 'HandR',
        23: 'Hip.L',
        24: 'Hip.R',
        25: 'ShinL',
        26: 'ShinR',
        27: 'FootL',
        28: 'FootR',
        31: 'FootL_end',
        32: 'FootR_end'
    }
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            flag, frame = cap.read()

            if flag:
                if len(calc_timestamps) == 0:
                    offset = cap.get(cv2.CAP_PROP_POS_MSEC)
                    calc_timestamps.append(0.0)
                else:
                    calc_timestamps.append(calc_timestamps[-1] + cap.get(cv2.CAP_PROP_POS_MSEC) - offset)

                results = pose.process(frame)

                landmarks = dict()
                keys = landmark_dict.keys()
                if results.pose_landmarks is not None:
                    for index, landmark in enumerate(results.pose_landmarks.landmark):
                        if index in keys:
                            landmarks[landmark_dict[index]] = [landmark.x,
                                                               landmark.y,
                                                               landmark.z]

                    pose_at_frame.append({
                        'timestamp': calc_timestamps[-1],
                        'landmarks': landmarks,
                    })

                    # render detections
                    mp_drawing.draw_landmarks(
                        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                        mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                        mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
                    )

                # To flip the camera
                flipped = cv2.flip(frame, flipCode = 1)

                # show the detected poses
                cv2.imshow("Mediapipe feed", flipped)
            else:
                break

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

    if save_output:
        df = pd.DataFrame(pose_at_frame)
        path = os.path.join(op_path, 'output.csv')
        df.to_csv(path)

    cap.release()
    cv2.destroyAllWindows()
