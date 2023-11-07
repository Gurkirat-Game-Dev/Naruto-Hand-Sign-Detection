import mediapipe as mp
import cv2 # import the opencv library 
import pyautogui
  
  
# define a video capture object             
vid = cv2.VideoCapture(0) 


# Grabbing the Holistic Model from Mediapipe and
# Initializing the Model    
hand_detector = mp.solutions.hands.Hands() 
 
# Initializing the drawing utils for drawing the facial landmarks on image
mp_drawing = mp.solutions.drawing_utils  


screen_width, screen_height = pyautogui.size()

while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks 

    if hands:
        for hand in hands:
            mp_drawing.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)             
                y = int(landmark.y * frame_height)
                # print(f"The value of x: {x}")
                # print(f"The value of y: {y}")
 
                if id == 8: 
                    cv2.circle(frame, (x,y), 10, (0,255,255))
                    finger_x = screen_height/screen_width*x
                    
                if   id == 12: 
                    cv2.circle(frame, (x,y), 10, (0,255,255))
                    index_x = screen_height/screen_width*x
                    if(abs(index_x - finger_x))  < 7:  
                        pyautogui.keyDown("space")      
                    else:
                        pyautogui.keyUp("space")
             
                    

    # Display the resulting frame 
    cv2.imshow('Video', frame) 

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 

