import cv2
import mediapipe as mp
import time
import math


# ---------------------------------------------
# SilentSign - Basic Emergency Detection
# ---------------------------------------------

# MediaPipe modules
mp_face_mesh = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils


# ---------------------------------------------
# Settings
# ---------------------------------------------

# Eye Aspect Ratio threshold
EAR_THRESHOLD = 0.20

# Number of consecutive frames required
BLINK_FRAMES = 3

# Number of blinks required for SOS
REQUIRED_BLINKS = 3


# ---------------------------------------------
# Helper Function
# ---------------------------------------------

def distance(p1, p2):
    """Calculate distance between two points."""
    return math.sqrt(
        (p1.x - p2.x) ** 2 +
        (p1.y - p2.y) ** 2
    )


def eye_aspect_ratio(landmarks, left=True):
    """
    Calculate a simple eye aspect ratio.
    """

    if left:
        # Left eye landmark indexes
        points = [33, 160, 158, 133, 153, 144]
    else:
        # Right eye landmark indexes
        points = [362, 385, 387, 263, 373, 380]

    p1 = landmarks[points[0]]
    p2 = landmarks[points[1]]
    p3 = landmarks[points[2]]
    p4 = landmarks[points[3]]
    p5 = landmarks[points[4]]
    p6 = landmarks[points[5]]

    vertical_1 = distance(p2, p6)
    vertical_2 = distance(p3, p5)

    horizontal = distance(p1, p4)

    return (vertical_1 + vertical_2) / (2.0 * horizontal)


# ---------------------------------------------
# SOS Function
# ---------------------------------------------

def send_sos(reason):
    """
    Prototype SOS function.

    In a real application this can be connected
    to SMS, Bluetooth, GPS or an emergency server.
    """

    print("\n" + "=" * 50)
    print("           EMERGENCY SOS TRIGGERED")
    print("=" * 50)

    print("Reason:", reason)
    print("Emergency contact notification initiated.")
    print("Location sharing can be added here.")
    print("Bluetooth communication can be added here.")

    print("=" * 50 + "\n")


# ---------------------------------------------
# Camera
# ---------------------------------------------

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()


# ---------------------------------------------
# MediaPipe Models
# ---------------------------------------------

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


# ---------------------------------------------
# Variables
# ---------------------------------------------

blink_counter = 0
blink_count = 0

last_blink_time = 0

SOS_COOLDOWN = 10
last_sos_time = 0

gesture_detected = False


# ---------------------------------------------
# Main Loop
# ---------------------------------------------

while True:

    success, frame = camera.read()

    if not success:
        print("Unable to read camera.")
        break

    frame = cv2.flip(frame, 1)

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # -----------------------------------------
    # Face Detection
    # -----------------------------------------

    face_result = face_mesh.process(rgb_frame)

    if face_result.multi_face_landmarks:

        face_landmarks = (
            face_result.multi_face_landmarks[0]
            .landmark
        )

        left_ear = eye_aspect_ratio(
            face_landmarks,
            left=True
        )

        right_ear = eye_aspect_ratio(
            face_landmarks,
            left=False
        )

        ear = (left_ear + right_ear) / 2

        # Detect closed eyes
        if ear < EAR_THRESHOLD:

            blink_counter += 1

        else:

            # Eye was closed for enough frames
            if blink_counter >= BLINK_FRAMES:

                blink_count += 1
                last_blink_time = time.time()

                print(
                    "Blink detected:",
                    blink_count
                )

            blink_counter = 0

        # Reset blink count after 5 seconds
        if time.time() - last_blink_time > 5:
            blink_count = 0

        # -------------------------------------
        # Blink SOS
        # -------------------------------------

        if blink_count >= REQUIRED_BLINKS:

            if time.time() - last_sos_time > SOS_COOLDOWN:

                send_sos(
                    "Three consecutive eye-blink signals"
                )

                last_sos_time = time.time()

            blink_count = 0


    # -----------------------------------------
    # Hand Gesture Detection
    # -----------------------------------------

    hand_result = hands.process(rgb_frame)

    gesture_detected = False

    if hand_result.multi_hand_landmarks:

        for hand_landmarks in hand_result.multi_hand_landmarks:

            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand_landmarks.landmark

            # ---------------------------------
            # Simple Emergency Gesture
            #
            # Detect a raised/open hand.
            # This is a prototype gesture and
            # can later be replaced by a trained
            # custom gesture classifier.
            # ---------------------------------

            fingers_up = 0

            # Thumb
            if landmarks[4].x < landmarks[3].x:
                fingers_up += 1

            # Index
            if landmarks[8].y < landmarks[6].y:
                fingers_up += 1

            # Middle
            if landmarks[12].y < landmarks[10].y:
                fingers_up += 1

            # Ring
            if landmarks[16].y < landmarks[14].y:
                fingers_up += 1

            # Little
            if landmarks[20].y < landmarks[18].y:
                fingers_up += 1

            # Five fingers = emergency gesture
            if fingers_up == 5:

                gesture_detected = True

                if time.time() - last_sos_time > SOS_COOLDOWN:

                    send_sos(
                        "Emergency hand gesture detected"
                    )

                    last_sos_time = time.time()


    # -----------------------------------------
    # Display Information
    # -----------------------------------------

    cv2.putText(
        frame,
        "SilentSign",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "Blink Count: " + str(blink_count),
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    if gesture_detected:

        cv2.putText(
            frame,
            "EMERGENCY GESTURE DETECTED",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    else:

        cv2.putText(
            frame,
            "Monitoring...",
            (20, 120),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )


    # -----------------------------------------
    # Show Camera
    # -----------------------------------------

    cv2.imshow(
        "SilentSign - Emergency Detection",
        frame
    )


    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


# ---------------------------------------------
# Release Resources
# ---------------------------------------------

camera.release()
cv2.destroyAllWindows()

face_mesh.close()
hands.close()

print("SilentSign stopped.")
