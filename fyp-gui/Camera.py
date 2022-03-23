# import the opencv library
import cv2 as cv

# define a video capture object
vid = cv.VideoCapture(0)

while(True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # To flip the camera
    flipped = cv.flip(frame, flipCode = 1)

    # Display the resulting frame
    cv.imshow('frame', flipped)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the capture object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()