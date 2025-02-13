from time import time 
import cv2 as cv
import pickle

cap = cv.VideoCapture("rtsp://192.168.1.165:554/user=admin_password=_channel=1_stream=0.sdp?real_stream")#0)#rtsp://192.168.1.4:12525/h264_ulaw.sdp')

# Define the codec and create VideoWriter object

# Desiger_FPS=30.0
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# out = cv.VideoWriter('output.avi', fourcc, Desiger_FPS , (640,  480))

every_frame=list()

if not cap.isOpened():
    print("Cannot open camera")
    exit()

period=time()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break    
    
    # # Our operations on the frame come here
    # Lable=time()-period
    # period=time()
    # cv.putText(frame,f"{Lable:.2f}" , (90, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    # every_frame.append((frame,Lable))
    
    
    # Display the resulting frame
    cv.imshow('frame', frame)
    
    # Write file and check quit!
    # out.write(frame)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


#analyses
sampel_under_mean_time =[(x[1],i) for i,x in enumerate(every_frame) if x[1]<0.03 ]
for i in [x[1] for x in sampel_under_mean_time]:
    cv.imshow("A",every_frame[83][0])
    cv.waitKey(1000)
    cv.destroyWindow('A')