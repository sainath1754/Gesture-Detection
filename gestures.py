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
            # Initialize list to store landmark coordinates
            landmark_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                # Get the coordinates
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                landmark_list.append([cx, cy])
            # Gesture recognition logic
            if len(landmark_list) != 0:
                # Example logic for gesture recognition
                # Open Hand (Palm) Gesture
                if landmark_list[4][1] < landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "Sainath pragada"
                # Pointing Up Gesture
                elif landmark_list[4][1] > landmark_list[3][1] and landmark_list[8][1] < landmark_list[6][1]:
                    gesture = "connect me in Linkedin" 
                #index base should be higher than index tip and thumb finger should not be in down side position
                else:
                    gesture = None
                
                # Display the corresponding text
                if gesture:
                    cv2.putText(frame, gesture, (landmark_list[0][0] - 50, landmark_list[0][1] - 50),cv2.FONT_HERSHEY_SIMPLEX, 2,(0, 255, 0), 3, cv2.LINE_AA) # Increased fontScale and thickness
    # Step 5: Display the Frame
    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Step 6: Release Resources
cap.release()
cv2.destroyAllWindows()
