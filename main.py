import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if __name__ == '__main__' :

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    trackerSelection = 2
    tracker_type = tracker_types[trackerSelection]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'GOTURN':
            tracker = cv2.TrackerGOTURN_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()
        if tracker_type == "CSRT":
            tracker = cv2.TrackerCSRT_create()

    # Read video
    fromCam = False
    if fromCam:
        video = cv2.VideoCapture(0)
    else:
        fileName = "drone1"
        video = cv2.VideoCapture(f"./resources/inputs/videos/drones/{fileName}.mp4")
    
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))

    size = (frame_width, frame_height)

    output = cv2.VideoWriter(
        f'./resources/outputs/videos/drones/{fileName}/{tracker_types[trackerSelection]}.mp4',
        cv2.VideoWriter_fourcc(*'MJPG'),
        30,
        size
    )

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
   
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    firstFrame = frame
    grayFirstFrame = cv2.cvtColor(firstFrame, cv2.COLOR_RGB2GRAY)
    firstBBox = bbox

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    okCount = 0
    accuracyResultArray = []

    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)

            output.write(frame)

            ### Calculate Accuracy

            grayFrame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            dp = 0
            for i in range(int(bbox[0]), int(bbox[0] + bbox[2])):
            	for j in range(int(bbox[1]), int(bbox[1] + bbox[3])):
                    if grayFirstFrame[i][j] == grayFrame[i][j]:
                        dp += 1
            f1 = dp / (firstBBox[2] * firstBBox[3])
            cv2.putText(frame, "Accuracy Result : " + str(f1), (100,100), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
            accuracyResultArray.append(f1)
            print(f1)

        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255), 2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)
    
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2)

        # Display result
        cv2.imshow("Tracking", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break

# write objects 
video.release() 
output.release() 
    
# Closes all the frames 
cv2.destroyAllWindows()