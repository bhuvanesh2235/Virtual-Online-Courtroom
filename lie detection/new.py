import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance as dist
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.optimizers import Adam


mp_face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.7)

emotion_model_path = 'C:\\Users\\gmoha\\PycharmProjects\\justiceapp\\emotion_detection_model_with_neural.h5'
emotion_model = load_model(emotion_model_path, compile=False)


emotion_model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']  # Update with your labels


LIP_COMPRESSION_RATIO = 0.35


FACEMESH_FACE_OVAL = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148,
                      176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109, 10]


LEFT_EYE = [33, 133, 159, 145, 153, 144, 160, 161, 163, 7]
RIGHT_EYE = [263, 362, 386, 374, 380, 373, 387, 388, 390, 249]


def get_aspect_ratio(top, bottom, right, left):
    height = dist.euclidean([top.x, top.y], [bottom.x, bottom.y])
    width = dist.euclidean([right.x, right.y], [left.x, left.y])
    return height / width


def get_lip_ratio(face_landmarks):
    return get_aspect_ratio(face_landmarks[0], face_landmarks[17], face_landmarks[61], face_landmarks[291])


def check_hand_on_face(hands_landmarks, face_landmarks):
    if hands_landmarks:
        face_points = [[(p.x, p.y) for p in [face_landmarks[i] for i in FACEMESH_FACE_OVAL]]]
        face_contours = np.array(face_points, dtype=np.float32)
        for hand_landmarks in hands_landmarks:
            for point in hand_landmarks.landmark:
                if cv2.pointPolygonTest(face_contours, (point.x, point.y), False) >= 0:
                    return True
    return False


def preprocess_face(image, face_landmarks):
    h, w, _ = image.shape
    x_min = int(min([landmark.x for landmark in face_landmarks]) * w)
    x_max = int(max([landmark.x for landmark in face_landmarks]) * w)
    y_min = int(min([landmark.y for landmark in face_landmarks]) * h)
    y_max = int(max([landmark.y for landmark in face_landmarks]) * h)

    face = image[y_min:y_max, x_min:x_max]
    face = cv2.resize(face, (48, 48))  # Assuming the model expects 48x48 input
    face = img_to_array(face)
    face = np.expand_dims(face, axis=0)
    face /= 255.0  # Normalizing
    return face


def get_mood(image, face_landmarks):
    face = preprocess_face(image, face_landmarks)
    predictions = emotion_model.predict(face)
    emotion = emotion_labels[np.argmax(predictions)]
    return emotion


def get_eyeball_position(face_landmarks):
    left_eye_center = np.mean([(face_landmarks[i].x, face_landmarks[i].y) for i in LEFT_EYE], axis=0)
    right_eye_center = np.mean([(face_landmarks[i].x, face_landmarks[i].y) for i in RIGHT_EYE], axis=0)
    left_eye_ratio = get_aspect_ratio(face_landmarks[159], face_landmarks[145], face_landmarks[133], face_landmarks[33])
    right_eye_ratio = get_aspect_ratio(face_landmarks[386], face_landmarks[374], face_landmarks[362],
                                       face_landmarks[263])

    if left_eye_ratio > 0.05 or right_eye_ratio > 0.05:
        if left_eye_center[0] < right_eye_center[0]:
            return "Looking Left"
        elif left_eye_center[0] > right_eye_center[0]:
            return "Looking Right"
    return "Center"


def main():
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        face_results = mp_face_mesh.process(image_rgb)
        hands_results = mp_hands.process(image_rgb)

        if face_results.multi_face_landmarks:
            face_landmarks = face_results.multi_face_landmarks[0].landmark


            if get_lip_ratio(face_landmarks) < LIP_COMPRESSION_RATIO:
                cv2.putText(image, "Lip Compression", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                            cv2.LINE_AA)

            if check_hand_on_face(hands_results.multi_hand_landmarks, face_landmarks):
                cv2.putText(image, "Hand on Face", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


            mood = get_mood(image, face_landmarks)
            cv2.putText(image, f"Mood: {mood}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


            eye_position = get_eyeball_position(face_landmarks)
            cv2.putText(image, f"Eye Position: {eye_position}", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2,
                        cv2.LINE_AA)

        cv2.imshow('Face Analysis', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
