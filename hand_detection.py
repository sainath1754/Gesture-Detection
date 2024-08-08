import cv2 
import mediapipe as mp # Library for hand tracking and landmark detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands() #Initializes the hands module for hand detection
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0) #starting the video capture
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break 
    frame = cv2.flip(frame, 1) # Flip the frame horizontally
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)   #Converts the frame from BGR to RGB
    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)  #Draws the detected hand landmarks on the frame
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #to stop the camera
        break
cap.release() #closes the webcam
cv2.destroyAllWindows()
