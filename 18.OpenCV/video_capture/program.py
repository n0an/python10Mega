import cv2, time

video = cv2.VideoCapture(0)

frames_count = 0

while True:
    check, frame = video.read()

    frames_count += 1

    # print 'check = ' + str(check)
    #
    # print 'frame = ' + str(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # time.sleep(1)

    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print 'Frames captured = ' + str(frames_count)


video.release()

cv2.destroyAllWindows()