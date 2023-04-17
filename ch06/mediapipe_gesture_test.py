import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 손가락 개수 세기 함수
def count_fingers(hand_landmarks):
    finger_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]
    count = 0
    for finger_tip in finger_tips:
        if hand_landmarks.landmark[finger_tip].y < hand_landmarks.landmark[finger_tip-1].y:
            count += 1
    return count

hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        result = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        if result.multi_hand_landmarks:
            hand_landmarks = result.multi_hand_landmarks[0]
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 손가락 끝이 PIP보다 위에 있고 엄지손가락 끝이 IP보다 오른쪽에 있는 경우
            if (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y) and (hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x):
                print("Okay!")

            # 손가락 개수가 4개인 경우
            elif count_fingers(hand_landmarks) == 4:
                print("palm detection!")

            # 손가락 개수 출력
            finger_count = count_fingers(hand_landmarks)
            if finger_count > 0:
                print("count of finger is " + str(finger_count))

        #cv2.imshow('MediaPipe Hands', frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
