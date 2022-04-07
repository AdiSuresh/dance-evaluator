import os
import cv2
import mediapipe as mp
import pandas as pd


video_path = r'fyp-gui/videos/young-man-walking-listening-to-music-from-his-headphones.mp4'

# takes video path and creates csv

def catch_pose():
    save_output=True
    op_path = './output/Upload'

    cap = cv2.VideoCapture(video_path)
    # We don't need to show the video feed
    # mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose

    with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
        frame_number = 0
        pose_at_frame = []
        while cap.isOpened():
            flag, frame = cap.read()
            if flag:
                print('reading frames')
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # make detection
                results = pose.process(frame)
                # frame.writable = True
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                landmarks = []
                for landmark in results.pose_landmarks.landmark:
                    landmarks.append({
                        'X': landmark.x,
                        'Y': landmark.y,
                        'Z': landmark.z,
                        'Visibility': landmark.visibility,
                    })
                frame_number += 1
                pose_at_frame.append({frame_number: landmarks})
                print(landmarks)
                print(len(landmarks))

                # for result in results:
                print(results)
                
                # render detections

                # I'm commenting the draw option since it is not relevant

                # mp_drawing.draw_landmarks(
                #     frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                #     mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                #     mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=2, circle_radius=2),
                # )
                # show the detected poses
                # I'm commenting this out since the user doesn't have to see 
                # the video
                # cv2.imshow('Feed', frame)
            else:
                pass

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        if save_output:
                df = pd.DataFrame(pose_at_frame)
                path = os.path.join(op_path, 'output.csv')
                df.to_csv(path)

    cap.release()
    cv2.destroyAllWindows()
